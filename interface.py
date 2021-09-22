from tkinter import *
import tkinter.ttk as ttk
import produktion as p

class UI():
    def __init__(self):
        self.root = Tk()
        self.robot = p.robot()

        self.TBP = ''

        self.Buttonframe = Frame(self.root)
        self.Buttonframe.grid(column=0, row = 0)

        self.DBframe = Frame(self.root)
        self.DBframe.grid(column=0, row = 0)

        self.title = Label(self.Buttonframe, text = "Robot-automation", font=("Arial Bold", 25))
        self.title.grid(column=0, row = 0)

        self.produceCBut = Button(self.Buttonframe, text = "Produce custom", command = self.produceC)
        self.produceCBut.grid(column = 0, row = 4)

        self.calibrateBut = Button(self.Buttonframe, text = "Calibrate", command = self.cali)
        self.calibrateBut.grid(column = 0, row = 5)

        self.posSubmit = Button(self.Buttonframe, text="Submit position", command = self.submit)
        self.posSubmit.grid(column = 0, row=6)

        self.root.mainloop()
        #calibrateWindow = Tk()

    def cali(self):
        self.robot.calibrate(self.calibrateBut)
        #calibrateWindow.mainloop()

    def submit(self):
        self.robot.cvar.set(1)

    def produceC(self):
        self.customWindow = Toplevel(self.root)
        self.customWindow.title("Produce custom order")
        self.customWindow.geometry("520x420")

        #wl = Label(self.customWindow, text = "Hello world").grid()
        bG = Button(self.customWindow, text = "Green", bg="green", command = self.colorG,
         height = 9, width = 20).grid(column = 0, row = 0)
        bB = Button(self.customWindow, text = "Blue", bg="blue", command = self.colorB,
         height = 9, width = 20).grid(column = 1, row = 0)
        bR = Button(self.customWindow, text = "Red", bg="red", command = self.colorR,
         height = 9, width = 20).grid(column = 0, row = 1)
        bY = Button(self.customWindow, text = "Yellow", bg="yellow", command = self.colorY,
         height = 9, width = 20).grid(column = 1, row = 1)

        produce = Button(self.customWindow, text = "Produce", command = self.pro,
         height = 9, width = 20).grid(column = 2, row = 1)

    def colorG(self):
        if len(self.TBP) != 4:
            self.TBP += "g"
            print(self.TBP)
        if self.TBP == 4:
            self.pro()
    def colorB(self):
        if len(self.TBP) != 4:
            self.TBP += "b"
            print(self.TBP)
        if self.TBP == 4:
            self.pro()
    def colorR(self):
        if len(self.TBP) != 4:
            self.TBP += "r"
            print(self.TBP)
        if self.TBP == 4:
            self.pro()
    def colorY(self):
        if len(self.TBP) != 4:
            self.TBP += "y"
            print(self.TBP)
        if self.TBP == 4:
            self.pro()

    def pro(self):
        self.robot.produce(self.TBP)
        self.TBP = ''

ui = UI()
