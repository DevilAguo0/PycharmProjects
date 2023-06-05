from tkinter import *

root = Tk()
root.title("温度转换")
root.geometry("800x400+200+400")
data = IntVar
def translate(data):
    result = data * 3
    return result


Label(root,text="转换{}°C to {}°F ".format(data,translate(data))).pack()


Entry(root, textvariable=data).pack()
Button(root, text="转换温度", command=translate).pack()
root.resizable
root.mainloop()
