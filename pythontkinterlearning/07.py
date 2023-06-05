from tkinter import *
colors = ["red","orange","yellow","blue","green","purple"]
root  = Tk()
root.title("使用after()刷新GUi图像界面")
f=Frame(root,width=200,height=200)
f.color=0
f['bg']=colors[f.color]
lb = Label(f,text='0')
lb.pack()
def foo():
    f.color = (f.color + 1)%(len(colors))
    lb['bg'] = colors[f.color]
    lb['text'] = str(int(lb['text'])+1)
    f.after(500,foo)
f.pack()
f.after(500,foo)
root.mainloop()