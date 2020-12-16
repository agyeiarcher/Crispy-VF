import ufoProcessor, os, fontmake, subprocess
from fontmake import font_project

parametricDesignSpacePath = "../designspaces/SOURCE PARAMETRIC MASTERS/CRISPY-PARAMETRIC AXES copy.designspace"
mastersDesignSpacePath = "../designspaces/WEIGHTWIDTHSERIF/Crispy[SRIF,wdth,wght].designspace"
mastersFolderPath = "../designspaces/WEIGHTWIDTHSERIF/sources/"

primary_mastersFolderPath = "../designspaces/SOURCE PARAMETRIC MASTERS/instances/"
primary_xopqParametricsPath = "../designspaces/SOURCE PARAMETRIC MASTERS/instances/minXOPQ/"
primary_xtraParametricsPath = "../designspaces/SOURCE PARAMETRIC MASTERS/instances/minXTRA/"
primary_yopqParametricsPath = "../designspaces/SOURCE PARAMETRIC MASTERS/instances/minYOPQ/"

sub_mastersFolderPath = "../designspaces/SOURCE PARAMETRIC MASTERS/duplicateinstances/"
sub_xopqParametricsPath = "../designspaces/SOURCE PARAMETRIC MASTERS/duplicateinstances/minXOPQ/"
sub_xtraParametricsPath = "../designspaces/SOURCE PARAMETRIC MASTERS/duplicateinstances/minXTRA/"
sub_yopqParametricsPath = "../designspaces/SOURCE PARAMETRIC MASTERS/duplicateinstances/minYOPQ/"


defaultsFolderPath = "../designspaces/WEIGHTWIDTHGRADE/Defaults/"
variableFontFolderPath = "../../font/variable_ttf/"
ParametricFontFolderPath = "../../font/variable_ttf/Parametric Version/"
buildScript = '/Users/aamacbook/Work\ Interim/Crispy-VF/build.sh'
baseStyles = ['Wide Thin', 'Wide Medium', 'Wide Black', 'Standard Thin', 'Standard Medium', 'Standard Black', 'Narrow Thin', 'Narrow Medium', 'Narrow Black']
maxFonts = []
minFonts = []
allTheFonts = []
finalFont = fontmake.font_project.FontProject()

def listFonts(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        if filenames:                
            return(dirnames)
                
def generateMasters(designSpacePath):
    ufoProcessor.build(designSpacePath, useVarlib=True, roundGeometry=True)
    # print("Instance builds completed")
    # return listFonts(primary_mastersFolderPath)

def separatemasters(path, maxVal, minVal):
    fontList = os.listdir(path)
    for f in fontList:
        if maxVal in f:
           maxFonts.append(path+f)
        if minVal in f:
           minFonts.append(path+f)
    return maxFonts, minFonts
       
def makePairs(path, stylename, maxVal, minVal):
    separatemasters(path, maxVal, minVal)
    arrayname = []
    for f in maxFonts:
        if stylename in f:
            arrayname.append(f)
            for m in minFonts:
                if stylename in m:
                    arrayname.append(m)
            return(list(dict.fromkeys(arrayname))) #list(dict.fromkeys(x)) is a good way to get a list with stripped duplicates

def makeDefaults(sourceFolderPath, styles, maxQuery, minQuery, midFactor, saveFolderPath): #these "queries" are for separating and making masters based on one range (e.g. weight, width based on strings in the filename)
    if len(styles) % 2 != 0:
        print("Incompatible number of masters. Please check your shit, sir")
    else:
        for stylename in styles:
            allTheFonts.append((makePairs(sourceFolderPath, stylename, maxQuery, minQuery)))
        # print(allTheFonts)
        i=0
        for pairs in allTheFonts:
            font3 = NewFont(showInterface = False)
            font1 = OpenFont(pairs[0], showInterface = False)
            font2 = OpenFont(pairs[1], showInterface = False)
            font3.interpolate(midFactor, font1, font2)
            font3.info.familyName = "Crispy"
            font3.info.styleName = styles[i]
            font3.changed()
            font3.save(saveFolderPath + "Crispy" + " " + styles[i] + ".ufo")
            print(f"Made a font for Crispy {styles[i]}")
            i+=1

def setUnicodes(folderPath):
    for fontFiles in listFonts(folderPath):
        if ".ufo" in fontFiles:
            font = OpenFont(folderPath+fontFiles, showInterface = False)
            for g in font.keys():
                font[g].autoUnicodes()
            font.changed()
            font.save(folderPath + font.info.familyName + " " + font.info.styleName + ".ufo")
            print(f"{font.info.familyName} {font.info.styleName} Unicodes auto-generated")

def matchWidths(folderPath):
    for style in baseStyles:
        thisPair = (makePairs(folderPath, style, "MaxGrade", "MinGrade"))
        print(thisPair)
        maxMaster = OpenFont(thisPair[0], showInterface = False)
        minMaster = OpenFont(thisPair[1], showInterface = False)
        for glyph in maxMaster.keys():
            if maxMaster[glyph]:
                maxMaster[glyph].leftMargin=int(maxMaster[glyph].leftMargin)
                maxMaster[glyph].rightMargin=int(maxMaster[glyph].rightMargin)
                widthDiff=maxMaster[glyph].width-minMaster[glyph].width
                minMaster[glyph].leftMargin+=int(widthDiff/2)
                minMaster[glyph].rightMargin+=int(widthDiff/2)
                if minMaster[glyph].width > maxMaster[glyph].width:
                     minMaster[glyph].rightMargin += -1
                if maxMaster[glyph].width > minMaster[glyph].width:
                     maxMaster[glyph].rightMargin += -1
                # print(f"Min Master ---> {minMaster.info.styleName} left margin: {minMaster[glyph].leftMargin} | right margin: {minMaster[glyph].rightMargin} | width: {minMaster[glyph].width}")
                # print(f"Max Master ---> {maxMaster.info.styleName} left margin: {maxMaster[glyph].leftMargin} | right margin: {maxMaster[glyph].rightMargin} | width: {maxMaster[glyph].width}")
        maxMaster.save(folderPath + maxMaster.info.familyName + " " + maxMaster.info.styleName + ".ufo")
        minMaster.save(folderPath + minMaster.info.familyName + " " + minMaster.info.styleName + ".ufo")
       
def bash_command(cmd):
    subprocess.Popen(cmd, shell=True, executable='/bin/bash')
    
# MAKE GRADED MASTERS
generateMasters(parametricDesignSpacePath)
# matchWidths(mastersFolderPath)
# matchWidths(yopqParametricsPath)
# setUnicodes(mastersFolderPath)
# generateMasters(mastersDesignSpacePath) #this is just so there are some static font files for reference in the instances
finalFont.build_variable_font(parametricDesignSpacePath, output_dir = variableFontFolderPath, ttf=True, optimize_gvar=True, use_production_names=True, reverse_direction=True, conversion_error=None, feature_writers=None, cff_round_tolerance=None)