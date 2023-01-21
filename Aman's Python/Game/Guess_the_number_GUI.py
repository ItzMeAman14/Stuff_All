import tkinter as tk
import random

window = tk.Tk()

window.title('Guessing Game')

lblInst = tk.Label(window , text = 'Guess a number from 0 to 9')
lblLine0 = tk.Label(window , text = '************************************************')
lblNoGuess = tk.Label(window , text = "No of Guesses: 0")
lblMaxGuess = tk.Label(window , text = "Max Guess: 3")
lblLine1 = tk.Label(window , text = "************************************************")
lblLogs = tk.Label(window , text = "Game Logs")
lblLine2 = tk.Label(window , text = "************************************************")

buttons = []
for index in range(0 , 10):
    button = tk.Button(window, text = index,command=lambda index=index: process(index), state=tk.DISABLED)
    buttons.append(button)

btnStartGameList = []

for index in range(0 ,1):
    btnStartGame = tk.Button(window ,text = 'Start Game', command=lambda :startgame(index))
    btnStartGameList.append(btnStartGame)


lblInst.grid(row = 0, column = 0 , columnspan=5)
lblLine0.grid(row = 1, column = 0 , columnspan=5)
lblNoGuess.grid(row = 2, column = 0 , columnspan=3)
lblMaxGuess.grid(row = 2, column = 3 , columnspan=2)
lblLine1.grid(row = 3, column = 0 , columnspan=5)
lblLogs.grid(row = 4, column = 0 , columnspan=5)

lblLine2.grid(row = 9, column = 0 , columnspan=5)

for row in range(0, 2):
    for col in range(0 , 5):
        i = row * 5 + col
        buttons[i].grid(row= row+10, column = col)

btnStartGameList[0].grid(row = 13, column = 0 , columnspan = 5)

#Main Game Logic

guess = 0
totalNoOfGuesses = 0
secretnumber = random.randrange(10)
print(secretnumber)
lblLogs = []
guess_row  = 4

#reset all variable
def init():
    global buttons , guess , totalNoOfGuesses, secretnumber , lblNoGuess , lblLogs , guess_row
    guess = 0
    totalNoOfGuesses = 0
    secretnumber = random.randrange(10)
    print(secretnumber)
    lblNoGuess['text'] = "Number of Guesses: 0"
    guess_row = 4

#remove all logs on init
for lblLog in lblLogs:
    lblLog.grid_forget()

lblLogs = []

def process(i):
    global totalNoOfGuesses, buttons , guess_row
    guess = i

    totalNoOfGuesses +=1
    lblNoGuess['text'] = "Number of Guesses:" + str(totalNoOfGuesses)


    #check if guess match secrect number
    if guess == secretnumber:
        lbl = tk.Label(window , text = "Your Guess was right.You won!  :)", fg='green' )
        lbl.grid(row = guess_row, column = 0 , columnspan=5)
        lblLogs.append(lbl)
        guess_row +=1


        for b in buttons:
            b['state'] = tk.DISABLED
    else:
        #give player some hints
        if guess > secretnumber:
            lbl = tk.Label(window , text = "Secret Number is less than your current guess :)", fg='red')
            lbl.grid(row = guess_row, column = 0 , columnspan= 5)
            lblLogs.append(lbl)
            guess_row +=1
        else:
            lbl = tk.Label(window , text = "Secret Number is greater than your current guess :)", fg='red')
            lbl.grid(row = guess_row, column = 0 , columnspan= 5)
            lblLogs.append(lbl)
            guess_row +=1

    if totalNoOfGuesses == 3:
        if guess != secretnumber:
            lbl = tk.Label(window, text = "Max Guess reached.You lost!  :)", fg="red")
            lbl.grid(row = guess_row , column = 0, columnspan=5)
            lblLogs.append(lbl)
            guess_row +=1


        for b in buttons:
            b['state'] = tk.DISABLED
        
    buttons[i]['state'] = tk.DISABLED

status  = 'none'

def startgame(i):
    global status
    for b in buttons:
        b['state'] = tk.NORMAL

    if status == 'none':
        status = 'started'
        btnStartGameList[i]['text'] = 'Restart Game'
    else:
        status = 'restarted'
        init()
    print("Game Started")

window.mainloop()