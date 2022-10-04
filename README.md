
# Clock using Tkinter Python

This is a simple and fun project in python for the biggeners who started their journey in pyhton gui making. 



## Deployment

To Install Tkinter please follow the below code

```bash
  pip install tkintertable
```

Now to use it you need to import it into your code to do that you need to follow below steps

```bash
  from tkinter import *
```
while we type the above command all the libraries from the Tkinter got importd into our code no need to import them one by one separately

Now need to import ttk from the Tkinter by the following code
```bash
  from tkinter.ttk import *
```
That code  tkinter.ttk causes several widgets (Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale and Scrollbar) to automatically replace the Tk widgets.

This has the direct benefit of using the new widgets which gives a better look and feel across platforms; however, the replacement widgets are not completely compatible. The main difference is that widget options such as “fg”, “bg” and others related to widget styling are no longer present in Ttk widgets. Instead, use the ttk.Style class for improved styling effects.

For more info visit https://docs.python.org/3/library/tkinter.ttk.html

Now need to import the strftime from time to do that follow the below lines
```bash
  from time import strftime
```
strftime() method comes from the class strftime and this comes from the module time

The strftime() method can be used to create formatted strings

The string you pass to the strftime() method may contain more than one format codes.
```bash
    root = Tk()
```
Instanciating an object of the tkinter to make an frame here I use the name root you can give any name as you want

```bash
    root.title("Clock")
```
Making an title of the frame as clock
```bash
    root.geometry("600x600")
```
To set the window size 600px X 600px
```bash
    def time():
    string = strftime("%H:%M:%S %p") # take a string to hold the output 
    label.config(text=string) # setting the text to the label
    label.config(font=("ds-digital", 96)) # setting the font and size of font
    label.after(1000, time) # taking 1000 time interval means after 1 sec the time value will be updated
```
The above function time is to fetch the current time
```bash
    label = Label(root, font="ds-digital", background="black", foreground="cyan")
    # making a label to hold the output of the string and setting it's background foreground and font 
    label.pack(anchor="center") # setting the position of the clock to the center and adding into the root frame
```
The above code is to make an label and pack is to add the label into the window that is made by tkinter framework
```bash
    time()
```
This is the function calling of the method that we just made to fetch the current timing
```bash
    mainloop()
```
Mainloop() here used to make the user understand that the execution becomes stop if we type anything after the mainloop() it will simply be eliminated and not executed by the interpreter
For more info can visit https://realpython.com/python-gui-tkinter/#:~:text=window.mainloop()%20tells%20Python,where%20you%20called%20the%20method.


##

                                                Thank You