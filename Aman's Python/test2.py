from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0
highscore = []
time  = 30

turn = "X"
draw = 10
xscore = 0
oscore = 0

def switch():
    a = messagebox.askyesno("QUIT","Do you really want to switch game?")
    if a == True:
        scn.destroy()
        ColourGame()

def TTT():

    btn.destroy()
    btn2.destroy()
    prgs.destroy()
    lab.destroy()
    scn.geometry('500x500')
    scn.resizable(0,0)

    frame1 = Frame(scn)
    frame1.pack()

    label = Label(frame1 , text = "Tic Tac Toe", font=("Garamond", 35),  foreground='black')
    label.pack()

    frame2 = Frame(scn)
    frame2.pack()

    def exit():
        a = messagebox.askyesno("QUIT","Do you really want to quit?")
        if a == True:
            scn.destroy()


    def restart():
        global turn
        global draw
        turn = "X"
        labchance.config(text = "X's Turn",font= ("Garamond", 25), underline = 0)
        draw = 10
        button1['text'] = " "
        button2['text'] = " "
        button3['text'] = " "
        button4['text'] = " "
        button5['text'] = " "
        button6['text'] = " "
        button7['text'] = " "
        button8['text'] = " "
        button9['text'] = " "
        #state changing
        button1['state'] = NORMAL
        button2['state'] = NORMAL
        button3['state'] = NORMAL
        button4['state'] = NORMAL
        button5['state'] = NORMAL
        button6['state'] = NORMAL
        button7['state'] = NORMAL
        button8['state'] = NORMAL
        button9['state'] = NORMAL


    def play(event):
        global turn
        global draw
        global xscore
        global oscore
        button = event.widget
        if turn == "X":
            button['text'] = "X"
            button['font'] = "Helvetica", 15
            button['state'] = DISABLED
            turn = "O"
            labchance.config(text = "O's Turn",font= ("Garamond", 25), underline = 0)
            draw -=1
            if button1['text'] == "X" and button2['text'] == "X" and button3['text'] == "X":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED
                draw +=1 
                xscore +=1
                Xlabel.config(text=("X Score: " + str(xscore)))
                messagebox.showinfo("O Loses", "X Wins") 
            elif button4['text'] == "X" and button5['text'] == "X" and button6['text'] == "X":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED
                draw +=1 
                xscore +=1
                Xlabel.config(text=("X Score: " + str(xscore)))
                messagebox.showinfo("O Loses", "X Wins") 
            elif button7['text'] == "X" and button8['text'] == "X" and button9['text'] == "X":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED
                draw +=1
                xscore +=1
                Xlabel.config(text=("X Score: " + str(xscore)))
                messagebox.showinfo("O Loses","X Wins") 
                #All Horizontal Checks
            elif button1['text'] == "X" and button4['text'] == "X" and button7['text'] == "X":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED
                draw +=1 
                xscore +=1
                Xlabel.config(text=("X Score: " + str(xscore)))
                messagebox.showinfo("O Loses","X Wins") 
            elif button2['text'] == "X" and button5['text'] == "X" and button8['text'] == "X":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED
                draw +=1 
                xscore +=1
                Xlabel.config(text=("X Score: " + str(xscore)))
                messagebox.showinfo("O Loses","X Wins") 
            elif button3['text'] == "X" and button6['text'] == "X" and button9['text'] == "X":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                draw +=1 
                xscore +=1
                Xlabel.config(text=("X Score: " + str(xscore)))
                messagebox.showinfo("O Loses","X Wins")
            elif button1['text'] == "X" and button5['text'] == "X" and button9['text'] == "X":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                xscore +=1
                draw +=1 
                Xlabel.config(text=("X Score: " + str(xscore)))
                messagebox.showinfo("O Loses","X Wins") 
            elif button3['text'] == "X" and button5['text'] == "X" and button7['text'] == "X":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                xscore +=1
                draw +=1 
                Xlabel.config(text=("X Score: " + str(xscore)))
                messagebox.showinfo("O Loses","X Wins") 
            elif draw == 1 :
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                messagebox.showinfo("Draw", "Game Draw")
        # O's Turns
        else:
            button['text'] = "O"
            button['font'] = "Helvetica", 15
            button['state'] = DISABLED
            turn = "X"
            labchance.config(text = "X's Turn",font= ("Garamond", 25), underline = 0)
            draw -=1 
            if button1['text'] == "O" and button2['text'] == "O" and button3['text'] == "O":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                oscore +=1
                draw +=1 
                Olabel.config(text=("O Score: " + str(oscore)))
                messagebox.showinfo("X Loses", "O Wins") 
            elif button4['text'] == "O" and button5['text'] == "O" and button6['text'] == "O":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                oscore +=1
                draw +=1 
                Olabel.config(text=("O Score: " + str(oscore)))
                messagebox.showinfo("X Loses", "O Wins") 
            elif button7['text'] == "O" and button8['text'] == "O" and button9['text'] == "O":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                oscore +=1
                draw +=1 
                Olabel.config(text=("O Score: " + str(oscore)))
                messagebox.showinfo("X Loses","O Wins") 
                #All Horizontal Checks
            elif button1['text'] == "O" and button4['text'] == "O" and button7['text'] == "O":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                oscore +=1
                draw +=1 
                Olabel.config(text=("O Score: " + str(oscore)))
                messagebox.showinfo("X Loses","O Wins") 
            elif button2['text'] == "O" and button5['text'] == "O" and button8['text'] == "O":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                oscore +=1
                draw +=1 
                Olabel.config(text=("O Score: " + str(oscore)))
                messagebox.showinfo("X Loses","O Wins") 
            elif button3['text'] == "O" and button6['text'] == "O" and button9['text'] == "O":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                oscore +=1
                draw +=1 
                Olabel.config(text=("O Score: " + str(oscore)))
                messagebox.showinfo("X Loses","O Wins") 
                #All Vertical Checks
            elif button1['text'] == "O" and button5['text'] == "O" and button9['text'] == "O":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                oscore +=1
                draw +=1 
                Olabel.config(text=("O Score: " + str(oscore)))
                messagebox.showinfo("X Loses","O Wins") 
            elif button3['text'] == "O" and button5['text'] == "O" and button7['text'] == "O":
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                oscore +=1
                draw +=1 
                Olabel.config(text=("O Score: " + str(oscore)))
                messagebox.showinfo("X Loses","O Wins") 
            elif draw == 1:
                button1['state'] = DISABLED 
                button2['state'] = DISABLED 
                button3['state'] = DISABLED 
                button4['state'] = DISABLED 
                button5['state'] = DISABLED 
                button6['state'] = DISABLED 
                button7['state'] = DISABLED 
                button8['state'] = DISABLED 
                button9['state'] = DISABLED 
                messagebox.showinfo("Draw", "Game Draw")

    button1 = Button(frame2, text = " ", height=3 , width=4)
    button1.grid(row = 0, column=1)
    button1.bind('<Button-1>', play)


    button2 = Button(frame2, text = " ", height=3 , width=4)
    button2.grid(row = 0, column=2)
    button2.bind('<Button-1>', play)


    button3 = Button(frame2, text = " ", height=3 , width=4)
    button3.grid(row = 0, column=3)
    button3.bind('<Button-1>', play)

    #2nd row
    button4 = Button(frame2, text = " ", height=3 , width=4)
    button4.grid(row = 1, column=1)
    button4.bind('<Button-1>', play)

    button5 = Button(frame2, text = " ", height=3 , width=4)
    button5.grid(row = 1, column=2)
    button5.bind('<Button-1>', play)

    button6 = Button(frame2, text = " ", height=3 , width=4)
    button6.grid(row = 1, column=3)
    button6.bind('<Button-1>', play)

    #3rd row
    button7 = Button(frame2, text = " ", height=3 , width=4)
    button7.grid(row = 2, column=1)
    button7.bind('<Button-1>', play)

    button8 = Button(frame2, text = " ", height=3 , width=4)
    button8.grid(row = 2, column=2)
    button8.bind('<Button-1>', play)

    button9 = Button(frame2, text = " ", height=3 , width=4)
    button9.grid(row = 2, column=3)
    button9.bind('<Button-1>', play)

    b = Button(scn, text = "Restart Game", command=restart)
    b.place(x = 300, y = 350)

    change_button = Button(scn, text = "Switch Game",command = switch)
    change_button.place(x = 200 , y = 450)

    b1 = Button(scn, text = "Exit", command=exit)
    b1.place(x = 100, y = 350)

    Xlabel = Label(scn, text = "X Score:" + str(xscore), font = ('Garamond', 25), underline=0)
    Xlabel.place(x = 50 , y = 400)

    labchance = Label(scn, text = "X's Turn", font = ("Garamond", 25), underline=0)
    labchance.place(x = 190, y = 298)

    Olabel = Label(scn, text='O Score:' + str(oscore), font = ("Garamond", 25), underline=0)
    Olabel.place(x = 250 , y= 400)
    scn.mainloop()

