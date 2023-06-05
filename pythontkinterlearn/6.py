from tkinter import *
root = Tk()
label =Label(root,text="意见栏")
label.pack()
text = Text(root,width=30,height=5)
text.pack()
# Entry(root,width=30,highlightcolor="red").pack()
root.mainloop()
