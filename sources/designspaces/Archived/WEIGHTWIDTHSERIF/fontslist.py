from fontTools.designspaceLib import DesignSpaceDocument
from vanilla import *
import inspect
import defcon

f = CurrentFont()
thisGlyph = CurrentGlyph()
doc = DesignSpaceDocument()
doc.read("Crispy[SRIF,wdth,wght].designspace")
referenceFileName = doc.sources[0].familyName #this assumed a well-made designspace file with correctly named font masters.
coordinateslist = []

fontsList =  doc.loadSourceFonts(defcon.Font)

for i in range(len(fontsList)):
    nameTag = str(fontsList[i].info.styleName)
    for glyph in fontsList[i]:
        compatibilityCounter=0
        if glyph.name == thisGlyph.name:
            pointCount = 0
            for contour in glyph:
                for segment in contour.segments:
                    for points in segment:
                        pointCount += 1
        for refFonts in fontslist:
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