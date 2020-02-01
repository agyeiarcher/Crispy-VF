import os

gradesFolderPath = "../designspaces/WEIGHTWIDTHGRADE/MASTERS/"                

def listFonts(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        if filenames:
            return(dirnames)
            
for fontFiles in listFonts(gradesFolderPath):
    if ".ufo" in fontFiles:
        font = OpenFont(gradesFolderPath+fontFiles, showInterface = False)
        for g in font.keys():
            font[g].autoUnicodes()
        print(f"{font.info.familyName} {font.info.styleName} Unicodes auto-generated")

# for font in fonts:
#     font.prepareUndo()
#     for g in font.keys():
#         if g:
#             font[g].autoUnicodes()
#     font.changed()
#     font.performUndo()
# print(f"{font.info.familyName} Unicode values set")
