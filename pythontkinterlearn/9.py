import tkinter
from tkinter import *
root = tkinter.Tk()
r=tkinter.StringVar()
r.set("1")
Radiobutton(root,variable=r,value="1",text="中国").pack()
Radiobutton(root,variable=r,value="2",text="美国").pack()
root.mainloop()
print(r.get())