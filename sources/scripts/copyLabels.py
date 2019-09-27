f=CurrentFont()
g=CurrentGlyph()

contourLabels={}

def fetchLabels(f):
    for k in f.keys():
        # print(f[k].name)
        labelList=[]
        for contour in f[k]:
            # print(contour)
            for segment in contour:
               for point in segment:
                   labelList.append(point.labels)
                   
        print(f[k].name+": "+str(labelList))                

fetchLabels(f)

# for k in h.keys():
#     for glyph in h[k]:
#         print(h[k].name)
#         for c in glyph:
#             for p in c:
#                 p.labels=templateLabel
