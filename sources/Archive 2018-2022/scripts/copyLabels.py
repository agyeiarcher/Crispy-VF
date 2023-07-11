f=OpenFont()
g=OpenFont()

contourLabels={}

def fetchLabels():
    for k in f.keys():
        # print(f[k].name)
        labelList=[]
        for contour in f[k]:
            # print(contour)
            for segment in contour:
               for point in segment:
                    b=point.labels
                    for contour in h[k]:
                        for segment in contour
                            for point in segment:
                                point.labels=b            

fetchLabels()

# for k in h.keys():
#     for glyph in h[k]:
#         print(h[k].name)
#         for c in glyph:
#             for p in c:
#                 p.labels=templateLabel
