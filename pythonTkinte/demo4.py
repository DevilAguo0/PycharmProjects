import tkinter as tk
root = tk.Tk()
a=tk.Toplevel()
b=tk.Toplevel()
root.title=("温度转换")
root.geometry("800x700+200+100")
root.resizable()
labelTemp = tk.Label(root,text='转换C to F...' ,height=5,width=20,fg="blue")
labelTemp.pack()
entryCd=tk.Entry(root)
entryCd.pack()
def btCLickde():
    cd = float(entryCd.get())
    labelTemp.config(text='%.2f C = %.2f F '%(cd,cd*1.8+32))
root.mainloop()


