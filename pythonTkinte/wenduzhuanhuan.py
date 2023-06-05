# coding=utf-8

from tkinter import *
from converters import *  # 自定义的转换温度的类包（http://blog.csdn.net/houyanhua1/article/details/78050510）

from 温度转换 import ScaleAndOffsetConverter


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.t_conv = ScaleAndOffsetConverter('C', 'F', 1.8, 32)  # 初始函数中实例化转换温度的类对象，重复调用就不会重复实例化对象了
        Label(frame, text='deg C').grid(row=0, column=0)  # 标签
        self.c_var = DoubleVar()
        Entry(frame, textvariable=self.c_var).grid(row=0, column=1)  # 文本框
        Label(frame, text='deg F').grid(row=1, column=0)
        self.result_var = DoubleVar()
        Label(frame, textvariable=self.result_var).grid(row=1, column=1)

        button = Button(frame, text='Convert', command=self.convert)  # 按钮
        button.grid(row=2, columnspan=2)

    def convert(self):
        a = self.t_conv.convert(self.c_var.get())
        self.result_var.set(a)


root = Tk()
root.wm_title('Temp Converter')
app = App(root)
root.mainloop()