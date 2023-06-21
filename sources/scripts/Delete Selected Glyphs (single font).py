af = AllFonts()
for f in af:
    f.prepareUndo()
    for glyphs in f:
        if glyphs.selected:
            print(glyphs.selected)
            f.removeGlyph(glyphs.name)
        f.performUndo()
    f.changed()