import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

coords = {"x":0,"y":0,"x2":0,"y2":0}
# keep a reference to all lines by keeping them in a list
lines = []

def click(e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y

    # create a line on this point and store it in the list
    lines.append(canvas.create_line(coords["x"],coords["y"],coords["x"],coords["y"]))

def drag3(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates
    #canvas.coords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])
    br()

def br():
    canvas.delete("all")
    #canvas.create_line(store['x'],store['y'],store['x2'],store['y2'])

    x1 = coords['x']
    x2 = coords['x2']

    y1 = coords['y']
    y2 = coords['y2']

    x=x1
    y=y1

    dx = x2 - x1
    dy = y2 - y1
    dT = 2 * (dy - dx)
    dS = 2 * dy
    d = dS - dx

    xVector = []
    yVector = []


    while x < x2:

        x += 1
        if d<0:
            d=d+dS

        else:
            y += 1
            d = d+dT


        xVector.append(x)
        yVector.append(y)
    print(xVector)
    print(len(xVector))
    print('\n')
    print(yVector)
    print(len(yVector))

    for i in range(0, len(xVector)-1):

        #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="blue")


        if (i % 2 == 0):
            canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="red")
            #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="red")
        else:
            canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="blue")
            #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="red")



canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag3)

root.mainloop()
