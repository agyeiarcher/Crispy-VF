from vanilla import *
from mojo.events import addObserver, removeObserver
from AppKit import NSApp, NSPanel

debug = True

class FontsCheckBox(object):

    def __init__(self):
        checkname = 'select fonts'
        windowname = 'comparing widths'
        self.i=10
        self.checkWindow = Window((200, 140+(len(AllFonts())*self.i*1.2)), checkname)
        self.varDict = {}
        self.fontsToSend = []
        for self.i in range(len(AllFonts())):
            self.varDict["string{0}".format(self.i)] = AllFonts()[self.i].info.styleName
        print(self.varDict)
        for varName, font in self.varDict.values():
            checkbox = CheckBox((5, 10+self.i, -10, 20), font, callback=self.checkBoxCallback, value=False)
            setattr(self.checkWindow, varName, checkbox)
            self.i+=20
        self.checkWindow.button = Button((10, (len(AllFonts())*25), -10, 20), "Compare Width Metrics", callback=self.buttonCallback)
        self.checkWindow.open()
                
        self.glyphlist = []
        self.columnlist=[]
        self.f1 = ""
        self.f2 = "" 
                
        self.listWindow = FloatingWindow((600, 400), windowname)
        self.listWindow.bind('close', self.windowClose)
        for window in [listWindow for listWindow in NSApp().windows() if listWindow.isVisible()]:
            if window.title() == windowname:
                window.close()   

    def checkBoxCallback(self, sender):
        if sender.get()==1:
            if sender.getTitle() in (list(self.varDict.values())):
                print("yeah "+sender.getTitle()+" in the mix")
                self.fontsToSend.append(sender.getTitle())
        else:
            if sender.getTitle() in (list(self.varDict.values())):
                print("yeah "+sender.getTitle()+" removed")
                self.fontsToSend.remove(sender.getTitle())
        print(self.fontsToSend)
    
    def makeColumns(self):
        for self.glyphs in self.f1:
            if self.glyphs:
                n = self.glyphs.name
                self.glyphlist.append(n)
            self.glyphlist.sort()
        for self.glyphs in self.glyphlist:
            if self.f1[self.glyphs].width == self.f2[self.glyphs].width and self.f1[self.glyphs].rightMargin == self.f2[self.glyphs].rightMargin and self.f1[self.glyphs].leftMargin == self.f2[self.glyphs].leftMargin:
                self.statusflag = "✔️"
            else:
                self.statusflag = "🔴"
            self.columnlist.append({"Glyph Name" : self.f1[self.glyphs].name, self.f1.info.styleName : str(self.f1[self.glyphs].width) + " – " + str(self.f1[self.glyphs].leftMargin) + " | " + str(self.f1[self.glyphs].rightMargin), self.f2.info.styleName : str(self.f2[self.glyphs].width) + " – " + str(self.f2[self.glyphs].leftMargin) + " | " + str(self.f2[self.glyphs].rightMargin), "Match" : self.statusflag})
        return self.columnlist
    
    def buttonCallback(self, sender):
        addObserver(self, 'updateFontInfo', 'fontDidSave')
        print('adding Observer')
        tempList=[]
        for names in self.fontsToSend:
            for f in AllFonts():
                if names == f.info.styleName:
                    print(f)
                    tempList.append(f)
        self.fontsToSend = tempList
        print(self.fontsToSend)
        self.f1 = self.fontsToSend[0]
        self.f2 = self.fontsToSend[1]
        if len(self.fontsToSend)==2:
            self.checkWindow.close()
            self.openList()
            
    def openList(self):
        self.listWindow.myList = List((0, 0, -0, -0), items = self.makeColumns(), columnDescriptions=[{"title": "Glyph Name"}, {"title": self.f1.info.styleName}, {"title": self.f2.info.styleName}, {"title": "Match"}], selectionCallback=self.selectionCallback)
        self.listWindow.open()
    
    def updateFontInfo(self, sender):
        print("wtf")
        self.openList()
        
                    
    def selectionCallback(self, sender):
        print(sender.getSelection())
        
    def windowClose(self, sender):
        removeObserver(self, 'fontDidSave')
        print('removing Observer')


FontsCheckBox()
 
# d = {}
# for i in range(len(AllFonts())):
#     d["string{0}".format(i)] = AllFonts()[i].info.styleName
# print(d)