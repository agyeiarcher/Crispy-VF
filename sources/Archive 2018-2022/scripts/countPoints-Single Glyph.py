af = AllFonts()

for font in af:
    for glyph in font:
        i=0
        for c in glyph:
            for p in c.points:
                i+=1               
    print(glyph.name, i)