def ColourGame():
    root = Toplevel()
    root.resizable(0,0)
    root.title('GUESS THE COLOUR')

    root.geometry('500x500')

    instructions = Label(root , text = 'Type in the colour of the words,and not the word text!', font=('Helvetica', 12))
    instructions.pack()

    l = Label(root , text = "...Press Enter to start the Game...", font=('Helvetica', 15))
    l.place(x = 100, y = 190)

    scoreLabel = Label(root , text = 'Score:' + str(score), font = ('Helvetica', 25))
    scoreLabel.pack()

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
        
    # def highscore():
    #     la = Label(root , text = "High Score : " + str(score), font=('Helvetica', 15))
    #     la.place(x = 350, y = 50)
    #     highscore.append(score)
    #     print(highscore)

    def restart():
        global score
        global time
        score = 0
        time = 30
        scoreLabel.config(text = "Score:" + str(score), font = ("Helvetica", 25))
        # if highscore[0] > score:
        #     score.config(text = "High Score : " + str(score), font =("Helvetica", 15))
        root.destroy()
        ColourGame()

    def countdown():
        global time

        if time > 0:

            time-=1

            timeLabel.config(text = 'Time Left:' + str(time))
        

            timeLabel.after(1000, countdown)

        elif time == 0:

            bu = Button(root, text = "Exit",font=('italic', 10), command = exit_scn)
            bu.place(x = 400, y = 370)

            br = Button(root ,text = "Restart Game", command = restart)
            br.place(x =100, y = 370)

            # highscore()


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
     





