f = CurrentFont()
f.prepareUndo()
for glyphs in f:
    if glyphs.selected:
        f.removeGlyph(glyphs.name)
    f.performUndo()