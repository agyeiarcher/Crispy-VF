f = CurrentFont()
g = CurrentGlyph()

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
        
xTRA(3500)
