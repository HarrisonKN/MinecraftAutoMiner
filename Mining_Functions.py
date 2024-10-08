from movements import *

def mineClockwise(X,Y,Z):
    mineDown()
    mineForward()


def mineDown():
    lookDown()
    mine()
    time.sleep(0.2)
    mineRelease()

def mineForward():
    stepForward()
    mine()

def testMineForward(X):
    mineDown()
    lookUp()
    time.sleep(1)

    for i in range(X):
        print(i+1)
        mineForward()
        time.sleep(0.2)

    keysRelease()

def testMineChunk(X,Y):
    print("IN TEST MINE CHUNK")
    mineDown()
    lookUp()

    #mine chunk going left to right, so clockwise
    for i in range(int(Y/2)): 
        print("Y Value: ",i+1)
        mineChunkLine(X)
        clockWiseReset()
        mineChunkLine(X)
        antiClockWiseReset()


def mineChunkLine(X):
    for i in range(X):
        print("X Value: ", i+1)
        mineForward()
        time.sleep(0.2)
    keysRelease()

def clockWiseReset():
    lookRight()
    mine()
    time.sleep(0.2)
    mineRelease()
    stepForward()
    lookRight()

def antiClockWiseReset():
    lookLeft()
    mine()
    time.sleep(0.2)
    mineRelease()
    stepForward()
    lookLeft()


