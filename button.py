import Tkinter as Tk

root=Tk.Tk()
root.title("Hello World")

frame1=Tk.Frame(root,bg="blue",height=200,width=400)
frame1.grid(row=1,column=1)#,sticky='n')

Tk.Button(frame1,text="Click to quit",command=quit).grid(row=0,column=0,padx=20,pady=20)

root.mainloop()
