from serial.tools import list_ports

import pydobot

#print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
#print(f'available ports: {[x.device for x in available_ports]}')

available_ports = list_ports.comports()
port = available_ports[0].device

device = pydobot.Dobot(port=port, verbose=False)

sqW = 20

def move(dx, dy, dz, r=0, waitArg=True):
    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    device.move_to(x+dx, y+dy, z+dz, r, wait=waitArg)
def reset():
    device.move_to(300, 0, 200, 0, wait=True)

def get(x, y, suck=True):
    reset()
    move(x*sqW-2, y*sqW+3, -195)
    move(0, 0, -10)
    device.suck(suck)
    move(0, 0, 10)
    reset()

greenPop, redPop, yellowPop, bluePop = (4, 4, 4, 4)
inp = ''

pallet = [
[1, 1, 1, 1],
[2, 2, 2, 2],
[3, 3, 3, 3],
[4, 4, 4, 4]
]

placePallet = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]
]

while inp != 'q':
    inp = input("Colour: ")
    reset()
    if inp == 'green':
        x = -1
        y = -8 + greenPop
        greenPop -= 1

    elif inp == 'red':
        x = 0
        y = -8 + redPop
        redPop -= 1

    elif inp == 'blue':
        x = 1
        y = -8 + greenPop
        greenPop -= 1

    elif inp == 'yellow':
        x = 2
        y = -8 + greenPop
        greenPop -= 1

    get(x, y, True)
    device.suck(False)



device.close()
