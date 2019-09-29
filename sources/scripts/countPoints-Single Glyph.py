g=CurrentGlyph()
i=0
for c in g:
    for p in c.points:
        i+=1               
print(i)