 # -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 02:07:23 2020

@author: CASPER
"""

import sounddevice as sd
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")
import numpy as np

from PIL import ImageTk, Image
import wave
import scipy.io.wavfile as wf


master =Tk()
master.geometry("800x800")
master.title("")
record_time = DoubleVar()

canvas=[]
def forget_canvas():
    try:
        canvas.get_tk_widget().pack_forget()
    except AttributeError:
        pass
    

fs = 44100

def voice_rec():
    global myrecording
    global time
    
    
   
    # seconds
    duration = float(record_time.get())
    
    myrecording =  sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float64')
    
    time=np.linspace(0,len(myrecording)/fs,num=len(myrecording))
    
    sd.wait()
    
    fig,a2=plt.subplots(figsize=(12,3))
    plt.plot(time,myrecording, color="blue")
    plt.xlabel('time')
    plt.ylabel('Amplitude')
    plt.title('My Woice Wave')
    
    global canvas
    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().grid(column = 6)
  
    canvas.draw()
    plt.close("all")
    

    
    
def function(): 
    global master
    forget_canvas()
    global canvas
    if sayi.get() == 1:  
        myrecording2=np.abs(myrecording)
        
        fig,a3=plt.subplots(figsize=(9,3))
        plt.plot(myrecording2, linewidth=3.0)
        plt.title('Full Wave', fontsize=20, y=1.03)
        plt.xlabel('Sample Number', fontsize=15)
        plt.ylabel('Amplitude', fontsize=15)
        
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().grid(column = 6)
   
        plt.close("all")
       
        print(myrecording2)
         
    
    elif sayi.get() == 2:
        myrecordings=myrecording.clip(0)
        fig,a4=plt.subplots(figsize=(9,3))
        plt.plot(myrecordings)
        plt.title('Half Wave', fontsize=20, y=1.03)
        plt.xlabel('Sample Number', fontsize=15)
        plt.ylabel('Amplitude', fontsize=15)
        plt.ylabel('Amplitude', fontsize=15)
        #global canvas
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().grid(column = 6)
   
        plt.close("all")
        print(myrecordings)
        
    elif sayi.get()==3:
        myrecordingss=myrecording.min()
        myss=myrecording-myrecordingss
        fig,a5=plt.subplots(figsize=(9,3))
        plt.plot(myss)
        plt.title('OFFSET', fontsize=20, y=1.03)
        plt.xlabel('Sample Number', fontsize=15)
        plt.ylabel('Amplitude', fontsize=15)
        #global canvas
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().grid(column = 6)
   
        plt.close("all")
        print(myss)
        
        
    
   
     
sayi = IntVar()

r1 = Radiobutton(master, text="full wave", variable=sayi, value=1)
r1.grid(row=2, column=1, padx=5)
r2 = Radiobutton(master, text="half wave", variable=sayi, value=2)
r2.grid(row=3, column=1, padx=5)
r3 = Radiobutton(master, text="offset wave", variable=sayi, value=3)
r3.grid(row=4, column=1, padx=5)  
     
d = ttk.Button(master, text="RUN", command=function)
d.grid(row=3, column=2, padx=5)  
   
a = Label(master, text=" Voice Recoder : ")
a.grid(row=0, column=0, padx=5)

b = Entry(master, textvariable=record_time)
b.grid(row=0,column=1, padx=5)

c = ttk.Button(master, text="Start Record", command=voice_rec)
c.grid(row=0, column=2, padx=5)  





      


master.mainloop()