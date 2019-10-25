import os, fnmatch
from fontParts.world import OpenFont

minGradeFlag = "MinGrade"
maxGradeFlag = "MaxGrade"

minGradeMasters = []
maxGradeMasters = []

#the following block makes two lists, one list with the masters labeled with "MinGrade", and another with "MaxGrade"
listOfFiles = os.listdir('.')
pattern = "*.ufo"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        if minGradeFlag in entry:
            minGradeMasters.append(entry)
        if maxGradeFlag in entry:
            maxGradeMasters.append(entry)

def makeGrades(maxMaster, minMaster):
    for k in maxMaster.keys():
        if maxMaster[k]:
            maxMaster[k].leftMargin=int(maxMaster[k].leftMargin)
            maxMaster[k].rightMargin=int(maxMaster[k].rightMargin)
            widthDiff=maxMaster[k].width-minMaster[k].width
            if widthDiff%2 == 0:
                minMaster[k].leftMargin+=int(widthDiff/2)
                minMaster[k].rightMargin+=int(widthDiff/2)
            else:
                widthDiff+=1
                minMaster[k].leftMargin+=int(widthDiff/2)-1
                minMaster[k].rightMargin+=int(widthDiff/2)
            minMaster.save()
            maxMaster.save()
            #verifications here
            print(minMaster.info.styleName + " " + minMaster[k].name + " = " + str(minMaster[k].width))
            print(maxMaster.info.styleName + " " + maxMaster[k].name + " = " + str(maxMaster[k].width)+"\n")

for masterMax in maxGradeMasters:
    for masterMin in minGradeMasters:
        if masterMax.replace(maxGradeFlag, "") == masterMin.replace(minGradeFlag, ""):
            maxMaster=OpenFont(masterMax)
            minMaster=OpenFont(masterMin)
            makeGrades(maxMaster, minMaster)