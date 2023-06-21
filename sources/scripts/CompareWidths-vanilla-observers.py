# menuTitle : my funky script
# shortCut  : command+q
# command+shift+control+alt+<input>
# character space tab backtab arrowup arrowdown arrowleft arrowright f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 f13 f14 f15 f16 f17 f18 f19 f20 f21 f22 f23 f24 f25 f26 f27 f28 f29 f30 f31 f32 f33 f34 f35 enter backspace delete home end pageup pagedown


from vanilla import *
from mojo.events import addObserver, removeObserver
from AppKit import NSApp

debug = True


class observerTest(object):

    def __init__(self):
        windowname = 'debug only test'
        if debug is True:
            self.w = Window((500, 50), windowname)
            self.w.bind('close', self.windowClose)
            for window in [w for w in NSApp().orderedWindows() if w.isVisible()]:
                if window.title() == windowname:
                    window.close()
            self.w.open()
        self.doStuff()

    def windowClose(self, sender):
        removeObserver(self, 'keyDown')
        print('removing Observer')

    def doStuff(self):
        addObserver(self, 'keyWasPressedMethod', 'keyDown')
        print('adding Observer')

    def keyWasPressedMethod(self, info):
        print('keyWasPressed')
        event = info['event']
        print(event)
        characters = event.characters()
        print(characters)

observerTest()