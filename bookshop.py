from tkinter import *
import backend

def get_row(event):
    try:
        global selec
        index=list1.curselection()[0]
        selec=list1.get(index)
    # return(selec)
        e1.delete(0,END)
        e1.insert(END,selec[1])
        e2.delete(0,END)
        e2.insert(END,selec[2])
        e3.delete(0,END)
        e3.insert(END,selec[3])
        e4.delete(0,END)
        e4.insert(END,selec[4])
    except IndexError:
        pass
def view_cmd():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def src():
    list1.delete(0,END)
    for row in backend.search(titletx.get(),authtx.get(),yrtx.get(),isbtx.get()):
        list1.insert(END,row)
def add():
    backend.insert(titletx.get(),authtx.get(),yrtx.get(),isbtx.get())
    list1.delete(0,END)
    list1.insert(END,(titletx.get(),authtx.get(),yrtx.get(),isbtx.get()))

def dele():    
    backend.delete(selec[0])
def upd():    
    backend.update(selec[0],titletx.get(),authtx.get(),yrtx.get(),isbtx.get())    





window=Tk()
window.wm_title("Book Store")
l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

titletx=StringVar()
e1=Entry(window,textvariable=titletx)
e1.grid(row=0,column=1)
authtx=StringVar()
e2=Entry(window,textvariable=authtx)
e2.grid(row=0,column=3)
yrtx=StringVar()
e3=Entry(window,textvariable=yrtx)
e3.grid(row=1,column=1)
isbtx=StringVar()
e4=Entry(window,textvariable=isbtx)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
list1.bind('<<ListboxSelect>>',get_row)
sb=Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)


b1=Button(window,text="View",width=12,command=view_cmd)
b1.grid(row=2,column=3)
b2=Button(window,text="Search entry",width=12,command=src)
b2.grid(row=3,column=3)
b3=Button(window,text="Insert",width=12,command=add)
b3.grid(row=4,column=3)
b4=Button(window,text="Update",width=12,command=upd)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete",width=12,command=dele)
b5.grid(row=6,column=3)
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)





window.mainloop()