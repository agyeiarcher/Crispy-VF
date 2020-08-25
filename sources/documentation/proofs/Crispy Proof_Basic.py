from pyNewsApi import PYNEWS

variableFontPath = "../../../font/variable_ttf/Crispy[srif,wdth,wght]-VF.ttf"

allCapSpacingString = "HHOHHOOHOO HHAHHOOAOO HHBHHOOBOO HHCHHOOCOO HHDHHOODOO HHEHHOOEOO HHFHHOOFOO HHGHHOOGOO HHIHHOOIOO HHJHHOOJOO HHKHHOOKOO HHLHHOOLOO HHMHHOOMOO HHNHHOONOO HHPHHOOPOO HHQHHOOQOO HHRHHOOROO HHSHHOOSOO HHTHHOOTOO HHUHHOOUOO HHVHHOOVOO HHWHHOOWOO HHXHHOOXOO HHYHHOOYOO HHZHHOOZOO"

spacingStringBox = (40, 20, 690, 500)

def randomHeadline():
    news = PYNEWS()
    data = news.get_headline_by_source(source='google-news')
    return data[randint(0, len(data)-1)]["title"]

def calcTextSizeForBox(txt, box, minSize, maxSize, tolerance):
    #calcTextSizeForBox function written originally by Just Van Rossum (thanks Just!)
    # font needs to already have been set
    #
    # We're implementing a so called binary search here. We have a minimum value,
    # a maximum value, and an initial value that we set right in the middle of
    # min and max. The approach is then to see "is this value too high (there's
    # an overflow)" or too low or maybe correct enough (no overflow).
    # If there's an overflow, the maxValue will be set to the current value,
    # and the value itsels is again placed right between min and max.
    # If there's no overflow, the minValue is set to the current value.
    # Soon, the value will be very close to the minSize value, and then
    # we're done.
    #
    # This kind of algorithm is more efficient than just trying a lot of values
    # in sequence, and can scale quite well.
    #
    fs = (minSize + maxSize) / 2
    while True:
        # Yes, this is potentially an endless loop, but
        # we (try to) guarantee that it always terminates
        fontSize(fs)
        overflow = textOverflow(txt, box)
        if overflow:
            maxSize = fs
            fs = (minSize + maxSize) / 2
            if fs - minSize < tolerance:
                fs = minSize
                # giving up, there will be overflow
                break
        else:
            if fs - minSize < tolerance:
                # close enough, done
                break
            minSize = fs
            fs = (minSize + maxSize) / 2
    return fs

def pageLabel(instanceName):
    font("")
    text(str(instanceName), (40, height() - 40))


for instanceName, setupMatrix in listNamedInstances(variableFontPath).items():
    duplicatecheck = []
    print(instanceName, setupMatrix)
    newPage("LetterLandscape")
    # with savedState():
    #     stroke(0)
    #     fill()
    #     rect(40, 40, width() - 100, height() - 130)
    pageLabel(instanceName)    
    fontVariations(wght= setupMatrix['wght'])
    fontVariations(wdth = setupMatrix['wdth'])
    fontVariations(SRIF = setupMatrix['SRIF'])
    font(variableFontPath)
    fs = calcTextSizeForBox(allCapSpacingString, spacingStringBox, minSize=5, maxSize=100, tolerance=0.1)
    print(fs)
    fontSize(fs)
    lineHeight(fs * 1.2)
    spacingText = textBox(allCapSpacingString, spacingStringBox, align="left")
    
    newPage("LetterLandscape")
    pageLabel(instanceName) 
    fontVariations(wght= setupMatrix['wght'])
    fontVariations(wdth = setupMatrix['wdth'])
    fontVariations(SRIF = setupMatrix['SRIF'])
    font(variableFontPath)
    textHeadline = randomHeadline().upper()
    fs = calcTextSizeForBox(textHeadline, spacingStringBox, minSize=5, maxSize=400, tolerance=0.1)
    fontSize(fs*0.8)
    lineHeight(fs*0.9)
    sampleWords = textBox(textHeadline, spacingStringBox, align="left")
    # print(fs)