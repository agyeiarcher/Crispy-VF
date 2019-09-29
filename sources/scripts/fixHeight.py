f=CurrentFont()
for g in f.keys():
    f[g].prepareUndo()
    f[g].scale((0.8,0.8))
    for c in f[g]:
        for s in c:
            for p in s:
                for p in s:
                    if isinstance(p.y, float):
                        p.y=int(round(p.y))
                    if isinstance(p.x, float):
                        p.x=int(round(p.x))
    if isinstance(f[g].rightMargin, float):
        f[g].rightMargin=int(round(f[g].rightMargin))
    if isinstance(f[g].leftMargin, float):
        f[g].leftMargin=int(round(f[g].leftMargin))
    f[g].width=f[g].width*0.8
    f.info.capHeight=1600
    f.info.ascender=1600
    f.info.xHeight=800
    f.info.descender=-400
    f[g].changed()
    f[g].performUndo()
    
    