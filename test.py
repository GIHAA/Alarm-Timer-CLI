from cProfile import label
from cgitb import text
from tkinter import *
from turtle import width
import tkinter as tk

def create_alarm():

    new_window = Tk()
    new_window.geometry("500x200")
    Label(new_window,text="create_alarm").pack() 
    old_window.destroy()   #close out of old window
    
def create_timer():
    root= Tk()

    # canvas1 = tk.Canvas(root, width = 400, height = 300)
    # canvas1.pack()

    # entry1 = tk.Entry (root) 
    # canvas1.create_window(200, 140, window=entry1)
    
    # entry2 = tk.Entry (root) 
    # canvas1.create_window(200, 140, window=entry2)
        
    # entry3 = tk.Entry (root) 
    # canvas1.create_window(200, 140, window=entry3)

    # def getSquareRoot ():  
    #     x1 = entry1.get()
    root.geometry("500x200")
    e1 = Entry(root,width=50)
    e1.pack()
    
    e2 = Entry(root,width=50)
    e2.pack()
    
    e3 = Entry(root,width=50)
    e3.pack()
    
    e1.insert(0,"Enter Hours: ")
    e2.insert(0,"Enter minutes: ")
    e3.insert(0,"Enter seconds: ")
    old_window.destroy()   #close out of old window

old_window = Tk()
old_window.geometry("500x200")

Label(old_window,text=" ALARM / TIMER   by radser2001").pack()
Button(old_window,text="alarm",command=create_alarm).pack()
Button(old_window,text="timer",command=create_timer).pack()




old_window.mainloop()