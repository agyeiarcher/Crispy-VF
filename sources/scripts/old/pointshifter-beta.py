

def yOPQ(stemAdjustment):
    
    #top and bottom bars=165
    #crossbars=155/-155
    
    #narrow tops: 150
    #narrow bottoms: 120
    
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