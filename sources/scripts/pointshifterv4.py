from vanilla import FloatingWindow, Slider
from mojo.UI import Message

class MoveGlyphWindow:

    '''Move the current glyph using sliders.'''

    def __init__(self, glyph):

        # if glyph is None, show a message
        if glyph is None:
            Message('no glyph selected', title='moveTool', informativeText='Please select one glyph first!')
            return

        # store the glyph and initial move values as object attributes
        self.glyph = glyph
        self.moveX = 0

        # create a floating window
        self.w = FloatingWindow((200, 74), "move %s" % self.glyph.name)

        # add a slider for moving in the x axis
        self.w.sliderX = Slider(
                (10, 10, -10, 22),
                value=0, maxValue=200, minValue=-200,
                callback=self.adjust)

        # open the window
        self.w.open()

    def adjust(self, sender):

        # get the current x and y values from the sliders
        valueX = self.w.sliderX.get()

        # calculate actual move distance
        x = self.moveX - valueX

        # move the glyph
        self.glyph.moveBy((x, y))

        # update saved values
        self.moveX = valueX

        # print the current move distance
        print(self.moveX)


OpenWindow(MoveGlyphWindow, CurrentGlyph())
print(CurrentGlyph())

