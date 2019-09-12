f=CurrentFont()

def adjustSidebearings(amt)

for glyph in f.selectedGlyphs:
    glyph.prepareUndo()
    glyph.rightMargin+=amt
    glyph.leftMargin+=amt
    glyph.performUndo()

adjustSidebearings(-12)


