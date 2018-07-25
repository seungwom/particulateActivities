from tkinter import *
import string
import random




def init(data):
    data.numPt = len(data.ptList)
    data.colors = ['red','blue','yellow','green','purple','orange','black','brown','cyan']
    data.colorIndex = 0
    data.margin = data.width / 10
    data.ptSize = data.width // 20
    data.imageList = []
    
def getParticles(data):
    ptDict = dict()
    for num in range(data.numPt):
        for particle in range(data.ptList[num]):
            pass
        data.colorIndex += 1
            
    
    
    
    
def mousePressed(event, data):
    pass


def keyPressed(event, data):
    if event.keysym == 'space':
        print('hi')



def redrawAll(canvas, data):    
    canvas.create_rectangle(data.margin, data.margin, data.width-data.margin, data.height-data.margin)
    colorIndex = 0
    for num in range(data.numPt):
        for particle in range(data.ptList[num]):
            drawParticle(data,canvas)
        data.colorIndex += 1
            
            



def drawParticle(data,canvas):
    x = random.randint(data.margin+data.ptSize, data.width-data.margin-data.ptSize)
    y = random.randint(data.margin+data.ptSize, data.height-data.margin-data.ptSize)
    canvas.create_oval(x-data.ptSize,y-data.ptSize,x+data.ptSize,y+data.ptSize, fill = data.colors[data.colorIndex])





###################################
# #use the run function as-is
###################################

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

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.ptList = ptList
    data.width = width
    data.height = height
    print(data.width, data.height)
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
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

ptList = [2,3]
run(ptList, 400, 400)