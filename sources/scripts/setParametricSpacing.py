af = AllFonts()
f = CurrentFont()
g = CurrentGlyph()

styleName = f.info.styleName

#making batches of letter groups below, to check for different things. The xCheckGroup lists are flattened to check if any characters are duplicated, so spacing isn't applied more than once to any one character. If they are, they're skipped over and reported

rightSideNotch = ["O", "B", "K", "D", "R", "W", "V", "X"]
leftSideNotch = ["A", "U", "X","O", "S.wide", "G.wide", "G", "C"]

rightSideFlat = ["J", "Q", "M", "N", "U", "H", "A", "N.wide", "I.narrow", "three.wide"]
leftSideFlat = ["M", "N", "K", "B", "E", "F", "P", "R", "W", "V", "L", "H", "E.wide", "F.wide", "N.wide", "I.narrow"]

rightSideSpecial = ["Z", "P", "T", "Y", "L", "Z.wide", "C.wide", "S.wide", "E.wide", "E", "F", "F.wide", "S", "I", "C"]
leftSideSpecial = ["J", "Z", "Y", "Z.wide", "S", "T", "I", "five.wide", "three.wide"]

rightPunct=["comma", "period"]
leftPunct=["comma", "period"]

rightGroup = [rightSideNotch, rightSideSpecial, rightSideFlat, rightPunct]
leftGroup = [leftSideNotch, leftSideSpecial, leftSideFlat, leftPunct]

rightSideCheckGroup = [k for l in rightGroup for k in l]
leftSideCheckGroup = [k for l in leftGroup for k in l]

def checkDuplicates(onelist):
    seen = set()
    for x in onelist:
        if x in seen: 
            return True
        seen.add(x)
    return False

def allClear(rightSideCheckGroup, leftSideCheckGroup):
    rightSideCheck = True
    leftSideCheck = True
    if checkDuplicates(rightSideCheckGroup):
        print("right group duplicates found. please resolve")
        rightSideCheck = False
    if checkDuplicates(leftSideCheckGroup):
        print("left group duplicates found. please resolve")
        leftSideCheck = False
    if rightSideCheck and leftSideCheck: return True
    
#we just need to cross-ref this before running the script at all. if there's a duplicate, fix it before we get started. doh fuck up.
    
def setSpacing(f):
    if allClear(rightSideCheckGroup, leftSideCheckGroup):
        if styleName == "x0y0t1000":
            rightSideNotchValue = 185
            leftSideNotchValue = 185        
            rightSideFlatValue = 240
            leftSideFlatValue = 240
            rightSideSpecialValue = 85
            leftSideSpecialValue  = 85
            rightPunctValue = 60
            leftPunctValue = 60
        if styleName == "x0y1000t1000":
            rightSideNotchValue = 85+40  
            leftSideNotchValue = 85+40         
            rightSideFlatValue = 125+40
            leftSideFlatValue = 125+40
            rightSideSpecialValue = 70+40
            leftSideSpecialValue  = 70+40
            rightPunctValue = 120
            leftPunctValue = 120
        if styleName == "x1000y0t1000":
            rightSideNotchValue = 85+65  
            leftSideNotchValue = 85+65         
            rightSideFlatValue = 125+65
            leftSideFlatValue = 125+65
            rightSideSpecialValue = 70+65
            leftSideSpecialValue  = 70+65
            rightPunctValue = 60
            leftPunctValue = 60
        if styleName == "x0y0t0":
            rightSideNotchValue = 29
            leftSideNotchValue = 29        
            rightSideFlatValue = 34
            leftSideFlatValue = 34
            rightSideSpecialValue = 27
            leftSideSpecialValue  = 27
            rightPunctValue = 21
            leftPunctValue = 21
        if styleName ==  "x0y1000t0":
            rightSideNotchValue = 27
            leftSideNotchValue = 27        
            rightSideFlatValue = 31
            leftSideFlatValue = 31
            rightSideSpecialValue = 25
            leftSideSpecialValue  = 25
            rightPunctValue = 21
            leftPunctValue = 21
        if styleName == "x1000y0t0":
            rightSideNotchValue = 45
            leftSideNotchValue = 45        
            rightSideFlatValue = 66
            leftSideFlatValue = 66
            rightSideSpecialValue = 30
            leftSideSpecialValue  = 30
            rightPunctValue = 25
            leftPunctValue = 25

        for g in f.keys():
            #set right margins
            f[g].prepareUndo()
            if f[g].name in rightSideNotch:
                f[g].rightMargin = rightSideNotchValue
            if f[g].name in rightSideFlat:
                f[g].rightMargin =  rightSideFlatValue
            if f[g].name in rightSideSpecial:
                f[g].rightMargin =  rightSideSpecialValue


            if f[g].name in leftSideNotch:
                f[g].leftMargin =  leftSideNotchValue
            if f[g].name in leftSideFlat:
                f[g].leftMargin =  leftSideFlatValue
            if f[g].name in leftSideSpecial:
                f[g].leftMargin =  leftSideSpecialValue
                        
            if f[g].name in rightPunct:
                f[g].rightMargin = rightSideNotchValue
            if f[g].name in leftPunct:
                f[g].rightMargin = rightSideNotchValue

            f[g].changed()
            f[g].performUndo()

setSpacing(f)