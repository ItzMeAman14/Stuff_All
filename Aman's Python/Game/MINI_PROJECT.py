from tkinter import *
from tkinter import ttk
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0

time  = 30

def New():
    root = Toplevel()
    root.title('GUESS THE COLOUR')

    root.geometry('500x500')

    instructions = Label(root , text = 'Type in the colour of the words,and not the word text!', font=('Helvetica', 12))
    instructions.pack()

    l = Label(root , text = "...Press Enter to start the Game...", font=('Helvetica', 15))
    l.place(x = 100, y = 190)

    scoreLabel = Label(root , text = 'Score:' + str(score), font = ('Helvetica', 25))
    scoreLabel.pack()

    a = score

    timeLabel = Label(root , text = 'Time left:' + str(time), font = ('Helvetica', 25))
    timeLabel.pack()

    colour = Label(root , font=('Helvetica',35))
    colour.pack()

    def startGame(event):

        if time == 30:

            countdown()

        
        nextcolour()

    colour_entry = Entry(root)

    colour_entry.focus_set()
    root.bind('<Return>', startGame)

    colour_entry.pack()
        
    def exit_scn():

        root.destroy()
        scn.destroy()
        
    def highscore():
        la = Label(root , text = "High Score : " + str(score), font=('Helvetica', 15))
        la.place(x = 350, y = 50)


    def countdown():
        global time

        if time > 0:

            time-=1

            timeLabel.config(text = 'Time Left:' + str(time))
        

            timeLabel.after(1000, countdown)

        elif time == 0:
            la1 = Label(root , text = "Game Over", font = ('Helvetica', 35))
            la1.place(x = 110 , y = 240)

            la = Label(root , text = "Your Score is : " + str(score), font = ('Helvetica', 25))
            la.place(x = 110 , y = 310)

            bu = Button(root, text = "Exit",font=('italic', 10), command = exit_scn)
            bu.place(x = 200, y = 370)

            highscore()


    def nextcolour():
        global score
        global time
        
        if time > 0:
            
            colour_entry.focus_set()

            if colour_entry.get().lower()==colours[1].lower():

                score+=1

            colour_entry.delete(0, END)

            random.shuffle(colours)

            colour.config(fg=str(colours[1]), text = str(colours[0]))

            scoreLabel.config(text = 'Score:' + str(score))
     





def prgsplay():
    import time
    l = Label(scn , text="Loading...Please Wait.......", font=('Helvetica',10))
    l.place(x = 97 , y = 120)
    for i in range(0, 11):
        prgs['value'] = 10*i
        prgs.update_idletasks()
        time.sleep(0.5)
        if prgs['value'] == 100:
            New()

if __name__=='__main__':

    scn = Tk()
    scn.title('Mini Project')
    scn.geometry('300x400')

    lab = Label(text = "Done")
    lab.place(x = 300 , y= 105)

    lab = Label(scn , text = "Click on the button to start the game")
    lab.pack(pady = 10)

    prgs = ttk.Progressbar(scn , length = 100, mode='determinate')
    
    btn  = Button(scn , text = 'Click Here', command=prgsplay)
    btn.pack(pady = 10)
    
    
    prgs.pack()
    

    scn.mainloop()
    
