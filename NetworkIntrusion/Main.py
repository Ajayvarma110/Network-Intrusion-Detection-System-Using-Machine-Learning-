import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import Logisticregression as LR
import RF as RF
import SVMa as svmalgo

import KNN as knn

bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"


def Home():
        global window
        def clear():
            print("Clear1")
            txt.delete(0, 'end')    
            
  



        window = tk.Tk()
        window.title("Network Intrusion Detection")
        
 
        window.geometry('1580x960')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window, text="Network Intrusion Detection Using Machine Learning" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=2,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=1)

        lbl = tk.Label(window, text="Dataset",width=10  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=400, y=200)
        
        txt = tk.Entry(window,width=15,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=600, y=210)
        

        


        def browse():
                path=filedialog.askopenfilename()
                print(path)
                txt.delete(0, 'end')
                txt.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Datset")     

        
        
                
        def LRprocess():
                sym=txt.get()
                if sym != "":
                        LR.process(sym)
                        tm.showinfo("Input", "Logistic Regression Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def RFprocess():
                sym=txt.get()
                if sym != "":
                        RF.process(sym)
                        tm.showinfo("Input", "Random Forest Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        
        def KNNprocess():
                sym=txt.get()
                if sym != "":
                        knn.process(sym)
                        tm.showinfo("Input", "KNN Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
        def SVMprocess():
                sym=txt.get()
                if sym != "":
                        svmalgo.process(sym)
                        tm.showinfo("Input", "SVM Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        

        browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=400, y=300)

        clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=600, y=300)
         
            

        LRbutton = tk.Button(window, text="LogisticRegression", command=LRprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        LRbutton.place(x=100, y=500)


        RFbutton = tk.Button(window, text="RandomForest", command=RFprocess  ,fg=fgcolor   ,bg=bgcolor1 ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        RFbutton.place(x=300, y=500)

        

        SVM1button1 = tk.Button(window, text="KNN", command=KNNprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVM1button1.place(x=500, y=500)
        SVM1button = tk.Button(window, text="SVM", command=SVMprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        SVM1button.place(x=700, y=500)

        

        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=14  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=900, y=500)

        window.mainloop()
Home()

