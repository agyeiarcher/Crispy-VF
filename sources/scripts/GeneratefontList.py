from vanilla import *

class ListDemo(object):

    def __init__(self):
        self.w = Window((100, 100))
        self.w.myList = List((0, 0, -0, -0),
                     [{"One": "A", "Two": "a"}, {"One": "B", "Two": "b"}],
                     columnDescriptions=[{"title": "One"}, {"title": "Two"}],
                     selectionCallback=self.selectionCallback)
        self.w.open()

    def selectionCallback(self, sender):
        print(sender.getSelection())

ListDemo()