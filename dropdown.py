import Tkinter as Tk

def color_change(*args):
    print "Color change alert! "+color.get()

root=Tk.Tk()
root.title("Dropdown")

frame1=Tk.Frame(root,height=200,width=400)
frame1.grid(row=1,column=1)#,sticky='n')

Tk.Label(frame1,text="pick a color",bg="white").grid(row=0,column=0,padx=20,pady=20)
color_choices=['mauve','ochre','turquoise','cyan']
color=Tk.StringVar(root)
color.set('cyan')
color_dropdown=Tk.OptionMenu(frame1,color,*color_choices).grid(row = 0, column =1,sticky='w')
color.trace('w',color_change)

root.mainloop()
