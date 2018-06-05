import Tkinter
root = Tkinter.Tk(  )
for r in range(3):
   for c in range(4):
      Tkinter.Label(root, text='Row%s/Column%s'%(r,c),fg="red",
         padx=5,pady=5 ).grid(row=r,column=c)
root.mainloop( )
