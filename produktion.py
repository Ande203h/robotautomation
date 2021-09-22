from serial.tools import list_ports

import pydobot
import pyautogui

import tkinter as tk

import random

class robot(object):
    def __init__(self):
        self.available_ports = list_ports.comports()
        self.port = self.available_ports[0].device

        self.device = pydobot.Dobot(port=self.port, verbose=False)

        self.sqx = 20.1
        self.sqy = 20.1
        self.sqz = 10
        self.down = 9.5
        self.midx = -0.1
        self.midy = 0.65
        self.row = 0
        self.column = 0
        self.placePop = 0
        self.greenPop = 0
        self.redPop = 0
        self.bluePop = 0
        self.yellowPop = 0

        self.cvar = 0

        self.reset()

    def reset(self):
        self.device.move_to(300, 0, 120, 90, wait=True)

    def move(self, dx, dy, dz, wait = True):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to(x + dx * self.sqx, y + dy * self.sqy, dz, r, wait = wait)

    def get(self, colour):
        if colour == 'g':
            self.move(-2+self.midx,-4+self.midy+self.greenPop,self.down)
            self.greenPop -= 1

        elif colour == 'r':
            self.move(-1+self.midx,-4+self.midy+self.redPop,self.down)
            self.redPop -= 1

        elif colour == 'b':
            self.move(0+self.midx,-4+self.midy+self.bluePop,self.down)
            self.bluePop -= 1

        elif colour == 'y':
            self.move(1+self.midx,-4+self.midy+self.yellowPop,self.down)
            self.yellowPop -= 1

        self.move(0, 0, -39, 90)
        self.device.suck(True)

    def place(self, string):
        if self.placePop >= len(string):
            self.row += 1
            self.placePop = 0
        if self.row >= 4:
            self.row = 0
            self.column += 1
        self.move(1+self.midx-self.column, 6+self.midy-self.row, self.down)
        #move(-2+mid, 6+mid-placePop, down)
        self.move(0, 0, -39+self.placePop*self.sqz)
        self.device.suck(False)
        self.placePop += 1

    def calibrate(self, button):
        self.cvar = tk.IntVar()
        self.reset()
        self.move(-2+self.midx,-4+self.midy, self.down-39)
        button.wait_variable(self.cvar)
        self.reset()
        self.move(1+self.midx,-7+self.midy,self.down-39)
        button.wait_variable(self.cvar)
        self.reset()
        self.move(1+self.midx, 6+self.midy, self.down-39)
        button.wait_variable(self.cvar)
        self.reset()
        self.move(1+self.midx-3, 6+self.midy-3, self.down-39)
        button.wait_variable(self.cvar)
        self.reset()

    def produce(self, string):
        self.reset()
        for i in string:
            print(i)
            self.get(i)
            self.reset()
            self.place(string)
            self.reset()

#calibrate()
"""
while True:
    check = True
    self.reset()
    inp = random.choice(['g', 'b', 'r', 'y'])
    while check:
        if inp == 'g' and greenPop == 4:
            inp = random.choice(['b', 'r', 'y'])
        elif inp == 'b' and bluePop == 4:
            inp = random.choice(['g', 'r', 'y'])
        elif inp == 'r' and redPop == 4:
            inp = random.choice(['b','g','y'])
        elif inp == 'y' and yellowPop == 4:
            inp = random.choice(['b','g','y'])
        else:
            check = False
    print(inp)
    get(inp)
    self.reset()
    place()
    self.reset()
"""

#self.device.close()
