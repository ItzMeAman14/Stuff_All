from tkinter import *
from tkinter import messagebox
import time

win = Tk()
win.resizable(0,0)
win.geometry('500x600')

def fun(event):
    event.widget
    if var1.get() == "":
        messagebox.showwarning("Error", "Password Missing...")
    elif var.get() == "":
        messagebox.showwarning("Error", "Username Missing...")
    else:
        lau.config(text = var.get())
        lap.config(text = var1.get())

def func():
    if var1.get() == "":
        messagebox.showwarning("Error", "Password Missing...")
    elif var.get() == "":
        messagebox.showwarning("Error", "Username Missing...")
    else:
        lau.config(text = var.get())
        lap.config(text = var1.get())

la = Label(win, text = "FaceBook", font=('Garamond', 25), fg = "Blue")
la.pack()

l = Label(win, text = "Enter Username:", font=('Garamond', 15))
l.place(x = 50, y = 100)

var = StringVar()
e = Entry(win,bd = 2, textvariable=var)
e.bind('<Return>', fun)
e.place(x = 250, y = 103)

l = Label(win, text = "Enter Password:", font=('Garamond', 15))
l.place(x = 50, y = 150)

label = Label(win, text = time.asctime(time.localtime(time.time())))
label.place(x = 0, y = 0)

var1 = StringVar()
e = Entry(win,bd = 2, textvariable=var1)
e.bind('<Return>', fun)
e.place(x = 250, y = 153)


l = Label(win, text = "*******************************************************************************")
l.place(x = 0, y = 240)

lu = Label(win, text = "Your Username:", font=('Garamond', 15))
lu.place(x = 50, y = 300)

lau = Label(win, text = "********************")
lau.place(x = 250 ,y =303 )

lp = Label(win, text = "Your Password:", font=('Garamond', 15))
lp.place(x = 50, y = 350)

lap = Label(win, text = "********************")
lap.place(x = 250 ,y =353 )

bu = Button(win, text = "Log In", command = func)
bu.bind('<Return>', fun)
bu.place(x = 210 ,y = 200)
win.mainloop()