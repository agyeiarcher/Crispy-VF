from fontTools.misc.transform import Transform
from math import radians

g = CurrentGlyph()

def getGlyph(glyph, skew, rotation, addComponents=False, skipComponents=False):
    skew = radians(skew)
    rotation = radians(-rotation)

    dest = g
    
    if skew == 0 and rotation == 0:
        return dest

    for contour in dest:
        for bPoint in contour.bPoints:
            bcpIn = bPoint.bcpIn
            bcpOut = bPoint.bcpOut
            if bcpIn == (0, 0):
                continue
            if bcpOut == (0, 0):
                continue
            if bcpIn[0] == bcpOut[0] and bcpIn[1] != bcpOut[1]:
                bPoint.anchorLabels = ["extremePoint"]
            if rotation and bcpIn[0] != bcpOut[0] and bcpIn[1] == bcpOut[1]:
                bPoint.anchorLabels = ["extremePoint"]

    cx, cy = 0, 0
    box = glyph.bounds
    if box:
        cx = box[0] + (box[2] - box[0]) * .5
        cy = box[1] + (box[3] - box[1]) * .5

    t = Transform()
    t = t.skew(skew)
    t = t.translate(cx, cy).rotate(rotation).translate(-cx, -cy)

    if not skipComponents:
        dest.transformBy(tuple(t))
    else:
        for contour in dest.contours:
            contour.transformBy(tuple(t))

        # this seems to work !!!
        for component in dest.components:
            # get component center
            _box = glyph.layer[component.baseGlyph].bounds
            if not _box:
                continue
            _cx = _box[0] + (_box[2] - _box[0]) * .5
            _cy = _box[1] + (_box[3] - _box[1]) * .5
            # calculate origin in relation to base glyph
            dx = cx - _cx
            dy = cy - _cy
            # create transformation matrix
            tt = Transform()
            tt = tt.skew(skew)
            tt = tt.translate(dx, dy).rotate(rotation).translate(-dx, -dy)
            # apply transformation matrix to component offset
            P = RPoint()
            P.position = component.offset
            P.transformBy(tuple(tt))
            # set component offset position
            component.offset = P.position

    dest.extremePoints(round=0)
    for contour in dest:
        for point in contour.points:
            if "extremePoint" in point.labels:
                point.selected = True
                point.smooth = True
            else:
                point.selected = False
    dest.removeSelection()
    dest.round()
    return dest

print(getGlyph(g, 8, 0))