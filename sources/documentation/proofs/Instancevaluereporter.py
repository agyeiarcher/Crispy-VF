import markdown
from fontTools.designspaceLib import DesignSpaceDocument

instanceNameString = "| Instance Name |"
filePath = "CRISPY-PARAMETRIC AXES.designspace"

def carpenter(designSpaceFile):
    headerString = ""
    columnSetup = "| :------- |"
    tableString = ""
    doc = DesignSpaceDocument()
    doc.read(designSpaceFile)
    doc.axes
    doc.sources
    doc.instances
    for axisNames in doc.axes:
        headerString+= " "+axisNames.name+" |"
    tableHeading = instanceNameString+headerString
    for additionalColumns in range(len(doc.axes)):
        columnSetup += " -------: |"
    for instances in doc.instances:
        valueString = "| "
        for axisLocationValue in instances.location.values():
            valueString+= str(axisLocationValue) +  " |"
        finalString = instances.styleName + "" + valueString +"\n"
        tableString+= finalString                
    finalTable = tableHeading + "\n" + columnSetup + "\n" + tableString
    return finalTable

instancesReport = markdown.markdown(carpenter(filePath), extensions=['tables'])
with open("testfile.md", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(instancesReport)
    
