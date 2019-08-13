glyph=CurrentGlyph()

glyph.prepareUndo()

for point in glyph.contours[0].selection:
    point.moveBy((-20,0))