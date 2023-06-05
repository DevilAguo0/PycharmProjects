import tkinter
import tkinter as tk
import random
from tkinter.messagebox import *





root = tkinter.Tk()
root.title('猜数字')
root.geometry("800x700+200+100")
root.resizable()
labelTemp = tk.Label(root, text='请任意10以内输入一个数字：', height=5, width=20, fg="blue")
labelTemp.pack()
def ran_Number():
    result = random.randint(1, 10)
    if result==labelTemp:
        showinfo("恭喜你答对啦！")
    else:
        showinfo("请重新输入！")
emptyNum = tk.Entry(root)
emptyNum.pack()
btnCal = tk.Button(root, text="输入数字：", command=ran_Number)
btnCal.pack()


root.mainloop()
