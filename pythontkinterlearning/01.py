from tkinter import *
root = Tk()
m=StringVar()
def callbutton1():
    print(m.get())
def callbutton2():
    for i in lb.curselection():
        print(lb.get(i))
root.title("Listbox Test")
lb=Listbox(root,listvariable=m)
for item in["北京","天津","上海"]:
    lb.insert(END,item)
lb.pack()
b1=Button(root,text="获取listbox的所有内容",command=callbutton1,width=20)
b1.pack()
b2=Button(root,text="获取Listbox的选中内容",command=callbutton2,width=20)
b2.pack()
root.mainloop()