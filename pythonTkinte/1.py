import tkinter

root = tkinter.Tk()
lb = tkinter.Label(root, text="hello python")
lb.pack()
bt1 = tkinter.Button(root, text="BUTTON1")
bt1.pack(side="left")
bt2 = tkinter.Button(root, text="BUTTON2")
bt2.pack(side="right", anchor="ne", fill="both", expand=1, ipadx=30, ipady=40, padx=20, pady=40)
root.mainloop()


