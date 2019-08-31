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
from skimage.feature import greycomatrix, greycoprops

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
        fiveAndOthers = sixthings(path)
        list.append([newPath+i, fiveAndOthers[0], fiveAndOthers[1], fiveAndOthers[2],fiveAndOthers[3],fiveAndOthers[4],
                     fiveAndOthers[5]])

    xfile = 'file3.xlsx'
    print('file write')
    xbook = xlsxwriter.Workbook(xfile)
    xsheet = xbook.add_worksheet('data')

    xsheet.write_row(0, 0, ['Image label','Maximum probability','Correlation','Contrast',
                            'Uniformity(Energy)','Homogenity','Entropy'])

    for i in range (1,(len(list))):
        xsheet.write_row(i, 0, list[i-1])

    xsheet.write_row(i+1, 0, list[i])

    xbook.close()

def sixthings(path):
    img = Image.open(path)
    img_array = np.array(img.convert('L', colors=8))
    imgmatrix = greycomatrix(img_array,[1], [0], levels=256, symmetric=True, normed=True)
    max_prob = np.amax(imgmatrix)
    correlation = greycoprops(imgmatrix,'correlation')
    contrast = greycoprops(imgmatrix,'contrast')
    energy = greycoprops(imgmatrix, 'energy')
    homogeneity = greycoprops(imgmatrix,'homogeneity')
    entropy = -np.sum(imgmatrix*np.log2(imgmatrix + (imgmatrix==0)))
    return [max_prob,correlation,contrast,energy,homogeneity,entropy]


def loading_data():
    root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/", title='Select a file')
    dir = pd.read_excel(root.sourceFile)
    global name_data,max_prob_ary,correlation_ary,contrast_ary,energy_ary,homogeneity_ary,entropy_ary
    name_data = []
    max_prob_ary = []
    correlation_ary = []
    contrast_ary = []
    energy_ary = []
    homogeneity_ary = []
    entropy_ary = []

    name_data = dir.iloc[:, 0]
    max_prob_ary = dir.iloc[:, 1]
    correlation_ary = dir.iloc[:, 2]
    contrast_ary = dir.iloc[:, 3]
    energy_ary = dir.iloc[:, 4]
    homogeneity_ary = dir.iloc[:, 5]
    entropy_ary = dir.iloc[:, 6]

    print("Loading Done")

def loading_image():
    root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/", title='Please select a image')
    print(root.sourceFile)
    global imgq,max_probq,correlationq,contrastq,energyq,homogeneityq,entropyq
    imgq = Image.open(root.sourceFile)
    img_arrayq = np.array(imgq.convert('L', colors=8))
    imgmatrixq = greycomatrix(img_arrayq,[1], [0], levels=256, symmetric=True, normed=True)
    max_probq = np.amax(imgmatrixq)
    correlationq = greycoprops(imgmatrixq,'correlation')
    contrastq = greycoprops(imgmatrixq,'contrast')
    energyq = greycoprops(imgmatrixq, 'energy')
    homogeneityq = greycoprops(imgmatrixq,'homogeneity')
    entropyq = -np.sum(imgmatrixq*np.log2(imgmatrixq + (imgmatrixq==0)))

    print('Quary image')
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
        canberra_distance = (abs(max_prob_ary[j]-max_probq)/(abs(max_prob_ary[j])+abs(max_probq)))+(abs(correlation_ary[j]-correlationq)/(abs(correlation_ary[j])+abs(correlationq)))+(abs(contrast_ary[j]-contrastq)/(abs(contrast_ary[j])+abs(contrastq)))+(abs(energy_ary[j]-energyq)/(abs(energy_ary[j])+abs(energyq)))+(abs(homogeneity_ary[j]-homogeneityq)/(abs(homogeneity_ary[j])+abs(homogeneityq)))+(abs(entropy_ary[j]-entropyq)/(abs(entropy_ary[j])+abs(entropyq)))
        dis_list.append([newPath+i,canberra_distance])
        j = j+1

    print('before')
    print(dis_list[0])

    dis_list.sort(key=lambda x: x[1])
    print('after')
    print(dis_list[0])

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
