g=CurrentGlyph()
f=CurrentFont()

rightinsidelabel='RIGHTINSIDE'
leftinsidelabel='LEFTINSIDE'
topinsidelabel='TOPINSIDE'
bottominsidelabel='BOTTOMINSIDE'
crossbarlabel='CROSSBAR'
topnotchlabel='TOPNOTCH'

print(g.name)

def yOPQ():
    
   yopqadjustment=f.info.xHeight/2
   g.prepareUndo()
   for c in g:
       for p in c.points:
           if topinsidelabel in p.labels:
               p.move((0,-700))
               if topnotchlabel in p.labels:
                   if p.x<g.width/2:
                       p.move((200,0))
               g.changed()
               
           if bottominsidelabel in p.labels:
               p.move((0,700))
               g.changed()
               
           if crossbarlabel in p.labels:
                if p.y<f.info.xHeight:
                   p.move((0,-550))
                if p.y>f.info.xHeight:
                   p.move((0,150))

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