def cgprgsplay():
    import time
    l = Label(scn , text="Loading...Please Wait.......", font=('Helvetica',10))
    l.place(x = 97 , y = 200)
    for i in range(0, 11):
        prgs['value'] = 10*i
        prgs.update_idletasks()
        time.sleep(0.5)
        if prgs['value'] == 100:
            ColourGame()
    prgs.pack()

def tttprgsplay():
    import time
    l = Label(scn , text="Loading...Please Wait.......", font=('Helvetica',10))
    l.place(x = 97 , y = 200)
    for i in range(0, 11):
        prgs['value'] = 10*i
        prgs.update_idletasks()
        time.sleep(0.5)
        if prgs['value'] == 100:
            l.destroy()
            TTT()
    prgs.pack()


if __name__=='__main__':
    scn = Tk()
    scn.resizable(0,0)
    scn.title('Mini Project')
    scn.geometry('300x400')

    lab = Label(scn , text = "Click on the button to start the game")
    lab.pack(pady = 10)

    prgs = ttk.Progressbar(scn , length = 100, mode='determinate')
    
    btn  = Button(scn , text = 'Colour Game', command=cgprgsplay)
    btn.pack(pady = 10)
    
    btn2 = Button(scn, text = "Tic Tac Toe", command=tttprgsplay)
    btn2.pack(pady = 15)
    
    prgs.pack()
scn.mainloop()

