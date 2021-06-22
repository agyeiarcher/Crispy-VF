from vanilla import *

class CheckBoxDemo(object):

    def __init__(self):
        self.w = Window((100, 200))
        self.d = {}
        self.l=[]
        for self.i in range(len(AllFonts())):
            self.d["string{0}".format(self.i)] = "CheckBox((10, 10*i, -10, 20), ""AllFonts()[i].info.styleName"", callback=self.checkBoxCallback, value=True)"
        print(self.d)
        self.w.stringt = CheckBox((0, 0, 100, 100), self.stringt, callback=self.checkBoxCallback, value=True)
        self.w.open()

    def checkBoxCallback(self, sender):
        print ("check box state change!", sender.get())

CheckBoxDemo()

# def 
# d = {}
# for i in range(len(AllFonts())):
#     d["string{0}".format(i)] = AllFonts()[i].info.styleName
# print(d)