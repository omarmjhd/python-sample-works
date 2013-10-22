

from Myro import*
init()

def roboScript(text,):

    commands = open(text, "r")
    commandsList = commands.readlines()

    for i in commandsList:
        itemList = i.split()
        if "fw" in i:
            forward(float(itemList[1]), float(itemList[2]))
        if "bw" in i:
            backward(float(itemList[1]), float(itemList[2]))
        if "tl" in i:
            turnLeft(float(itemList[1]), float(itemList[2]))
        if "tr" in i:
            turnRight(float(itemList[1]), float(itemList[2]))
        if "bp" in i:
            beep(float(itemList[2]), float(itemList[1]))