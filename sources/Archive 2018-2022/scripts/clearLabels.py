g=CurrentGlyph()

def clearLabels():
    for c in g:
            for p in c.points:
                p.labels=[]
                
clearLabels()