import fontParts

g=CurrentGlyph()

def xOPQ(stemAdjustment):
    
    #625 for wides, 500 for narrows
        
    # for glyph in f.selectedGlyphs:
        
    g.prepareUndo()

    for contour in g.contours:
                
        noShiftingRight=True
        noShiftingLeft=True
    
        if g.name is 'W':
            stemAdjustment=stemAdjustment/2
            
        for point in contour.selection:
            if point.x > g.width/2:
                point.moveBy((stemAdjustment,0))
                noShiftingRight=False
                print("right contour points moved by "+str(stemAdjustment)+ " points")
            if point.x < g.width/2:
                point.moveBy((-stemAdjustment,0))
                noShiftingLeft=False
                print("left contour points moved by "+str(stemAdjustment)+ " points")

        if not noShiftingRight:
            g.rightMargin+=stemAdjustment*1.2
        if not noShiftingLeft:
            g.leftMargin+=stemAdjustment*1.2
    
    g.changed()    
    g.performUndo()
    
xOPQ(1017)
 