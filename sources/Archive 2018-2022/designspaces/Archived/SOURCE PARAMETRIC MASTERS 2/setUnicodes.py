import os

gradesFolderPath = "../designspaces/WEIGHTWIDTHGRADE/"                

def listFonts(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        if filenames:
            if ".ufo" in dirnames:
                return(dirnames)
for font in fonts:
    font.prepareUndo()
    for g in font.keys():
        if g:
            font[g].autoUnicodes()
    font.changed()
    font.performUndo()
print(f"{font.info.familyName} Unicode values set")
