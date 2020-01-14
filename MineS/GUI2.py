'''
Created on Dec 29, 2019

@author: TommyHessel
'''
 
from tkinter import *

def donothing():
    x = 0

root2 = Tk() 
butt = Button(root2, text = "Play")
butt2 = Button(root2, text = "Controls")
butt3 = Button(root2, text = "Quit")
butt.grid(row=0, column=0)
butt2.grid(row=0, column = 1)
butt3.grid(row=0, column = 2)
menubar = Menu(root2)
filemenu = Menu(menubar, tearoff=1)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root2.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root2.config(menu=menubar)
root2.mainloop()