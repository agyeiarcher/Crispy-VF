f=CurrentFont()

for glyph in f.selectedGlyphs:
    glyph.prepareUndo()
    glyph.rightMargin+=10
    glyph.leftMargin+=10
    glyph.performUndo()
