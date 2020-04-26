from fontTools.designspaceLib import DesignSpaceDocument
from vanilla import *

f = CurrentFont()
thisGlyph = CurrentGlyph()
doc = DesignSpaceDocument()
doc.read("Crispy[SRIF,wdth,wght].designspace")
referenceFileName = doc.sources[0].familyName #this assumed a well-made designspace file with correctly named font masters.
fontslist = []
coordinateslist = []

if f.info.familyName == referenceFileName: #this basically checks for making sure that the Glyphs you're checking against is a glyph from a font in the designspace you're querying
    for master in doc.sources:
        fontslist.append(master.path)

for fonts in fontslist:
    thisFont = OpenFont(fonts, showInterface=False)
    nameTag = str(thisFont.info.styleName)
    pointCount = 0
    for glyph in thisFont:
        compatibilityCounter = 0
        if glyph.name == thisGlyph.name:
            for contour in glyph:
                for p in contour.points:
                    pointCount+=1
        for refFonts in fontslist:
            refFont = OpenFont(refFonts, showInterface=False)
            compatible = glyph.isCompatible(refFont[glyph.name])
            if compatible:
                compatibilityCounter+=1
    print(compatibilityCounter)
            
    tableString = {"Style Name":nameTag, "Number of Points":pointCount}
    coordinateslist.append(tableString)

class ListDemo(object):

    def __init__(self):
        self.w = FloatingWindow((400, 400))
        self.w.myList = List((0, 0, -0, -0),
                     coordinateslist,
                     columnDescriptions=[{"title": "Style Name"}, {"title": "Number of Points"}],
                     selectionCallback=self.selectionCallback)
        self.w.open()

    def selectionCallback(self, sender):
        print("testing")

ListDemo()