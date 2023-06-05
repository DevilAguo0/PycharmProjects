from tkinter import *
from tkinter.messagebox import *


def btn1Click():
    showinfo("Info", "不要点我啊")


def btn2Click():
    showwarning("Warning", "警告⚠️")


def btn3Click():
    showerror("Error", "显示一个错误")


def btn4Click():
    askquestion("Question", "什么问题？")


def btn5Click():
    askokcancel("okCancle", "ok吗")


def btn6Click():
    askyesno("YesNo", "Askyesno Test")


def btn7Click():
    askretrycancel("Retry", "Askretrycancel Test")


root = Tk()
root.title("Messagebox Test")
btn1 = Button(root, text="Showinfo", command=btn1Click)
btn1.pack(fill=X)
Button(root, text="Showwarning", command=btn2Click).pack(fill=X)
Button(root, text="Showerror", command=btn3Click).pack(fill=X)
Button(root, text="Askquestion", command=btn4Click).pack(fill=X)
Button(root, text="Askokcancel", command=btn5Click).pack(fill=X)
Button(root, text="Askyesno", command=btn6Click).pack(fill=X)
Button(root, text="Askretrycancel", command=btn7Click).pack(fill=X)
root.mainloop()
