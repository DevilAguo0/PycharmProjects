from tkinter import *
root = Tk()
root.title("登录")
root['width'] = 200
root['height'] = 80
Label(root,text="用户名",width=6).place(x=1,y=1)
Entry(root,width=20).place(x=55,y=1)
Label(root,text="密码",width=6).place(x=1,y=20)
Entry(root,width=20).place(x=55,y=20)
Button(root,text="登录",width=5,bg="#FFFF00").place(x=75,y=50)
Button(root,text="注册",width=5,bg="#FFFF00").place(x=165,y=50)
root.mainloop()
