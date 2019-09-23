glyph = CurrentGlyph()
f= CurrentFont()

from collections import OrderedDict

# labelName = 'top'
# g = CurrentGlyph()
# g.prepareUndo()
# for c in g:
#     for b in c.bPoints:
#         if labelName in b.naked().labels:
#             b.move((0, 200))
# g.performUndo()

def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

p='douche'

Plabels=[]    

for k in f.keys():
    for contour in f[glyph.name]:
            for point in contour.points:
                    if point.labels is not ' ':
                        # print(point.labels)
                        b=' '.join(str(l) for l in point.labels)
            if b not in Plabels:
                Plabels.append(b)
print(Plabels)
                    
                    