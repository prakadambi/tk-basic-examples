import Tkinter as Tk

root=Tk.Tk()
root.title("Frame")

frame1=Tk.Frame(root,bg="blue",height=200,width=400)
frame1.grid(row=1,column=1,sticky='n')

frame2=Tk.Frame(root,bg="red",height=200,width=400)
frame2.grid(row=2,column=1)

frame3=Tk.Frame(root,bg="green",height=400,width=400)
frame3.grid(row=1,column=1,columnspan=2)

frame1.tkraise()
root.mainloop()
