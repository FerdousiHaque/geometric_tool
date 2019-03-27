import tkinter as tk

root = tk.Tk()
root.geometry("500x520")
canvas = tk.Canvas(root, bg="white", width=400, height=400)
canvas.pack()

previous_x = previous_y = 0
x = y = 0
coords = {"x":0,"y":0,"x2":0,"y2":0}
move = False
lengthX = 0
Xpoints_array = []
Ypoints_array = []

# Defining region codes
INSIDE = 0 #0000
LEFT = 1 #0001
RIGHT = 2 #0010
BOTTOM = 4 #0100
TOP = 8	 #10000

def print_points():
        canvas.bind("<ButtonPress-1>", tell_me_where_you_are)

def clipping():
        print("HERE")
        print(Xpoints_array,Ypoints_array)
        #canvas.bind("<ButtonPress-1>", mainClip)
        canvas.delete("all")
        lengthX=len(Xpoints_array)
        for i in range(0,lengthX-1):
            clip(Xpoints_array[i],Ypoints_array[i],Xpoints_array[i+1],Ypoints_array[i+1])
        clip(Xpoints_array[lengthX-1],Ypoints_array[lengthX-1],Xpoints_array[0],Ypoints_array[0])
        #canvas.delete("all")
        canvas.create_rectangle(x_min,y_min,x_max,y_max)
        print("There")
        print(Xpoints_array,Ypoints_array)


def tell_me_where_you_are(event):
        print("Here I am")
        canvas.create_oval(event.x, event.y, event.x, event.y, fill = "red", width = "4")
        previous_x = event.x
        previous_y = event.y

        Xpoints_array.append(event.x)
        Ypoints_array.append(event.y)

        print(Xpoints_array)
        print(Ypoints_array)
def points():
        canvas.bind("<ButtonPress-1>", lines)

def lines():
        lengthX=len(Xpoints_array)

        for i in range(0,lengthX-1):
            canvas.create_line(Xpoints_array[i],Ypoints_array[i],Xpoints_array[i+1],
                                    Ypoints_array[i+1])
        canvas.create_line(Xpoints_array[lengthX-1],Ypoints_array[lengthX-1],
                               Xpoints_array[0],Ypoints_array[0])

# Function to compute region code for a point(x,y)
def computeCode(x, y):
	code = INSIDE
	if x < x_min:	 # to the left of rectangle
		code |= LEFT
	elif x > x_max: # to the right of rectangle
		code |= RIGHT
	if y < y_min:	 # below the rectangle
		code |= BOTTOM
	elif y > y_max: # above the rectangle
		code |= TOP

	return code
def rect():
    canvas.bind( "<Button-1>", startRect )
    canvas.bind( "<ButtonRelease-1>", stopRect )
    canvas.bind( "<B1-Motion>", movingRect )

def startRect(event):
    move = True
    coords["x"] = event.x
    coords["y"] = event.y
    global x_min
    global y_min
    x_min = coords["x"]
    y_min= coords["y"]

    #Create rectangle
    canvas.create_rectangle(coords["x"], coords["y"], coords["x"], coords["y"])

def stopRect(event):
    move = False
    coords["x2"] = event.x
    coords["y2"] = event.y
    global x_max
    global y_max
    x_max = coords["x2"]
    y_max= coords["y2"]

    canvas.create_rectangle(coords["x"], coords["y"], coords["x2"], coords["y2"])

def movingRect(event):
    if move:
        coords["x2"] = event.x
        coords["y2"] = event.y
        canvas.create_rectangle(coords["x"], coords["y"],coords["x2"], coords["y2"])

def clip(x1,y1,x2,y2):
    print("ClipClip")
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:

		# If both endpoints lie within rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # If both endpoints are outside rectangle
        elif (code1 & code2) != 0:
            break

        # Some segment lies within the rectangle
        else:

			# Line Needs clipping
			# At least one of the points is outside,
			# select it
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point
			# using formulas y = y1 + slope * (x - x1),
			# x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:

				# point is above the clip rectangle
                x = x1 + (x2 - x1) * \
                    (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:

				# point is below the clip rectangle
                x = x1 + (x2 - x1) * \
								(y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:

                # point is to the right of the clip rectangle
                y = y1 + (y2 - y1) * \
								(x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:

				# point is to the left of the clip rectangle
                y = y1 + (y2 - y1) * \
								(x_min - x1) / (x2 - x1)
                x = x_min

			# Now intersection point x,y is found
			# We replace point outside clipping rectangle
            # by intersection point
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1,y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)
    x1 = int(x1 + 0.5)
    x2 = int(x2 + 0.5)
    y1 = int(y1 + 0.5)
    y2 = int(y2 + 0.5)
    if accept:
        #canvas.delete("all")
        canvas.create_line(x1,y1,x2,y2)
    else:
        print("No points added")


button1 = tk.Button(root,
                   text="Press for Point",
                   fg="blue",
                   command=print_points)
button1.pack()
button2 = tk.Button(root,
                   text="Draw Polygon",
                   fg="green",
                   command=lines)
button2.pack()
button3 = tk.Button(root,
                   text="Select Window",
                   fg="red",
                   command=rect)
button3.pack()
button4 = tk.Button(root,
                   text="Clipping",
                   command=clipping)
button4.pack()


root.mainloop()
