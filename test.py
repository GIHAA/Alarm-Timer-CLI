from cProfile import label
from cgitb import text
from tkinter import *



def create_alarm():

    new_window = Tk()
    Label(new_window,text="create_alarm").pack() 
    old_window.destroy()   #close out of old window
    
def create_timer():
    new_window = Tk()
    Label(new_window,text="create_timer").pack()     
    old_window.destroy()   #close out of old window

old_window = Tk()

Label(old_window,text=" ALARM / TIMER   by radser2001").pack()
Button(old_window,text="alarm",command=create_alarm).pack()
Button(old_window,text="timer",command=create_timer).pack()




old_window.mainloop()