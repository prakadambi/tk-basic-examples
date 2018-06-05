import Tkinter as Tk

root = Tk.Tk()

v = Tk.IntVar()

Tk.Label(root,text="""Choose a 
programming language:""",justify = Tk.LEFT,
        padx = 20).pack()
Tk.Radiobutton(root,text="Python",padx = 20,variable=v,value=1).pack(anchor=Tk.W)
Tk.Radiobutton(root,text="Perl",padx = 20,variable=v,value=2).pack(anchor=Tk.W)

root.mainloop()
