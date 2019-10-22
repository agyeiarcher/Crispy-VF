minMaster=OpenFont('KRSPY-parametric-WideThinMinGrade.ufo', showInterface=False)
maxMaster=OpenFont('KRSPY-parametric-WideThinMaxGrade.ufo', showInterface=False)

def checkWidths():
    for k in maxMaster.keys():
        if maxMaster[k]:
            print(minMaster.info.styleName + " " + minMaster[k].name + " = " + str(minMaster[k].width))
            print(maxMaster.info.styleName + " " + maxMaster[k].name + " = " + str(maxMaster[k].width)+"\n")

def makeGrades():
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
            print(minMaster.info.styleName + " " + minMaster[k].name + " = " + str(minMaster[k].width))
            print(maxMaster.info.styleName + " " + maxMaster[k].name + " = " + str(maxMaster[k].width)+"\n")

makeGrades()