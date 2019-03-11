import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.rectx0 = 0
        self.recty0 = 0
        self.rectx1 = 0
        self.recty1 = 0
        self.move = False
        self.lengthX = 0
        self.clipper_size = 4
        self.i=self.x1=self.x2=self.y1=self.y1=self.i_pos=0
        self.k=self.ix=self.iy=self.kx=self.ky=self.k_pos=0
        self.Xpoints_array = []
        self.Ypoints_array = []
        self.newXpoints_array = []
        self.newYpoints_array = []
        self.poly_size=self.num=self.den = 0
        self.x3=self.x3=self.y4=self.y4 = 0

        self.canvas = tk.Canvas(self, width=400, height=400, bg = "white")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.button2 = tk.Button(self.parent, text = "Points", command = self.print_points)
        self.button2.pack(side="top", fill="both", expand=True)
        self.button = tk.Button(self.parent, text = "Polygon", command = self.lines)
        self.button.pack(side="top", fill="both", expand=True)
        self.button1 = tk.Button(self.parent, text = "Window", command = self._createCanvasBinding)
        self.button1.pack(side="top", fill="both", expand=True)
        self.button3 = tk.Button(self.parent, text = "Clipping", command = self.cliping)
        self.button3.pack(side="top", fill="both", expand=True)

    def print_points(self):
        self.canvas.bind("<ButtonPress-1>", self.tell_me_where_you_are)

    def clipping(self):
        self.canvas.bind("<ButtonPress-1>", self.mainClip)


    def tell_me_where_you_are(self, event):

        self.canvas.create_oval(event.x, event.y, event.x, event.y, fill = "red", width = "4")
        self.previous_x = event.x
        self.previous_y = event.y

        self.Xpoints_array.append(event.x)
        self.Ypoints_array.append(event.y)

        print(self.Xpoints_array)
        print(self.Ypoints_array)
    def points(self):
        self.canvas.bind("<ButtonPress-1>", self.lines)

    def lines(self):
        self.lengthX=len(self.Xpoints_array)

        for i in range(0,self.lengthX-1):
            self.canvas.create_line(self.Xpoints_array[i],self.Ypoints_array[i],self.Xpoints_array[i+1],self.Ypoints_array[i+1])


    def _createCanvasBinding(self):
        self.canvas.bind( "<Button-1>", self.startRect )
        self.canvas.bind( "<ButtonRelease-1>", self.stopRect )

    def startRect(self, event):
        #self.canvas.delete("all")
        self.move = True
        #Translate mouse screen x0,y0 coordinates to canvas coordinates
        self.rectx0 = self.canvas.canvasx(event.x)
        self.recty0 = self.canvas.canvasy(event.y)
        #Create rectangle
        self.rect = self.canvas.create_rectangle(
            self.rectx0, self.recty0, self.rectx0, self.recty0)


    def stopRect(self, event):
        self.move = False
        #Translate mouse screen x1,y1 coordinates to canvas coordinates
        self.rectx1 = self.canvas.canvasx(event.x)
        self.recty1 = self.canvas.canvasy(event.y)
        #Modify rectangle x1, y1 coordinates (final)
        self.canvas.create_rectangle(self.rectx0, self.recty0,
                      self.rectx1, self.recty1)
        print('Rectangle ended')

    def mainClip(self):
        print("Main Clip")
        print(self.lengthX)
        self.clip(self.rectx0,self.recty0,self.rectx1,self.recty0)
        self.clip(self.rectx1,self.recty0,self.rectx1,self.recty1)
        self.clip(self.rectx1,self.recty1,self.rectx0,self.recty1)
        self.clip(self.rectx0,self.recty1,self.rectx0,self.recty0)
        #Draw polygon Here
        self.canvas.delete("all")
        self.canvas.create_rectangle(self.rectx0, self.recty0,self.rectx1, self.recty1)
        for i in range(0,self.poly_size):
            self.canvas.create_line(self.newXpoints_array[i],self.newYpoints_array[i],self.newXpoints_array[i+1],self.newYpoints_array[i+1])

    def clip(self,x1,y1,x2,y2):
        self.i = 0
        for i in range(0,self.lengthX):
            self.k=(i+1) % self.lengthX
            self.ix = self.Xpoints_array[i]
            self.iy = self.Ypoints_array[i]
            self.kx = self.Xpoints_array[self.k]
            self.ky = self.Ypoints_array[self.k]
            self.i_pos =(x2-x1) * (self.iy-y1) - (y2-y1) * (self.ix-x1)
            self.k_pos =(x2-x1) * (self.ky-y1) - (y2-y1) * (self.kx-x1)

            if self.i_pos<0 and self.k_pos<0:
                self.newXpoints_array[self.poly_size] = self.kx
                self.newYpoints_array[self.poly_size] = self.ky
                self.poly_size = self.poly_size+1
            elif self.i_pos>=0 and self.k_pos<0:
                self.newXpoints_array[self.poly_size] = self.x_intersect(x1,y1, x2, y2, self.ix, self.iy, self.kx, self.ky)
                self.newYpoints_array[self.poly_size] = self.y_intersect(x1,y1, x2, y2, self.ix, self.iy, self.kx, self.ky)
                self.poly_size = self.poly_size+1
                self.newXpoints_array[self.poly_size] = self.kx
                self.newYpoints_array[self.poly_size] = self.ky
                self.poly_size = self.poly_size+1
            elif self.i_pos>=0 and self.k_pos<0:
                self.newXpoints_array[self.poly_size] = self.x_intersect(x1,y1, x2, y2, self.ix, self.iy, self.kx, self.ky)
                self.newYpoints_array[self.poly_size] = self.y_intersect(x1,y1, x2, y2, self.ix, self.iy, self.kx, self.ky)
                self.poly_size = self.poly_size+1
            else:
                print("No points added")

    def x_intersect(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.num = (x1*y2 - y1*x2) * (x3-x4) -(x1-x2) * (x3*y4 - y3*x4)
        self.den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
        return self.num/self.den
    def y_intersect(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.num = (x1*y2 - y1*x2) * (y3-y4) -(y1-y2) * (x3*y4 - y3*x4)
        self.den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
        return self.num/self.den


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
