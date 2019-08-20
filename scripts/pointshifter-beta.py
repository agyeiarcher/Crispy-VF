f=CurrentFont()

def xOPQ(stemAdjustment):
        
    for glyph in f.selectedGlyphs:

        for i in range(len(glyph.contours)):
        
            glyph.prepareUndo()
            
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
                    print("left contour points moved by "+str(stemAdjustment)+ " points")

            if noShiftingRight is False:
                glyph.rightMargin+=stemAdjustment*1.2
            if noShiftingLeft is False:
                glyph.leftMargin+=stemAdjustment*1.2
            
            glyph.performUndo()
    
# xOPQ(220)

def yOPQ(stemAdjustment):
    
    for glyph in f.selectedGlyphs:        
                
        for i in range(len(glyph.contours)):
            
            glyph.prepareUndo()

            for point in glyph.contours[i].selection:
                if point.y < f.info.capHeight/2:
                    point.moveBy((0,stemAdjustment))
                    print("top contour points moved by "+str(stemAdjustment)+ " points")
                if point.y > f.info.capHeight/2:
                    point.moveBy((0,-stemAdjustment))
                    print("top contour points moved by "+str(stemAdjustment)+ " points")
            
            glyph.performUndo()

yOPQ(-60)