g=CurrentGlyph()
f=CurrentFont()

wideTransform = -566
narrowTransform = -460

def yOPQ(stemAdjustment):
    g.prepareUndo()
    for contour in g.contours:
        for point in contour.selection:
            if point.y < f.info.capHeight/2:
                point.moveBy((0,-stemAdjustment))
                print("top contour points moved by "+str(stemAdjustment)+ " points")
            elif point.y > f.info.capHeight/2:
                point.moveBy((0,stemAdjustment))
                print("top contour points moved by "+str(stemAdjustment)+ " points")
    g.changed()
    g.performUndo()

if f.info.styleName == "x0y1000t0":
    yOPQ(narrowTransform)
elif f.info.styleName == "x0y1000t1000":
    yOPQ(wideTransform)

print(f.info.styleName)