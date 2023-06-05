from tkinter import *
from tkinter.filedialog import *
def openfile():
    r=askopenfilename(title="打开文件",filetypes=[('Pyhon','*.py.puw'),('All files','*')])
    print(r)
def savefile():
    r=askopenfilename(title="保存文件",initialdir="E:\\教学\\exp",initialfile="hello.py")
    print(r)
root = Tk()
root.title("打开文件对话框示例")
root.geometry("625x300")
btn1 = Button(root,text="File Open",command=openfile)
btn2=Button(root,text="FIle Save",command=savefile)
btn2.pack()
btn1.pack()
root.mainloop()
