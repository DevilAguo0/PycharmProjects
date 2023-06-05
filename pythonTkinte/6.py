from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Button Test")


def callback():
    showinfo("人生苦短，我用Python！")



Button(root, text="外观装饰边界附近的标签", width=19, relief=GROOVE,bg="red").pack()
Button(root,text="设置按钮状态",width=21,state=DISABLED).pack()
Button(root,text="设置bimtmap放到按钮左边位置",compound="left",bitmap="error").pack()
Button(root,text="设置command事件调用命令",fg="blue",bd=2,command=callback).pack()
Button(root,text="设置高度宽度以及文字显示位置",anchor="sw",width=30,height=2).pack()


root.mainloop()
