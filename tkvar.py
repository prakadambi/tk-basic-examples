import Tkinter as Tk

root=Tk.Tk()
root.title("Tkvar")

frame1=Tk.Frame(root,bg="blue")
frame1.grid(row=0,column=0)#,sticky='n')

tkvar=Tk.StringVar()
tkvar.set("hello")
e1=Tk.Entry(frame1,textvariable=tkvar)
e1.grid(row=0,column=0,padx=20,pady=20)

def varwrite(*args):
    print "Write:",tkvar.get()

tkvar.trace("w", varwrite)

#print e1.get()
root.mainloop()
