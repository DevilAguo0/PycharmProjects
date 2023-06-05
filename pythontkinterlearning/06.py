from tkinter import *
root = Tk()
root.title("使用frame组件的例子")
root.geometry("200x400+30+40")
f1=Frame(root)
f1.pack()
f2=Frame(root)
f2.pack()
f3=LabelFrame(root,text="第三个Frame")
f3.pack(side="bottom")
Button(f1,text="red",fg="red").pack(side="left")
Button(f1,text="black",fg="black").pack(side="left")
Button(f2,text="Blue",fg="Blue").pack(side=LEFT)
Button(f3,text="green",fg="green").pack(side="left")














root.mainloop()