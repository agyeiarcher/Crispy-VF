from vanilla import *

af = AllFonts()
g = CurrentGlyph()

print(g.name)

def getReport(fontsList):
    report = ""
    for fonts in fontsList:
        #you can look up RFont in the FontParts documentation to see more things you can do with this 
        for glyph in fonts: 
            #you can look up RGlyph in the FontParts documentation to see more things you can do with this
            if glyph.name == g.name:
                i=0
                for contour in glyph:
                    for p in contour.points:
                        i+=1 #add 1 to i every time you encounter a point, done for each counter in the specified glyph
                report+= f"{glyph.name} in {fonts.info.styleName} has {i} points \n"
    return report

class PointCounter(object):
    def __init__(self):
        self.w = FloatingWindow((300, 22*len(af)), "Points Counter")  
        self.w.textBox = TextBox((10, 10, -10, 20*len(af)), getReport(af), alignment='left')        
        self.w.open()

PointCounter()