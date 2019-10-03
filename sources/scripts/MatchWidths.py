maxMaster=OpenFont('/Users/aamacbook/Work Interim/Krspy-VF/sources/drawing/krspy v2/instances/NarrowBlackMaxGrade copy.ufo')
minMaster=OpenFont('/Users/aamacbook/Work Interim/Krspy-VF/sources/drawing/krspy v2/instances/NarrowBlackMinGrade copy.ufo')

for k in maxMaster.keys():
    if maxMaster[k]:
        # widthDiff=maxMaster[k].width-minMaster[k].width
        # minMaster[k].leftMargin+=widthDiff/2
        # minMaster[k].rightMargin+=widthDiff/2
        print(minMaster[k].width)
        print(maxMaster[k].width)
