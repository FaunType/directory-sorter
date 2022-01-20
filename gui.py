from tkinter import *

class CreateGui():

    def __init__(self):
        self.window = Tk()
        self.top_frame = Frame(self.window)
        self.bottom_frame = Frame(self.window)

    def createWidgets(self):
        self.default = Button(self.top_frame, text = 'I\'ve gotta set this up...', command = self.window.destroy)
        self.default.pack(side='top')
        self.top_frame.pack()
        self.bottom_frame.pack()
        mainloop()
