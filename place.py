from Tkinter import *

root = Tk()
root.geometry("200x100")
w = Label(root, text="Red", bg="red", fg="white")
w.place(x=20,y=10,width=100,height=20)
w = Label(root, text="Green", bg="green", fg="black")
w.place(x=20,y=30,width=100,height=20)
w = Label(root, text="Blue", bg="blue", fg="white")
w.place(x=20,y=50,width=100,height=20)

mainloop()
