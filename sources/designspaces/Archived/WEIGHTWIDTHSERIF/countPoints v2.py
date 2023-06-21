from fontTools.designspaceLib import DesignSpaceDocument
from vanilla import *
import inspect
import defcon

f = CurrentFont()
thisGlyph = CurrentGlyph()
doc = DesignSpaceDocument()
doc.read("Crispy[SRIF,wdth,wght].designspace")
coordinateslist = []
problemsList = []
for k in doc.sources:
    print(k.path)

for k in doc.sources:
    b = OpenFont((k.path), showInterface=False)
    for glyph in b:
        if glyph.name == CurrentGlyph().name:
             # print(glyph.font.info.familyName + " " + glyph.font.info.styleName)
             pointCount = 0
             for contour in glyph:
                 for segment in contour.segments:
                     for points in segment:
                         pointCount += 1          
             errorCount = 0
             for refFonts in doc.sources:
                temp = OpenFont((refFonts.path), showInterface=False)
                compatible, report = glyph.isCompatible(temp[glyph.name])
                if compatible:
                    errorCount+=0
                else:
                    errorCount+=1
                    # print("no!", temp.info.styleName)
                    # print('\n    ')
                if errorCount>len(doc.sources)/2:
                    errorFlag =  "\U0001F494"
                else:
                    errorFlag = "\U0001F49A"
                tableString = {"Style Name":b.info.styleName, "Number of Points":pointCount, "Compatibility":errorFlag}
                temp.close()
             coordinateslist.append(tableString)
    b.close()

class ShowCompatibility(object):

    def __init__(self):
        self.w = FloatingWindow((400, 400))
        self.w.myList = List((0, 0, -0, -0),
                     coordinateslist,
                     columnDescriptions=[{"title": "Style Name"}, {"title": "Number of Points"}, {"title": "Compatibility"}],
                     selectionCallback=self.selectionCallback)
        self.w.open()

    def selectionCallback(self, sender):
        print("testing")

ShowCompatibility()