from math import pi, radians, degrees, tan, hypot, atan2, cos, sin
from fontTools.ufoLib.pointPen import PointToSegmentPen, SegmentToPointPen, ReverseContourPointPen
from fontTools.misc.bezierTools import splitCubicAtT
from penCollection.outlinePen import OutlinePen
from fontTools.pens.basePen import BasePen
from fontTools.pens.recordingPen import RecordingPen
from mojo.pens import DecomposePointPen
from fontTools.misc.transform import Identity
from fontPens.transformPointPen import TransformPointPen

f = CurrentFont()
g = CurrentGlyph()

_ANGLE_EPSILON = pi/36

extrusionX = -180
extrusionY = -180

def calcVector(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x2 - x1
    dy = y2 - y1
    return dx, dy

def calcAngle(point1, point2):
    dx, dy = calcVector(point1, point2)
    return atan2(dy, dx)

def polarCoord(coordsxy, angle, distance, extrusion=160): #this basically defined the coordinates for the x+y of the translation. i think.
    (x,y)=coordsxy
    nx = x + (distance * cos(angle))+extrusionX
    ny = y + (distance * sin(angle))+extrusionY
    return nx, ny

def calcArea(points):
    l = len(points)
    area = 0
    for i in range(l):
        x1, y1 = points[i]
        n = (i+1)%l #modified here to test for n values
        x2, y2 = points[int(n)]  #modified here to return int to stop throwing error
        area += (x1*y2)-(x2*y1)
    return area / 2 #modified here to return int to stop throwing error

def firstDerivative(coords1, c_coords1, c_coords2, coords2, value):
    x1, y1=coords1
    cx1, cx2=c_coords1
    x2, y2=coords2
    cy1, cy2=c_coords2
    mx = bezierTangent(x1, cx1, cx2, x2, value)
    my = bezierTangent(y1, cy1, cy2, y2, value)
    return mx, my

def bezierTangent(a, b, c, d, t):
    # Implementation of http://stackoverflow.com/questions/4089443/find-the-tangent-of-a-point-on-a-cubic-bezier-curve-on-an-iphone
    return (-3*(1-t)**2 * a) + (3*(1-t)**2 * b) - (6*t*(1-t) * b) - (3*t**2 * c) + (6*t*(1-t) * c) + (3*t**2 * d)
    
class TranslationPen(BasePen):
    """
    Draw an outline resulting from the reunion of an initial contour and a translated version thereof.
    Translation is defined by an angle and a width/length.
    This kind of drawing basically produces a calligraphic effect (in a translated manner as Gerrit Noordzij puts it),
    it can also serve as a way of extruding a shape for 3D shadow effects.
    """
    
    def __init__(self, otherPen, frontAngle=0, frontWidth=20):
        self.otherPen = otherPen
        self.frontAngle = radians(frontAngle)
        self.offset = polarCoord((0,0), radians(frontAngle), frontWidth)
        self.points = []
    

    def _moveTo(self, pt):
        self.points.append((pt, 'move'))

    def _lineTo(self, pt1):
        pt0, previousType = self.points[-1]
        angle = calcAngle(pt0, pt1)
        self.translatedLineSegment(pt0, pt1)
        self.points.append((pt1, 'line'))

    def _curveToOne(self, c1, c2, pt1):
        pt0, previousType = self.points[-1]
        newSegments = self.splitAtAngledExtremas(pt0, c1, c2, pt1)
        if len(newSegments):
            for segment in newSegments:
                pt0, c1, c2, pt1 = segment
                self.translatedCurveSegment(pt0, c1, c2, pt1)
        else:
            self.translatedCurveSegment(pt0, c1, c2, pt1)
        self.points.append((c1, None))
        self.points.append((c2, None))
        self.points.append((pt1, 'curve'))

    def endPath(self):
        self.points = []

    def closePath(self):
        previousPoint, previousType = self.points[-1]
        if previousType in ['line','curve']:
            pt0, pt1 = self.points[-1][0], self.points[0][0]
            self.translatedLineSegment(pt0, pt1)
            self.points = []

    def splitAtAngledExtremas(self, pt0, pt1, pt2, pt3):
        frontAngle = self.frontAngle
        segments = []
        for i in range(101):
            t = i / 100
            nx, ny = firstDerivative(pt0, pt1, pt2, pt3, t)
            tanAngle = atan2(ny, nx)
            if tan(frontAngle - _ANGLE_EPSILON) < tan(tanAngle) < tan(frontAngle + _ANGLE_EPSILON):
                newSegments = splitCubicAtT(pt0, pt1, pt2, pt3, t)
                if len(newSegments) > 1:
                    segments = newSegments
                    break
        return segments

    def translatedCurveSegment(self, pt0, c1, c2, pt1):
        ox, oy = self.offset
        #added the declarations to compensate for def((x,x), (x,x)) not working in Py3
        x0, y0 = pt0
        xc1, yc1 = c1
        xc2, yc2 = c2
        x1, y1 = pt1
        pen = self.getPen([(x0, y0), (x1, y1), (x1+ox, y1+oy), (x0+ox, y0+oy)])
        pen.moveTo((x0, y0))
        pen.curveTo((xc1, yc1), (xc2, yc2), (x1, y1))
        pen.lineTo((x1+ox, y1+oy))
        pen.curveTo((xc2+ox, yc2+oy), (xc1+ox, yc1+oy), (x0+ox, y0+oy))
        pen.closePath()
        

    def translatedLineSegment(self, pt0, pt1):
        ox, oy = self.offset  
        x0, y0 = pt0
        x1, y1 = pt1
        # print("XXXX", [pt0, pt1, x1+ox, y1+oy, x0+ox, y0+oy])
        pen = self.getPen([pt0, pt1, (x1+ox, y1+oy), (x0+ox, y0+oy)])
        pen.moveTo(pt0)
        pen.lineTo(pt1)
        pen.lineTo((x1+ox, y1+oy))
        pen.lineTo((x0+ox, y0+oy))
        pen.closePath()

    def getPen(self, points):
        area = calcArea(points)
        if area < 0:
            pen = self.getReversePen()
        else:
            pen = self.otherPen
        return pen
    
    def returnExtrapolation(self, transformation):
        ox, oy = self.offset
        print(ox,oy)

    def getReversePen(self):
        adapterPen = PointToSegmentPen(self.otherPen)
        reversePen = ReverseContourPointPen(adapterPen)
        return SegmentToPointPen(reversePen)

    def addComponent(self, baseGlyphName, transformation):
        self.otherPen.addComponent(baseGlyphName, transformation)
        

def makeShadow(g, extrusionX, extrusionY):
    destPen = RecordingPen()
    myPen = TranslationPen(destPen)
    g.draw(myPen)
    with g.undo("Apply Translate Pen"):
        destPen.replay(g.getPen())
        if g.rightMargin%2==0:
            g.rightMargin+=int(extrusionX-20) #20 is compensation for frontWidth in the TranslationPen constructor
        else:
            g.rightMargin+=int(extrusionX-19)
        g.changed()

def makeShadowGlyphBackground(g):
    m  = Identity
    m = m.scale(1.01,1.006)
    m = tuple(m)
    shadowGlyph = RGlyph()
    shadowGlyph.width = g.width
    shadowPen = shadowGlyph.getPointPen()
    transformPen = TransformPointPen(shadowPen, m)
    decomposePen = DecomposePointPen(f, transformPen)
    g.drawPoints(decomposePen)
    f.insertGlyph(shadowGlyph, name=str(g.name+".shadow"))

def makeShadowGlyph(g):
    f.prepareUndo()
    m  = Identity
    m = m.scale(1)
    m = tuple(m)
    makeShadowGlyphBackground(g)
    shadowGlyph = f[str(g.name+".shadow")]
    makeShadow(shadowGlyph, extrusionX, extrusionY)
    shadowGlyph.removeOverlap()
    insetPen = shadowGlyph.getPointPen()
    transformPen = TransformPointPen(insetPen, m)
    reversePen = ReverseContourPointPen(transformPen)
    g.drawPoints(reversePen)
    outlinePen = OutlinePen(f, contrast=0, offset=1, connection="square", miterLimit=10)
    g.draw(outlinePen)
    outlinePen.drawSettings(drawInner=True, drawOuter=True)
    outlinePen.drawPoints(insetPen)
    f.performUndo()

makeShadowGlyph(g)