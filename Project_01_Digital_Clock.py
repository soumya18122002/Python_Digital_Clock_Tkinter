from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk() # instanciating an object of the tkinter to make an frame 
root.title("Clock") # making an title of the frame as clock
# root.geometry("600x600")


def time():
    string = strftime("%H:%M:%S %p") # take a string to hold the output 
    label.config(text=string) # setting the text to the label
    label.config(font=("ds-digital", 96)) # setting the font and size of font
    label.after(1000, time) # taking 1000 time interval means after 1 sec the time value will be updated


label = Label(root, font="ds-digital", background="black", foreground="cyan")
# making a label to hold the output of the string and setting it's background foreground and font 
label.pack(anchor="center") # setting the position of the clock to the center and adding into the root frame

time() # calling of the function time
mainloop() # end of the frame 
