from mojo.UI import *
f=CurrentFont()
g=FindGlyph(f)
for k in AllFonts():
    OpenGlyphWindow(k[g.name])