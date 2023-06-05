from tkinter import *
from tkinter.simpledialog import *


def inputStr():
    r = askstring("Python Tkinter", "input string", initialvalue="Python Tkinter")
    print(r)


def inputInt():
    r = askinteger("Python Tkinter", "input Inter")
    print(r)


def inputFloat():
    r = askfloat("Python Tkinter", "input Float")
    print(r)


root = Tk()
Button(root,text="Input String",command=inputStr).pack(side="left")
Button(root,text="Input Integer",command=inputInt).pack(side="left")
Button(root,text="Input Float",command=inputFloat).pack(side="left")
root.mainloop()