from tkinter import*
from tkinter import ttk

def new():
    nscn = Toplevel()
    nscn.geometry('500x500')
    if com['values'][1]== var.get():
        label = Label(nscn, text = "Monday",font = ('Helvetica',50))
        label.pack()
    elif com['values'][2] == var.get():
        label = Label(nscn, text = "Tuesday",font = ('Helvetica',50))
        label.pack()
    elif com['values'][3] == var.get():
        label = Label(nscn, text = "Wednesday",font = ('Helvetica',50))
        label.pack()
    elif com['values'][4] == var.get():
        label = Label(nscn, text = "Thursday",font = ('Helvetica',50))
        label.pack()
    elif com['values'][5] == var.get():
        label = Label(nscn, text = "Friday",font = ('Helvetica',50))
        label.pack()
    elif com['values'][6] == var.get():
        label = Label(nscn, text = "Saturday",font = ('Helvetica',50))
        label.pack()
    nscn.mainloop()

scn=Tk()
scn.geometry("500x250")
lbl=Label(scn,text="select day")
lbl.pack()

var = StringVar()
com=ttk.Combobox(scn,width=25,textvariable=var)
com['state']='readonly'
com['values']=('sun','mon','tue','wed','thu','fri','sat')
com.pack()

print(com['values'][6])

btn=Button(scn,text="ok",command = new)
btn.place(x=200,y=200)

scn.mainloop()