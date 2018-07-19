from tkinter import *
import string
import random


def init(data):
    data.timer = 0
    data.numPt = len(data.ptList)
    data.boxX, data.boxY = data.width / 5, data.height / 5
    data.colors = ['red','blue','yellow','green','purple','orange','black','brown','cyan']
    data.margin = data.width / 10

def redrawAll(canvas, data):
    canvas.create_rectangle(data.margin, data.margin, data.width-data.margin, data.height-data.margin, outline = 'black')
    colorIndex = 0
    for num in range(data.numPt):
        for particle in range(num):
            colorIndex += 1
            drawParticle(colorIndex)
            
def drawParticle(colorIndex):
    pass





####################################
# use the run function as-is
####################################

def run(ptList, width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.ptList = ptList
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


ptList = [2,3]
run(ptList, 400, 400)