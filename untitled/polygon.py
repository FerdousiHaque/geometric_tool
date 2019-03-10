import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.points_recorded = []
        self.rectx0 = 0
        self.recty0 = 0
        self.rectx1 = 0
        self.recty1 = 0
        self.move = False
        self.canvas = tk.Canvas(self, width=400, height=400, bg = "white")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.button1 = tk.Button(self, text = "Window", command = self._createCanvasBinding)
        self.button1.pack(side="top", fill="both", expand=True)
        self.button2 = tk.Button(self, text = "Polygon", command = self.print_points)
        self.button2.pack(side="top", fill="both", expand=True)
        self.button3 = tk.Button(self, text = "Clipping")
        self.button3.pack(side="top", fill="both", expand=True)

    def print_points(self):
        self.canvas.bind("<Motion>", self.tell_me_where_you_are)
        self.canvas.bind("<B1-Motion>", self.draw_from_where_you_are)
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()
        self.canvas.create_line(self.points_recorded, fill = "red")
        self.points_recorded[:] = []

    def tell_me_where_you_are(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def draw_from_where_you_are(self, event):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()

        self.x = event.x
        self.y = event.y
        self.canvas.create_line(self.previous_x, self.previous_y,
                                self.x, self.y)
        self.points_recorded.append(self.previous_x)
        self.points_recorded.append(self.previous_y)
        self.points_recorded.append(self.x)
        self.points_recorded.append(self.x)
        self.previous_x = self.x
        self.previous_y = self.y

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

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
