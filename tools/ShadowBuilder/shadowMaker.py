from fontTools.pens.recordingPen import RecordingPen
from mojo.pens import DecomposePointPen
from translationPenAA import TranslationPen

f = CurrentFont()
g = CurrentGlyph()

def makeShadow(g, extrusion):
    destPen = RecordingPen()
    myPen = TranslationPen(destPen, extrusion)
    g.draw(myPen)
    with g.undo("Apply Translate Pen"):
        destPen.replay(g.getPen())
        if g.rightMargin%2==0:
            g.rightMargin+=int(extrusion-20) #20 is compensation for frontWidth in the TranslationPen constructor
        else:
            g.rightMargin+=int(extrusion-19)
        g.changed()

def makeShadowGlyphBackground(g, extrusion):
    shadowGlyph = RGlyph()
    shadowGlyph.width = g.width
    shadowPen = shadowGlyph.getPointPen()
    decomposePen = DecomposePointPen(f, shadowPen)
    g.drawPoints(decomposePen)
    f.insertGlyph(shadowGlyph, name=str(g.name+".shadow"))
    makeShadow(shadowGlyph, extrusion)
    g.drawPoints(decomposePen)
    with c in g:
        c.reverse
        
print(TranslationPen.calcArea)   