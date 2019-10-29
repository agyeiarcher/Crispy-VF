from drawBot import *
from drawBot.ui.drawView import DrawView
from vanilla import Window, Slider
from fontTools.ttLib import TTFont

f= CurrentFont()
p=TTFont(f.path)
g=p.getGlyphSet()

def drawGlyph(g):
    bez = BezierPath()
    g.draw(bez)
    drawPath(bez)

class DrawBotViewer(object):

    def __init__(self):
        # create a window
        self.w = Window((400, 400), minSize=(200, 200))
        # add a slider
        self.w.slider = Slider((10, 10, -10, 22), callback=self.sliderCallback)
        # add a drawBox view
        self.w.drawBotCanvas = DrawView((0, 40, -0, -0))
        # draw something
        self.drawIt()
        # open the window
        self.w.open()

    def sliderCallback(self, sender):
        # slider chagned so redraw it
        self.drawIt()

    def drawIt(self):
        # get the value from the slider
        value = self.w.slider.get()
        print(value)
        # initiate a new drawing
        newDrawing()
        # add a page
        newPage(300, 300)
        # set a fill color
        fill(1, value/100., 0)
        # draw a rectangle
        rect(10, 10, 100, 100)
        # set a font size
        # font(TTFont(f.path))
        fontSize(48 + value)
        # draw some text
        # text("H", (10, 120))
        scale(0.002)
        g = font[f["A"]]
        drawGlyph(g)
        # get the pdf document
        pdfData = pdfImage()
        # set the pdf document into the canvas
        self.w.drawBotCanvas.setPDFDocument(pdfData)

DrawBotViewer()
# print(f.path)

