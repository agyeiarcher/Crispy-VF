f=CurrentFont()

def xOPQ(stemAdjustment):
        
    for glyph in f.selectedGlyphs:
        
        glyph.prepareUndo()

        for contour in glyph.contours:
                    
            noShiftingRight=True
            noShiftingLeft=True
 
            for point in contour.selection:
                if point.x > glyph.width/2:
                    point.moveBy((stemAdjustment,0))
                    noShiftingRight=False
                    print("right contour points moved by "+str(stemAdjustment)+ " points")
                if point.x < glyph.width/2:
                    point.moveBy((-stemAdjustment,0))
                    noShiftingLeft=False
                    print("left contour points moved by "+str(stemAdjustment)+ " points")

            if not noShiftingRight:
                glyph.rightMargin+=stemAdjustment*1.2
            if not noShiftingLeft:
                glyph.leftMargin+=stemAdjustment*1.2
        
        glyph.changed()    
        glyph.performUndo()
    
# xOPQ(460/1.61803398875)

def yOPQ(stemAdjustment):
    
    for glyph in f.selectedGlyphs:        
        
        glyph.prepareUndo()
        for contour in glyph.contours:
        
            for point in contour.selection:
                if point.y < f.info.capHeight/2:
                    point.moveBy((0,stemAdjustment))
                    print("top contour points moved by "+str(stemAdjustment)+ " points")
                elif point.y > f.info.capHeight/2:
                    point.moveBy((0,-stemAdjustment))
                    print("top contour points moved by "+str(stemAdjustment)+ " points")
        glyph.changed()
        glyph.performUndo()

# yOPQ(220)

def xTRA(stemAdjustment):
    
    #letters=612
    #figs=528
        
    for glyph in f.selectedGlyphs:
        
        glyph.prepareUndo()

        for contour in glyph.contours:
                    
            shiftingRight=False
            shiftingLeft=False
 
            for point in contour.selection:
                if point.x < glyph.width/2:
                    point.moveBy((-stemAdjustment,0))                    
                    shiftingLeft=True
                    print("stems moved by "+str(stemAdjustment)+ " points")
                if point.x > glyph.width/2:
                    point.moveBy((stemAdjustment,0))
                    shiftingRight=True
                    print("stems moved by "+str(stemAdjustment)+ " points")
        
            if shiftingRight:
                glyph.rightMargin+=stemAdjustment
            if shiftingLeft:
                glyph.leftMargin+=stemAdjustment
        
        glyph.changed()    
        glyph.performUndo()
    
xTRA(528)

