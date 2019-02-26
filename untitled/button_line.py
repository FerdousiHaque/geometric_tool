import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

canvas = tk.Canvas(root, bg='white', height=300, width=300)
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

def direct_line():

    canvas.bind("<Button-1>", click)
    canvas.bind("<B1-Motion>", drag1)

def dda_line():

    canvas.bind("<ButtonPress-1>", click)
    canvas.bind("<B1-Motion>", drag2)

def bresen():
    canvas.bind("<ButtonPress-1>", click)
    canvas.bind("<B1-Motion>", drag3)
def drag1(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates
    #canvas.co,ords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])
    direct()

def direct():
    canvas.delete("all")
    #canvas.create_line(store['x'],store['y'],store['x2'],store['y2'])

    x1 = coords['x']
    x2 = coords['x2']

    y1 = coords['y']
    y2 = coords['y2']

    m = (y2 - y1) / (x2 - x1)
    c = y2 - m * x2

    xVector = []
    yVector = []


    i = 1

    if abs(m) <= 1:

        for xi in range(x1, x2):

            yi = m * xi + c
            rounded_y = int(yi + 0.5)

            xVector.append(xi)
            yVector.append(rounded_y)
    print(xVector)
    print(len(xVector))
    print('\n')
    print(yVector)
    print(len(yVector))

    print(m)

    for i in range(0, len(xVector)-1):

        #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="blue")


        if (i % 2 == 0):
            canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="red")
            #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="red")
        else:
            canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="blue")
            #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="red")

    else:


        for yi in range(y1, y2):
            xi = (yi - c)/m

            rounded_xi = int(xi + 0.5)

            xVector.append(rounded_xi)
            yVector.append(yi)
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
def drag2(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates
    #canvas.coords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])
    dda()

def dda():
    canvas.delete("all")
    #canvas.create_line(store['x'],store['y'],store['x2'],store['y2'])

    x1 = coords['x']
    x2 = coords['x2']

    y1 = coords['y']
    y2 = coords['y2']

    dx = x2 - x1
    dy = y2 - y1

    m = dy / dx

    xVector = [x1]
    yVector = [y1]


    if abs(m) <= 1:

        while x1 < x2:

            x1 += 1
            y1 = y1 + m
            rounded_y = int(y1 + 0.5)

            xVector.append(x1)
            yVector.append(rounded_y)
    print(xVector)
    print(len(xVector))
    print('\n')
    print(yVector)
    print(len(yVector))

    print(m)

    for i in range(0, len(xVector)-1):

        #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="blue")


        if (i % 2 == 0):
            canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="red")
            #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="red")
        else:
            canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="blue")
            #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="red")

    else:
        while y1 < y2:
            x1 = x1 +1 / m
            y1 += 1
            rounded_x = int(x1 + 0.5)
            xVector.append(rounded_x)
            yVector.append(y1)
    print(yVector)
    print(len(yVector))
    print('\n')
    print(xVector)
    print(len(xVector))

    print(m)

    for i in range(0, len(xVector)-1):

        #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="blue")


        if (i % 2 == 0):
            canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="red")
            #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="red")
        else:
            canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="blue")
            #canvas.create_oval(xVector[i], yVector[i], xVector[i], yVector[i], width=1, fill="red")

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
button1 = tk.Button(root,
                   text="Direct Line",
                   fg="blue",
                   command=direct_line)
button1.pack()
button2 = tk.Button(root,
                   text="DDA Line",
                   fg="green",
                   command=dda_line)
button2.pack()
button3 = tk.Button(root,
                   text="Bresenham",
                   fg="orange",
                   command=bresen)
button3.pack()
button4 = tk.Button(root,
                   text="Circle",
                   fg="black",
                   command=quit)
button4.pack()
button = tk.Button(root,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack()


root.mainloop()
