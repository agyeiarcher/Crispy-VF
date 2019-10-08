maxMaster=OpenFont('/Users/aamacbook/Work Interim/Krspy-VF/sources/drawing/krspy v2/instances/KRSPY-parametric-NarrowThinMaxGrade.ufo')
minMaster=OpenFont('/Users/aamacbook/Work Interim/Krspy-VF/sources/drawing/krspy v2/instances/KRSPY-parametric_NarrowThinMinGrade.ufo')

for k in maxMaster.keys():
    if maxMaster[k]:
        maxMaster[k].leftMargin=int(maxMaster[k].leftMargin)
        maxMaster[k].rightMargin=int(maxMaster[k].rightMargin)
        widthDiff=maxMaster[k].width-minMaster[k].width
        minMaster[k].leftMargin+=int(widthDiff/2)
        minMaster[k].rightMargin+=int(widthDiff/2)
        print(minMaster[k].width)
        print(maxMaster[k].width)
