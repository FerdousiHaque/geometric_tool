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




canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag2)

root.mainloop()
