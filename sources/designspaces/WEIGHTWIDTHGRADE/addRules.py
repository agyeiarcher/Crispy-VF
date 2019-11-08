from designSpaceDocument import DesignSpaceDocument
doc = DesignSpaceDocument()
doc.read("Crispy[GRAD,SHDW,wdth,wght].designspace")
print(doc.axes)
doc.sources
doc.instances