from vanilla import FloatingWindow, Slider
from mojo.UI import Message

f= CurrentFont()
g=CurrentGlyph()

def BuildLabelsList(theFont):
    Plabels=[]    
    for glyph in theFont:
        for contour in glyph:
                for point in contour.points:
                    b=point.labels
                Plabels=Plabels+b
                Plabels=list(dict.fromkeys(Plabels)) #remove duplicates
    print(Plabels)
    return Plabels

class MoveGlyphWindow:

    '''Move the current glyph using sliders.'''

    def __init__(self, glyph):

        # if glyph is None, show a message
        # store the glyph and initial move values as object attributes
                
        for labelslider in BuildLabelsList(f):
            # create a floating window
            self.w = FloatingWindow((200, 74), "move "+str(labelslider))

            # add a slider for moving in the x axis
            self.g = glyph
            self.moveX = 0
            self.label= labelslider
            self.w.labelslider = Slider(
                    (10, 10, -10, 22),
                    value=0, maxValue=100, minValue=-100,
                    callback=self.adjust)

            # open the window
            self.w.open()

    def adjust(self, sender):

        # get the current x and y values from the sliders
        valueX = self.w.labelslider.get()

        # calculate actual move distance
        x = self.moveX - valueX

        # move the glyph
        self.g.moveBy((x, 0))

        # update saved values
        self.moveX = valueX

        # print the current move distance
        print(self.moveX)

BuildLabelsList(f)
OpenWindow(MoveGlyphWindow, CurrentGlyph())






                    