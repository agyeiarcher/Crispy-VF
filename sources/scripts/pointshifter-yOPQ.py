g=CurrentGlyph()
f=CurrentFont()

rightinsidelabel='RIGHTINSIDE'
leftinsidelabel='LEFTINSIDE'
topinsidelabel='TOPINSIDE'
bottominsidelabel='BOTTOMINSIDE'
crossbartoplabel='CROSSBARTOP'
crossbarbottomlabel='CROSSBARBOTTOM'
crossbarlabel='CROSSBAR'
sidenotchlabel='SIDENOTCH'

crossbartiltlabel = 'CROSSBARTILT'
topnotchlabel='TOPNOTCH'
outnotchlabel='OUTNOTCH'
topseriflabel='TOPSERIF'
bottomseriflabel='BOTTOMSERIF'



print(g.name)
   
def yOPQ():
    
    #be careful to manually check for: J,
    
    stemwidth=2
    topbaradjustment=620*0.7
    crossbaradjustment=360*0.7
    
    g.prepareUndo() 
    
    for c in g: 
       
        for p in c.points:
            if topinsidelabel in p.labels:
                p.move((0,-topbaradjustment)) 
                if topnotchlabel in p.labels:
                    if p.x<g.width/2:
                        p. move((40,0))
            g.changed()   
               
            if bottominsidelabel in p.labels:
                p.move((0,topbaradjustment))
                g.changed()
               
            if crossbarlabel in p.labels:
                if p.y<f.info.xHeight:
                    p.move((0,-crossbaradjustment/2))
                if p.y>f.info.xHeight: 
                    p.move((0,crossbaradjustment/2))
                g.changed()
                
            if crossbartoplabel in p.labels:
                p.move((0,crossbaradjustment/2))
                g.changed()
            if crossbarbottomlabel in p.labels:
                p.move((0,-crossbaradjustment/2))
                g.changed()
                   
            if outnotchlabel in p.labels:
                if p.y>f.info.xHeight:
                    p.move((0,-topbaradjustment-stemwidth+(f.info.capHeight-p.y)))
                if p.y<f.info.xHeight:
                    p.move((0,(topbaradjustment-p.y)+stemwidth))
                g.changed()
                
            if sidenotchlabel in p.labels:
                if p.y>f.info.xHeight:
                    p.move((0,-topbaradjustment-stemwidth+(f.info.capHeight-p.y)))
                if p.y<f.info.xHeight:
                    p.move((0,(topbaradjustment-p.y)+stemwidth))
                g.changed()
    
            if topseriflabel in p.labels:
                if g.name is 'Q':
                    p.move((0,-topbaradjustment/2))
                else:
                    p.move((0,-topbaradjustment+(f.info.capHeight-p.y)))
                g.changed()
    
            if bottomseriflabel in p.labels: 
                p.move((0,topbaradjustment-p.y+2))
                g.changed()

g.performUndo()
 
def clearLabels():
    for c in g:
            for p in c.points:
                p.labels=[]
                

# clearLabels()
# xTRA()
yOPQ()
            

# print(f.info.xHeight)