af = AllFonts()
f = CurrentFont()
g = CurrentGlyph()

styleName = f.info.styleName

#making batches of letter groups below, to check for different things. The xCheckGroup lists are flattened to check if any characters are duplicated, so spacing isn't applied more than once to any one character. If they are, they're skipped over and reported

rightSideFlat = ["J", "Q", "M", "N", "H", "I.narrow", "three.wide", "E", "E.wide", "E.wideskinny", "F", "F.wide", "Y","Y.wide","Y.wideskinny", "zero", "one.narrow", "U.narrow", "N.narrow","M.narrow", "L", "I","P", "C"]
rightSideNotch = ["O", "B","B.skinnymiddle", "K", "D", "R", "W", "V", "X", "three", "eight",  "S.wide", "S", "S.wideskinny", "T", "C.wide"]

leftSideFlat = ["R.wide", "D", "M", "N", "K", "B", "B.skinnymiddle", "E", "F", "P", "R", "W", "V", "L","L.wide", "H", "E.wide", "F.wide", "I.narrow", "zero", "K.narrow", "U.narrow", "N.narrow", "Y","Y.wide","Y.wideskinny", "I"]
leftSideNotch = ["X","O", "G.wideskinny","G.wide", "G", "C", "eight", "six", "nine", "Q","M.narrow", "S.wide", "S", "S.wideskinny", "T"]

rightSideSpecial = ["A", "Z", "Z.wide","G", "one", "five", "five.wide", "four", "seven", "six", "nine", "two"]
leftSideSpecial = ["A", "J", "Z", "Z.wide", "five.wide", "three.wide", "one", "three", "five", "four", "seven", "one.narrow", "two"]

rightPunct=["comma", "period"]
leftPunct=["comma", "period"]

rightGroup = [rightSideNotch, rightSideSpecial, rightSideFlat, rightPunct]
leftGroup = [leftSideNotch, leftSideSpecial, leftSideFlat, leftPunct]

#using a list comprehension to flatten the lists
rightSideCheckGroup = [k for l in rightGroup for k in l] #using a list comprehension to flatten the lists
leftSideCheckGroup = [k for l in leftGroup for k in l]

def checkDuplicates(listToCheck):
    seen = set()
    for x in listToCheck:
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
        
        #this group of conditionals is very...bad
        
        if styleName == "x0y0t1000":
            rightSideNotchValue = 440 
            leftSideNotchValue = 440         
            rightSideFlatValue = 590
            leftSideFlatValue = 590
            rightSideSpecialValue = 390
            leftSideSpecialValue = 390 
            rightPunctValue = 100
            leftPunctValue =100
        if styleName == "x0y1000t1000":
            rightSideNotchValue = 440 
            leftSideNotchValue = 440         
            rightSideFlatValue = 590
            leftSideFlatValue = 590
            rightSideSpecialValue = 390
            leftSideSpecialValue = 390 
            rightPunctValue = 100
            leftPunctValue =100
        if styleName == "x1000y0t1000":
            rightSideNotchValue = 190 
            leftSideNotchValue = 190         
            rightSideFlatValue = 380
            leftSideFlatValue = 380
            rightSideSpecialValue = 100 
            leftSideSpecialValue = 100   
            rightPunctValue = 100
            leftPunctValue = 100
        if styleName == "x0y0t0":
            rightSideNotchValue = 35
            leftSideNotchValue = 35        
            rightSideFlatValue = 47
            leftSideFlatValue = 47
            rightSideSpecialValue = 29
            leftSideSpecialValue = 29       
            rightPunctValue = 21
            leftPunctValue = 21
        if styleName ==  "x0y1000t0":
            rightSideNotchValue = 29
            leftSideNotchValue = 29        
            rightSideFlatValue = 34
            leftSideFlatValue = 34
            rightSideSpecialValue = 29
            leftSideSpecialValue = 29       
            rightPunctValue = 21
            leftPunctValue = 21
        if styleName == "x1000y0t0":
            rightSideNotchValue = 10
            leftSideNotchValue = 10   
            rightSideFlatValue = 22
            leftSideFlatValue = 22
            rightSideSpecialValue = 9
            leftSideSpecialValue = 9
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

# for font in af:
setSpacing(f)
print(f"edited spacing for {f.info.familyName} {f.info.styleName}")