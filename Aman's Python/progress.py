from tkinter import *
from tkinter import ttk
import time

win = Tk()
win.geometry('500x500')
win.title("Timer With Progress")

def func():
    import time
    for i in range(0, 11):
        progress['value'] = 10*i
        progress.update_idletasks()
        time.sleep(0.5)

    lab = Label(text = "Done")
    lab.place(x = 300 , y= 105)



progress = ttk.Progressbar(win , length=100 , mode = "determinate")


btn = Button(win , text = "Start", command=func)
btn.place(x = 200 , y = 100)

progress.place(x = 200 , y = 20)

win.mainloop()