import Tkinter as Tk
n=0

def count():
    global n
    n+=1
    print "clicked "+str(n)+" times"

root=Tk.Tk()
root.title("Callback")

frame1=Tk.Frame(root,bg="blue")
frame1.grid(row=1,column=1)#,sticky='n')

Tk.Button(frame1,height=2,width=4,text="Click",command=count).grid(row=0,column=0,padx=20,pady=20)

root.mainloop()
