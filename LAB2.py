from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from os import listdir
from os.path import isfile, join
from PIL import Image,ImageTk
import numpy as np
import xlsxwriter
import pandas as pd

root = tk.Tk()
root.geometry("630x300")

label1 = Label(root, text="Show here the Query Image", font=("Helvetica", 12))
label1.pack(side='top')


list = []
dis_list = []

def browse_button():
    global filename
    filename = filedialog.askdirectory()
    print(filename)

def calculation():
    global newPath
    newPath = filename + '/'
    global files
    files = [f for f in listdir(newPath) if isfile(join(newPath, f))]
    for i in files:
        path = newPath+i
        fiveAndOthers = fiveAndvariance(path)
        list.append([newPath+i, fiveAndOthers[0], fiveAndOthers[1], fiveAndOthers[2],fiveAndOthers[3],fiveAndOthers[4],
                     fiveAndOthers[5]])

    xfile = 'file.xlsx'
    print('writing file')
    xbook = xlsxwriter.Workbook(xfile)
    xsheet = xbook.add_worksheet('data')

    xsheet.write_row(0, 0, ['Image label','Min','Q1','Median','Q3','Max','Variance'])

    for i in range (1,(len(list))):
        xsheet.write_row(i, 0, list[i-1])

    xsheet.write_row(i+1, 0, list[i])

    xbook.close()

def fiveAndvariance(path):
    img = Image.open(path).convert('L')
    arry = np.array(img)
    max=np.amax(arry)
    min=np.amin(arry)
    q3=np.percentile(arry, 75)
    q1=np.percentile(arry, 25)
    median=np.percentile(arry, 50)
    ver= np.mean(abs(arry - arry.mean())**2)
    return [min,q1,median,q3,max,ver]


def loading_data():
    root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/", title='Select a file')
    dir = pd.read_excel(root.sourceFile)
    global name_data,max_data,min_data,q3_data,q1_data,median_data,ver_data
    name_data = []
    max_data = []
    min_data = []
    q3_data = []
    q1_data = []
    median_data = []
    ver_data = []

    name_data = dir.iloc[:, 0]
    max_data = dir.iloc[:, 1]
    min_data = dir.iloc[:, 2]
    q3_data = dir.iloc[:, 3]
    q1_data = dir.iloc[:, 4]
    median_data = dir.iloc[:, 5]
    ver_data = dir.iloc[:, 6]

    print("Loading Done")

def loading_image():
    root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/", title='Please select a image')
    print(root.sourceFile)
    global img,queryImg,max,min,q3,q1,median,ver
    img = Image.open(root.sourceFile).convert('L')
    queryImg=np.array(img)

    max=np.amax(queryImg)
    min=np.amin(queryImg)
    q3=np.percentile(queryImg, 75)
    q1=np.percentile(queryImg, 25)
    median=np.percentile(queryImg, 50)
    ver= np.mean(abs(queryImg - queryImg.mean())**2)
    print(max,min,median,q3,q1,ver)

    #image show
    showImg=Image.open(root.sourceFile)
    tkimage = ImageTk.PhotoImage(showImg)
    label=Label(root,image = tkimage)
    label.image = tkimage
    label.pack(side='top')


def display():
    print('image analysis')
    j=0
    for i in files:
        dis_list.append([newPath+i,float(abs(max-max_data[j])+abs(min-min_data[j])+abs(q3-q3_data[j])+abs(q1-q1_data[j])+
                                                 abs(median-median_data[j])+abs(ver-ver_data[j]))])
        j = j+1

    print('before')
    print(dis_list[1])

    dis_list.sort(key=lambda x: x[1])
    print('after')
    print(dis_list[1])

    #Display 10 IMAGE
    for i in range(0,5):
        image = Image.open(dis_list[i][0])
        image = image.resize((100, 75), Image.ANTIALIAS) #(height, width)
        pic = ImageTk.PhotoImage(image)
        label=Label(root,image = pic)
        label.image = pic
        label.pack(side='right')

    for i in range(5,10):
        image = Image.open(dis_list[i][0])
        image = image.resize((75, 80), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(image)
        label=Label(root,image = pic)
        label.image = pic
        label.pack(side='bottom')


button1 = tk.Button(root,
                   text="Load Training images",
                   fg="blue",
                   command=browse_button)

button1.pack(side='left')

button2 = tk.Button(root,
                   text="Extract Feature and store in database",
                   fg="green",
                   command=calculation)

button2.pack(side='left')

button3 = tk.Button(root,
                   text="Load Feature Data",
                   fg="red",
                   command=loading_data)

button3.pack(side='left')

button4 = tk.Button(root,
                   text="Load Query image",
                   fg="orange",
                   command=loading_image)

button4.pack(side='left')
button5 = tk.Button(root,
                   text="Display Images",
                   fg="black",
                   command=display)

button5.pack(side='left')

label2 = Label(root, text="Similar Images", font=("Helvetica", 14))
label2.pack(side='left')
root.mainloop()
