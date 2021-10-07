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
        self.sqz = 9.9
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
        self.device.move_to_J(300, 0, 120, 90, wait=True)

    def move(self, dx, dy, dz, wait = True):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to_J(x + dx * self.sqx, y + dy * self.sqy, dz, r, wait = wait)

    def move_L(self, dx, dy, dz, wait = True):
        (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
        self.device.move_to_L(x + dx * self.sqx, y + dy * self.sqy, dz, r, wait = wait)

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
        else:
            print("ERROR: NO COLOR NAMED " + colour)

        self.move_L(0, 0, -40, 90)
        self.device.suck(True)
        self.move_L(0, 0, 10, 90)

    def place(self):
        #function for placing cubes
        #adds one to column, and resets row if row is 4
        if self.row == 4:
            self.row = 0
            self.column += 1
        #prepares to make pallet if pallet is filled
        if self.column == 4:
            self.column = 0
            self.row = 0
        #moves to top of where the cube should be placed
        self.move(1+self.midx-self.column, 6+self.midy-self.row, self.down)
        #moves down and places
        self.move_L(0, 0, -39+self.placePop*self.sqz)
        self.device.suck(False)
        #moves up
        self.move_L(0, 0, 30)
        #adds one to the amount of placed cubes
        self.placePop += 1

    def calibrate(self, button):
        #function for calibrating
        self.cvar = tk.IntVar()
        #resets and moves to the get-pallets right upper corner
        self.reset()
        self.move(-2+self.midx,-4+self.midy, self.down-39)
        button.wait_variable(self.cvar)
        #resets and moves to the get-pallets left lower corner
        self.reset()
        self.move(1+self.midx,-7+self.midy,self.down-39)
        button.wait_variable(self.cvar)
        #resets and moves to the place-pallets right lower corner
        self.reset()
        self.move(1+self.midx, 6+self.midy, self.down-39)
        button.wait_variable(self.cvar)
        self.reset()
        self.move(1+self.midx-3, 6+self.midy-3, self.down-39)
        button.wait_variable(self.cvar)
        self.reset()

    def produce(self, tuplet):
        self.reset()
        print(tuplet)
        for i in tuplet:
            print("getting " + i)
            self.get(i)
            print("resetting")
            self.reset()
            print("placing")
            self.place()
            print("resetting")
            self.reset()
        print(self.row, self.column)
        self.row += 1
        self.placePop = 0

    def produce_pallet(self, list):
        print("list:")
        print(list)
        for tuplet in list:
            print("tuplet:")
            print(tuplet)
            for string in tuplet:
                self.produce(string)
