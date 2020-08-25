variableFontPath = "../../../font/variable_ttf/Crispy[srif,wdth,wght]-VF.ttf"
fontList = listNamedInstances(variableFontPath).values()
variationsList = list(listFontVariations(variableFontPath).keys())
matrixList = list(listNamedInstances(variableFontPath).items())
# print(matrixList)
# for matrix in matrixList:
#     print(matrix)

# print(listNamedInstances(fontPath).values())
# print(fontList)
# for i in fontList:
#     # variationsString = str(i).replace(":", "=").replace("{", "").replace("}", "").replace("'", "")
#     # print(variationsString)
#     font(fontPath)
#     fontVariations(wght= 1.0, wdth= 15.0, SRIF= 1.0)
#     text("HELLO Q", (100, 100))

def pageLabel(instanceName):
    font("")
    text(str(instanceName), (40, height()-40))

for instanceName, setupMatrix in listNamedInstances(variableFontPath).items():
    print(instanceName, setupMatrix)
    newPage("LetterLandscape")
    fontVariations(wght= setupMatrix['wght'])
    fontVariations(wdth = setupMatrix['wdth'])
    fontVariations(SRIF = setupMatrix['SRIF'])
    pageLabel(instanceName)
    font(variableFontPath)
    text("HELLO Q", (40, 100))

# print(list(listFontVariations(fontPath).keys()))
# for variations in list(listFontVariations(fontPath).keys()):
#     print(variations)

