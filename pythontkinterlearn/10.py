import tkinter as tk

def colorChecked():
    label.config(fg=color.get())
def typeChecked():
   textType=typeBlod.get()+typeItalic.get()
   if textType
root = tk.Tk()
root.title("Radio & Check Test")
label = tk.Label(root,text="CHeck the format of text",height = 3,font=("Arail",12))
label.config(fg="blue")
label.pack()
color = tk.StringVar()
color.set("blue")
tk.Radiobutton(root,text="红色",variable=color,value="red",command=colorChecked).pack(side=tk.LEFT)
tk.Radiobutton(root,text="蓝色",variable=color,value="blue",command=colorChecked).pack(side=tk.LEFT)
tk.Radiobutton(root,text="绿色",variable=color,value="green",command=colorChecked).pack(side=tk.LEFT)
typeBlod=tk.IntVar()
typeItalic=tk.IntVar()
tk.Checkbutton(root,text="粗体",variable=typeBlod,offvalue=1,onvalue=0,command=typeChecked).pack(side=tk.LEFT)
tk.Checkbutton(root,text="斜体",variable=typeItalic,onvalue=2,offvalue=0,command=typeChecked).pack(side=tk.LEFT)
root.mainloop()