g=CurrentGlyph()

def xOPQ(stemAdjustment):
    
    #625 for wides, 500 for narrows
        
    # for glyph in f.selectedGlyphs:
        
    g.prepareUndo()
    
    if g.width<1000:
        stemAdjustment=stemAdjustment*0.85
        spacingEdit=stemAdjustment*1.1

    for contour in g.contours:
                
        noShiftingRight=True
        noShiftingLeft=True
            
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
            g.rightMargin+=spacingEdit
        if not noShiftingLeft:
            g.leftMargin+=spacingEdit
    
    g.changed()    
    g.performUndo()
    
xOPQ(1017/2)
  