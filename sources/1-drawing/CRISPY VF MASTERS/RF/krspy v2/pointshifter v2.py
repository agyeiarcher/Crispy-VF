glyph = CurrentGlyph()

# labelName = 'top'
# g = CurrentGlyph()
# g.prepareUndo()
# for c in g:
#     for b in c.bPoints:
#         if labelName in b.naked().labels:
#             b.move((0, 200))
# g.performUndo()

p='douche'

for contour in glyph:
        for point in contour.points:
                print(point.labels)
                if p in point.labels:
                    point.moveBy((0,20))