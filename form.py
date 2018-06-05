import Tkinter as Tk
def get_text():
    print "You entered "+e1.get()
root=Tk.Tk()
root.title("Hello World")

frame1=Tk.Frame(root,bg="blue",height=200,width=400)
frame1.grid(row=1,column=1)#,sticky='n')

Tk.Button(frame1,text="Submit",command=get_text).grid(row=2,column=0,padx=20,pady=20)
e1=Tk.Entry(frame1)
e1.grid(row=1,column=0,padx=20,pady=20)

Tk.Label(frame1,text="Type something!").grid(row=0,column=0)

root.mainloop()


