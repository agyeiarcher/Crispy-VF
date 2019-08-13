glyph=CurrentGlyph()

def xOPQ(stemAdjustment):

    glyph.prepareUndo()
    
    for i in range(len(glyph.contours)):
        
        noShiftingRight=True
        noShiftingLeft=True
        
        for point in glyph.contours[i].selection:
            if point.x > glyph.width/2:
                point.moveBy((stemAdjustment,0))
                noShiftingRight=False
                print("right contour points moved by "+str(stemAdjustment)+ " points")
            if point.x < glyph.width/2:
                point.moveBy((-stemAdjustment,0))
                noShiftingLeft=False

        if noShiftingRight is False:
            glyph.rightMargin+=stemAdjustment
        if noShiftingLeft is False:
            glyph.leftMargin+=stemAdjustment

xOPQ(130)

print(glyph.contours)