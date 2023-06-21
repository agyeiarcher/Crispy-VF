# from pyNewsApi import PYNEWS
import io, os, glob

fontPath = '/Users/aamacbook/Work Interim/Crispy-VF/sources/designspaces/WEIGHTWIDTHSERIF/instances/Sample-CrispyLC/Crispy Terminal Medium V2-accents.otf'

filetype = "*.txt"

spacingStringBox = (40, 40, 690, 500)

texts = []

for filename in os.listdir("texts"):
    if not filename.startswith('.'): #bypass .DS_STORE files in case
        textFilePath = os.getcwd()+"/texts/"+filename
        with open(textFilePath, "r", encoding="utf-8") as f:
            print(textFilePath)
            textString = f.read()
        texts.append(textString)
    
allCapSpacingString = "HAHBHCHDHEHFHGHHHIHJHKHLHMHNHOHHHPHQHRHSHTHUHVHWHXHYHZH \n OAOBOCODOEOFOGOHOIOJOKOLOMONOOOOOPOQOROSOTOUOVOWOXOYOZO"

def randomHeadline():
    news = PYNEWS()
    data = news.get_headline_by_source(source='google-news')
    return data[randint(0, len(data))]["title"]

def calcTextSizeForBox(txt, box, minSize=5, maxSize=300, tolerance=0.1):
    fs = (minSize + maxSize) / 2
    
    fontSize(fs)
    lineHeight(fs)
    overflow = textOverflow(txt, box)
    if overflow:
        while overflow:
            fs += -0.5
            fontSize(fs)
            lineHeight(fs)
            overflow = textOverflow(txt, box)
    else:
        while not overflow:
            fs += 0.5
            fontSize(fs)
            lineHeight(fs)
            overflow = textOverflow(txt, box)
    return fs

def pageLabel(instanceName):
    font("")
    text(str(instanceName), (40, height() - 40))

def makeProof(proofString):
    newPage("LetterLandscape")
    font(fontPath)
    fs = calcTextSizeForBox(proofString, spacingStringBox)
    print(fs)
    fontSize(fs*0.7)
    if fs<20:
        lineHeight(fs*1.2)
    else:
        lineHeight(fs)
    spacingText = textBox(proofString, spacingStringBox, align="left")

for proofStrings in texts:       
    makeProof(proofStrings)
saveImage()