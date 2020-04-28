from fontTools.designspaceLib import DesignSpaceDocument
from fontTools import ttLib
from vanilla import *
import inspect
import defcon

f = CurrentFont()
thisGlyph = CurrentGlyph()
doc = DesignSpaceDocument.fromfile("Crispy[SRIF,wdth,wght].designspace")
coordinateslist = []
doc.loadSourceFonts(ttLib.TTFont,recalcBBoxes=False)

# for i in range(len(fontsList)):
#     nameTag = str(fontsList[i].info.styleName)
#     for glyph in fontsList[i]:
#         compatibilityCounter=0
#         if glyph.name == "H":
#             pointCount = 0
#             for contour in glyph:
#                 for segment in contour.segments:
#                     for points in segment:
#                         pointCount += 1                           
#     tableString = {"Style Name":nameTag, "Number of Points":pointCount}
#     coordinateslist.append(tableString)

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

# ListDemo()
# for i in range(len(fontsList)): 
#     for g in fontsList[i]:
#         if g.name == thisGlyph.name:
#             if fontsList[i].info.styleName != thisGlyph.font.info.styleName:
#                 compatible, report = g.isCompatible(thisGlyph)
#                 print(fontsList[i].info.styleName, g.name)
                
# for fonts in fontsList:
#     if fonts.info.styleName != thisGlyph.font.info.styleName:
#         for g in fonts:
#             compatible, report = g.isCompatible(f[g.name])
