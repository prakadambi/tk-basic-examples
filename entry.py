import Tkinter as Tk

root=Tk.Tk()
root.title("Hello World")

frame1=Tk.Frame(root,bg="blue")
frame1.grid(row=0,column=0)#,sticky='n')

e1=Tk.Entry(frame1)
#e1.insert(0,"Demonstrating Entry widget")
e1.grid(row=0,column=0,padx=20,pady=20)

#print e1.get()
root.mainloop()
