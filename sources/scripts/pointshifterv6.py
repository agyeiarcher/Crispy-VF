g=CurrentGlyph()
f=CurrentFont()

rightstemlabel='RIGHTSTEM'
outnotchlabel = 'OUTNOTCH'
insidenotchlabel = 'INSIDENOTCH'
sidenotchlabel = 'SIDENOTCH'
topnotchlabel = 'TOPNOTCH'
bottomseriflabel = 'BOTTOMSERIF'
topseriflabel = 'TOPSERIF'

twosides=['M', 'W', 'I']
crossbars=['F','E']
notaswide=['J', 'L']

print(g.name)

def xTRA():
    
    widthadjustment=4500
    topnotchadjustment=580
    sidenotchadjustment=240    
    outnotchadjustment=300
    topserifadjustment=150
    bottomserifadjustment=150
    insidenotchadjustment=420
    
    for c in g:
        for p in c.points:
            g.prepareUndo()
            
            if rightstemlabel in p.labels:
                if g.name in twosides:
                    print("yer")
                    if p.x>g.width/2:
                        p.move((widthadjustment*0.5,0))
                    if p.x<g.width/2:
                        p.move((-widthadjustment*0.5,0))
                        
                if g.name in twosides and 'I':
                    if p.x>g.width/2:
                        p.move((widthadjustment/2.25,0))
                    if p.x<g .width/2:
                        p.move((-widthadjustment/2.25,0))
                        
                if g.name in notaswide:
                    p.move((widthadjustment*0.9,0))
                if g.name in notaswide and 'L':
                    p.move((widthadjustment*0.8,0))
                else:
                    p.move((widthadjustment,0))
                    
            #top/bottom notch points
            if topnotchlabel in p.labels:
                if p.x>g.width/2:
                    p.move((-topnotchadjustment,0))
                if p.x<g.width/2:
                    p.move((topnotchadjustment,0))
                g.changed()
            #vert stem notch points
            if sidenotchlabel in p.labels:
                p.move((0,-240))
                g.changed()  
             #two way e.g. X,8,B vert stem notch points
            if outnotchlabel in p.labels:
                if p.y<f.info.xHeight:
                    p.move((0,-outnotchadjustment))
                if p.y>f.info.xHeight:
                    p.move((0,outnotchadjustment*0.95))
                g.changed()
 
            if insidenotchlabel in p.labels:
                p.move( (-insidenotchadjustment,0))
             #'serif' lengths
            if topseriflabel in p.labels:
                p.move( (0,-topserifadjustment)) 
            if bottomseriflabel in p.labels:
                p.move( (0,bottomserifadjustment))
            
             #compensate spacing for new glyph width
            
            g.leftMargin=0.022*g.width
            g.rightMargin=g.leftMargin
            g.changed()  
             
            g.performUndo()  
 
def clearLabels():
    for c in g:
            for p in c.points:
                p.labels=[]
                
# clearLabels()

xTRA()


# print(f.info.xHeight)