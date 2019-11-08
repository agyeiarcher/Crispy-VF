f = CurrentFont()
for g in f.keys():
    if f[g]:
        flag = ".shadow"
        if flag not in f[g].name:
            print("<sub name=" +'"'+str(f[g].name)+'"'+ " with= " + '"' + str(f[g].name+".shadow")+'">')