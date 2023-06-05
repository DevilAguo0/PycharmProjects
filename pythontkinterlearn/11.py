from tkinter import *
root = Tk()
def hello():
    print("单击主菜单")
menubar=Menu(root)  #  创建菜单栏
filter_menu=Menu(menubar,tearoff=False)  #  创建空菜单
# for item in ["文件","编辑","视图"]:
#     m.add_command(label=item,command=hello)
filter_menu.add_command(label="文件",command=hello)
filter_menu.add_command(label="编辑",command=hello)
menubar.add_cascade(label="主菜单",menu=filter_menu)
# root['menu'] = filter_menu
root.config(menu=menubar)
root.mainloop()

# from tkinter import *
#
# root = Tk()
# menubar = Menu(root)  # 创建菜单栏
# file_menu = Menu(menubar, tearoff=False) # 创建空菜单
# file_menu.add_command(label="a") # 向file_menu菜单中添加label
# file_menu.add_command(label="b")
# menubar.add_cascade(label="A", menu=file_menu) # 将file_menu菜单添加到菜单栏
# root.config(menu=menubar) # display the menu
# root.mainloop()
