f= CurrentFont()

print

from collections import OrderedDict

# labelName = 'top'
# g = CurrentGlyph()
# g.prepareUndo()
# for c in g:
#     for b in c.bPoints:
#         if labelName in b.naked().labels:
#             b.move((0, 200))
# g.performUndo()


def BuildLabelsList(theFont):
    Plabels=[]    
    for glyph in theFont:
        for contour in glyph:
                for point in contour.points:
                    # print(point.labels)
                    b=point.labels
                if b not in Plabels:
                    Plabels=Plabels+b
                    Plabels=list(dict.fromkeys(Plabels)) #remove duplicates
    print(Plabels)
    return Plabels


                    