import time
from tkinter import *

root = Tk()

if time.daylight == 1:
    light = "It is light outside"
else:
    light = "It is dark outside"

def refresh(event, light):
    if time.daylight == 1:
        label.config(text="It is light outside")
    else:
        label.config(text= "It is dark outside")

label = Label(root, text=light)
label.pack()
button = Button(root, text="Refresh", command=refresh(time.daylight, light)).pack()

root.mainloop()
