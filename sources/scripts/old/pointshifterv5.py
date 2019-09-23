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
        self.moveXTRA = 0

        # create a floating window
        self.w = FloatingWindow((200, 74), "move %s" % self.glyph.name)

        # add a slider for moving in the x axis
        self.w.sliderXTRA = Slider(
                (10, 10, -10, 22),
                value=0, maxValue=200, minValue=0,
                callback=self.adjustXTRA)
                
        # self.w.sliderXOPQ = Slider(
        #         (10, 10, -10, 22),
        #         value=0, maxValue=200, minValue=-200,
        #         callback=self.adjust)
    
        # open the window
                
        self.w.open()

    def adjustXTRA(self, sender):
        
        # crossbartop='CROSSBARTOP'
        # crossbarbottom='CROSSBARBOTTOM'
        # rightsideinsidelabel='RIGHTSIDEINSIDE'
        # rightsideoutsidelabel='RIGHTSIDEOUTSIDE'
        # leftsideinsidelabel='LEFTSIDEINSIDE'
        # leftsideoutsidelabel='LEFTSIDEOUTSIDE'
        rightstemlabel='RIGHTSTEM'

        # get the current x and y values from the sliders
        valueXTRA = self.w.sliderXTRA.get()

        # calculate actual move distance
        x = self.moveXTRA - valueXTRA

        # move the glyph
        
        for self.c in self.glyph:
            for self.p in self.c.points:
                if rightstemlabel in self.p.labels:
                    self.glyph.prepareUndo()
                    self.p.move((-x,0))
                    self.glyph.rightMargin
                    self.glyph.changed()
                    self.glyph.performUndo()
        # self.glyph.moveBy((x, 0))

        # update saved values
        self.moveXTRA = valueXTRA

        # print the current move distance
        print(self.moveXTRA)


OpenWindow(MoveGlyphWindow, CurrentGlyph())

