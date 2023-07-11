from vanilla import *
from mojo.events import addObserver, removeObserver
from AppKit import NSApp, NSPanel

af = AllFonts()
f = CurrentFont()

debug = True

class ListDemo(object):
    
    def __init__(self):
        windowname = 'debug only test'
        if debug is True:
            self.glyphlist = []
            self.columnlist=[]
            self.f1 = AllFonts()[0]
            self.f2 = AllFonts()[1]
            self.w = FloatingWindow((600, 400), windowname)
            self.w.bind('close', self.windowClose)
            for window in [w for w in NSApp().windows() if w.isVisible()]:
                if window.title() == windowname:
                    window.close()          
            self.w.open()
            self.doStuff()
    
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
            
    def selectionCallback(self, sender):
        print(sender.getSelection())
    
    def windowClose(self, sender):
        removeObserver(self, 'fontDidSave')
        print('removing Observer')
        
    def updateFontInfo(self, sender):
        ListDemo()
                   
    def doStuff(self):
        addObserver(self, 'updateFontInfo', 'fontDidSave')
        print('adding Observer')
        self.w.myList = List((0, 0, -0, -0), self.makeColumns(), columnDescriptions=[{"title": "Glyph Name"}, {"title": self.f1.info.styleName}, {"title": self.f2.info.styleName}, {"title": "Match"}], selectionCallback=self.selectionCallback)


ListDemo()