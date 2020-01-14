af = AllFonts()
f = CurrentFont()
g = CurrentGlyph()

styleName = f.info.styleName

#making batches of letter groups below, to check for different things. The xCheckGroup lists are flattened to check if any characters are duplicated, so spacing isn't applied more than once to any one character. If they are, they're skipped over and reported

rightSideNotch = ["O", "B", "K", "D", "R", "W", "V", "X", "three", "eight", "K.narrow", "M.narrow", "B.narrow"]
leftSideNotch = ["A", "U", "X","O", "G.wide", "G", "C", "eight", "six", "nine", "Q"]

rightSideFlat = ["J", "Q", "M", "N", "U", "H", "A", "N.wide", "I.narrow", "three.wide", "Y.alt", "zero", "one.narrow", "U.narrow", "N.narrow"]
leftSideFlat = ["D", "M", "N", "K", "B", "E", "F", "P", "R", "W", "V", "L", "H", "E.wide", "F.wide", "I.narrow", "zero", "K.narrow", "U.narrow", "M.narrow","B.narrow", "N.narrow"]

rightSideSpecial = ["Z", "P", "T", "Y", "L", "Z.wide", "C.wide", "S.wide", "E.wide", "E", "F", "F.wide", "S", "I", "C", "G", "L.wide", "one", "five", "five.wide", "four", "seven", "six", "nine", "two"]
leftSideSpecial = ["J", "Z", "Y", "Z.wide", "S", "T", "I", "five.wide", "three.wide", "S.wide", "Y.alt", "one", "three", "five", "four", "seven", "one.narrow", "two"]

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
            rightSideNotchValue = 260 
            leftSideNotchValue = 260         
            rightSideFlatValue = 380
            leftSideFlatValue = 380
            rightSideSpecialValue = 160
            leftSideSpecialValue  = 160
            rightPunctValue = 50
            leftPunctValue = 50
        if styleName == "x0y1000t1000":
            rightSideNotchValue = 160 AllFonts
            leftSideNotchValue = 160         
            rightSideFlatValue = 200
            leftSideFlatValue = 200
            rightSideSpecialValue = 130
            leftSideSpecialValue  = 130
            rightPunctValue = 50
            leftPunctValue = 50
        if styleName == "x1000y0t1000":
            rightSideNotchValue = 160 
            leftSideNotchValue = 160         
            rightSideFlatValue = 200
            leftSideFlatValue = 200
            rightSideSpecialValue = 130
            leftSideSpecialValue  = 130
            rightPunctValue = 50
            leftPunctValue = 50
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
            rightSideNotchValue = 45-25
            leftSideNotchValue = 45-25        
            rightSideFlatValue = 66-25
            leftSideFlatValue = 66-25
            rightSideSpecialValue = 30-25
            leftSideSpecialValue  = 30-25
            rightPunctValue = 25-15
            leftPunctValue = 25-15

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