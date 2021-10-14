from tkinter import *
import tkinter.ttk as ttk
import produktion as p
import data as d

class UI():
    def __init__(self):
        self.root = Tk()
        self.robot = p.robot()
        self.data = d.robot_data()

        self.TBP = ''

        self.Buttonframe = Frame(self.root)
        self.Buttonframe.grid(column=0, row = 0)

        self.DBframe = Frame(self.root)
        self.DBframe.grid(column=1, row = 0)

        i = 0
        r_set = self.data.get_ordrer()
        for pallet in r_set:
            for j in range(len(pallet)):
                e = Entry(self.DBframe)
                e.grid(row = i, column = j)
                e.insert(END, pallet[j])
            i += 1

        self.title = Label(self.Buttonframe, text = "Robot-automation", font=("Arial Bold", 25))
        self.title.grid(column=0, row = 0)

        self.produceCBut = Button(self.Buttonframe, text = "Produce custom", command = self.produceC)
        self.produceCBut.grid(column = 0, row = 4)

        self.calibrateBut = Button(self.Buttonframe, text = "Calibrate", command = self.cali)
        self.calibrateBut.grid(column = 0, row = 5)

        self.posSubmit = Button(self.Buttonframe, text="Submit position", command = self.submit_pos)
        self.posSubmit.grid(column = 0, row=6)

        self.newOrderButton = Button(self.Buttonframe, text = "New order pallet", command = self.new).grid(column = 0, row = 7)

        self.producePBut = Button(self.Buttonframe, text="Produce pallet from DB", command = self.pFromDb)
        self.producePBut.grid(column = 0, row=8)

        self.producePEntry = Entry(self.Buttonframe)
        self.producePEntry.grid(column = 0, row=9)

        self.resetBut = Button(self.Buttonframe, text="REE", command = self.reset)
        self.resetBut.grid(column = 0, row=10)

        self.root.mainloop()
        #calibrateWindow = Tk(

    def reset(self):
        self.robot.placePop = 0
        self.robot.greenPop = 0
        self.robot.redPop = 0
        self.robot.bluePop = 0
        self.robot.yellowPop = 0

    def pFromDb(self):
        list = self.data.produce_palle(self.producePEntry.get())
        self.robot.produce_pallet(list)

    def cali(self):
        self.robot.calibrate(self.calibrateBut)
        #calibrateWindow.mainloop()

    def submit_pos(self):
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

    def new(self):
        self.palletW = Toplevel(self.root)
        self.palletW.title("Create pallet")
        self.palletW.geometry("680x150")

        self.entries = []
        self.pName = Entry(self.palletW)
        self.pName.grid(column = 0, row = 0)
        self.submitPallet = Button(self.palletW, text = 'Submit', command = self.submit).grid(column = 3, row = 5)

        self.b = Button(self.palletW, text = 'get', command = self.data.get_ordrer)
        Button(self.palletW, text = 'get', command = self.data.get_ordrer).grid(column = 2, row = 5)
        n = 0

        for y in range(4):
            for x in range(4):
                n += 1
                field = Entry(self.palletW)
                field.grid(column = x, row = y+1)
                self.entries.append(field)

        #print(self.entries)

    def submit(self):
        self.data.new_order(self.entries, self.pName.get())

        i = 0
        r_set = self.data.get_ordrer()
        for pallet in r_set:
            for j in range(len(pallet)):
                e = Entry(self.DBframe)
                e.grid(row = i, column = j)
                e.insert(END, pallet[j])
            i += 1
def main():
    ui = UI()

if __name__ == "__main__":
    main()
