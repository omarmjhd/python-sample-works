
from Myro import *
init()

def avoidWalls():
    for x in timer(60):
        if getIR() == [0,0]:
            turnLeft(1,1.5)
        if getIR() == [0,1]:
            turnLeft(1,1.5)
        if getIR() == [1,0]:
            turnLeft(1,1.5)
        else:
            translate(-1)
    for x in range(5):
        turnLeft(1,.25)
        beep(.25,800)
        turnRight(1,.25)
        beep(.25,400)