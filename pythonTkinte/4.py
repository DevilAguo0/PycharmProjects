from tkinter import *
root =Tk()
root.title="按钮"
Button(root,text="Button1",relief=FLAT).grid(row=0,column=0)
Button(root,text="Button2",relief=RAISED).grid(row=1,column=0)
Button(root,text="Button2",relief=SUNKEN).grid(row=2,column=0)
Button(root,text="Button2",relief=GROOVE).grid(row=3,column=0)
Button(root,text="Button2",relief=RIDGE).grid(row=4,column=0)
Button(root,text="Button2",relief=SOLID).grid(row=5,column=0)



root.mainloop()
