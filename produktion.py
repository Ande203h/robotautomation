from serial.tools import list_ports

import pydobot

import random

#print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
#print(f'available ports: {[x.device for x in available_ports]}')

available_ports = list_ports.comports()
port = available_ports[0].device

device = pydobot.Dobot(port=port, verbose=False)

sqx = 20
sqy = 20
sqz = 10
down = 10
mid = 0.5

def reset():
    device.move_to(300, 0, 120, 90, wait=True)

def move(dx, dy, dz, wait = True):
    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    device.move_to(x+dx*sqx, y+dy*sqy, dz, r, wait = wait)

def get(colour):
    global greenPop, redPop, bluePop, yellowPop
    if colour == 'green':
        move(-2+mid,-4+mid+greenPop,down)
        greenPop -= 1

    elif colour == 'red':
        move(-1+mid,-4+mid+redPop,down)
        redPop -= 1

    elif colour == 'blue':
        move(0+mid,-4+mid+bluePop,down)
        bluePop -= 1

    else:
        move(1+mid,-4+mid+yellowPop,down)
        yellowPop -= 1

    move(0, 0, -39, 90)
    device.suck(True)

def place():
    global placePop
    move(-2+mid, 6+mid, down)
    #move(-2+mid, 6+mid-placePop, down)
    move(0, 0, -39+placePop*sqz)
    device.suck(False)
    placePop += 1

placePop = 0
greenPop = 0
redPop = 0
bluePop = 0
yellowPop = 0

while True:
    reset()
    inp = random.choice(['green', 'blue', 'red', 'h'])
    print(inp)
    get(inp)
    reset()
    place()
    reset()

device.close()
