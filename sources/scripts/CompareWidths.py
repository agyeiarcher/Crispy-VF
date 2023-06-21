f = CurrentFont()
glyphlist = []
for glyphs in f:
    if glyphs:
        n = glyphs.name
        glyphlist.append(n)
glyphlist.sort()

for glyphs in glyphlist:
    print(glyphs + " " + str(f[glyphs].width))
        