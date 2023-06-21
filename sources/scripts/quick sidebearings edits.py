f=CurrentFont()

def adjustSidebearings(amt):
    for glyph in f.selectedGlyphs:
        if glyph:
            glyph.prepareUndo()
            glyph.rightMargin+=amt
            glyph.leftMargin+=amt
            glyph.performUndo()

adjustSidebearings(180)


