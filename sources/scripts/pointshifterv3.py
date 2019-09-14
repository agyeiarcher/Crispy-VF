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

listyy=["test", "no", "dollars", "no"]

Plabels=[]    

for glyph in f:
    for contour in glyph:
            for point in contour.points:
                # print(point.labels)
                b=point.labels
            if b not in Plabels:
                Plabels=Plabels+b
print(Plabels)
                    