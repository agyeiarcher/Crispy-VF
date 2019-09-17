g=CurrentGlyph()
f=CurrentFont()

rightstemlabel='RIGHTSTEM'
leftstemlabel='LEFTSTEM'
outnotchlabel = 'OUTNOTCH'
crossbarlabel = 'CROSSBAR'
insidenotchlabel = 'INSIDENOTCH'
sidenotchlabel = 'SIDENOTCH'
topnotchlabel = 'TOPNOTCH'
bottomseriflabel = 'BOTTOMSERIF'
topseriflabel = 'TOPSERIF'
insidenotchrightlabel = 'INSIDENOTCHRIGHT'
insidenotchleftlabel = 'INSIDENOTCHLEFT'

twosides=['M', 'W', 'I','Q', 'T']
crossbars=['F','E']
notaswide=['J', 'L']

print(g.name)

#PLEASE VERIFY GLYPHS ANYWAY, ESPECIALLY: S

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
                if g.name is 'I':
                    if p.x>g.width/2:
                        p.move((widthadjustment/2.25,0))
                    if p.x<g.width/2:
                        p.move((-widthadjustment/2.25,0))
                elif g.name in twosides:
                    p.move((widthadjustment*0.5,0))
                elif g.name in notaswide:
                    p.move((widthadjustment*0.9,0))
                else:
                    p.move((widthadjustment,0))
                    
            if leftstemlabel in p.labels:
                p.move((-widthadjustment*0.5,0))
                    
            #top/bottom notch points
            if topnotchlabel in p.labels:
                if p.x>g.width/2:
                    p.move((- topnotchadjustment,0))
                if p.x<g.width/2:
                    p.move((topnotchadjustment,0))
            
            #vert stem notch points
            if sidenotchlabel in p.labels:
                if p.y<f.info.xHeight:
                    p.move((0,240))
                if p.y>f.info.xHeight:
                    p.move((0,-240))
            
            #two way e.g. X,8,B vert stem notch points
            if outnotchlabel in p.labels:
                if p.y<f.info.xHeight:
                    p.move((0,-outnotchadjustment))
                if p.y>f.info.xHeight: 
                    p.move((0,outnotchadjustment*0.95 ))
                    
            if insidenotchlabel in p.labels:
                if g.name in twosides:
                    if p.x<g.width/2:
                        p.move((insidenotchadjustment,0))
                else:
                    p.move((-insidenotchadjustment,0))
    
            #'serif' lengths
            if topseriflabel in p.labels:
                p.move( (0,-topserifadjustment))
            if bottomseriflabel in p.labels:
                p.move( (0,bottomserifadjustment))         
            #crossbar angle compensation
            if crossbarlabel in p.labels:
                if p.y<f.info.xHeight:
                    p.move((0,-160))
                if p.y>f.info.xHeight:
                    p.move((0,40))
                if g.name is 'S':
                    p.move((0,100))           
            if insidenotchrightlabel in p.labels:
                p.move((insidenotchadjustment/2,0))
            if insidenotchleftlabel in p.labels:
                p.move((-insidenotchadjustment/2,0))
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