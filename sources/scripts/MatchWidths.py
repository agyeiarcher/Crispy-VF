maxMaster=OpenFont('/Users/aamacbook/Work Interim/Krspy-VF/sources/drawing/krspy v2/instances/KRSPY-NB-MaxG.ufo')
minMaster=OpenFont('/Users/aamacbook/Work Interim/Krspy-VF/sources/drawing/krspy v2/instances/KRSPY-NB-MinG.ufo')

for k in maxMaster.keys():
    if maxMaster[k]:
        print(maxMaster.info.styleName+" "+maxMaster[k].name+" width: "+str(maxMaster[k].width))