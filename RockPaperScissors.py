from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Rock Paper Scissors')
root.configure(bg='light blue')
root.geometry('650x400')

label1 = Label(root, text="Hey, user! Welcome to Rock Paper Scissors!", bg='light blue', font=("Arial", 16))
label1.place(relx=0.5, y=150, anchor=CENTER)
label2 = Label(root, text="Can you beat the computer?", bg='light blue', font=("Arial", 12))
label2.place(relx=0.5, y=190, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to play Rock Paper Scissors?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text="Let's get started!", command=msg, bg='brown', fg='white')
button1.place(x=260, y=250)

def topwin():
    top = Toplevel()
    top.title("Rock Paper Scissors")
    top.configure(bg='light grey')
    top.geometry('600x450+50+50')

    score_player = 0
    score_computer = 0

    label = Label(top, text="Choose Rock, Paper, or Scissors!", bg='light grey', font=("Arial", 14))
    label.place(x=170, y=40)
    result = Label(top, text="Make your choice!", bg='light grey', font=("Arial", 13))
    result.place(x=210, y=180)

    score = Label(top, text="Player: 0     Computer: 0", bg='light grey', font=("Arial", 12))
    score.place(x=210, y=230)

    choices = ["Rock", "Paper", "Scissors"]

    def play(player_choice):
        nonlocal score_player, score_computer
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            message = "It's a tie!"
        elif ((player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Paper" and computer_choice == "Rock") or 
              (player_choice == "Scissors" and computer_choice == "Paper")):
            score_player += 1
            message = "You win!"
        else:
            score_computer += 1
            message = "Computer wins!"

        result.config(text="You chose: " + player_choice + "\nComputer chose: " + computer_choice + "\n\n" + message)

        score.config(text="Player: " + str(score_player) +"     Computer: " + str(score_computer))

    button_rock = Button(top,text="Rock", command=lambda: play("Rock"), bg='brown', fg='white', width=12)
    button_paper = Button(top, text="Paper", command=lambda: play("Paper"), bg='white', fg='black', width=12)
    button_scissors = Button(top, text="Scissors", command=lambda: play("Scissors"), bg='grey', fg='white', width=12)

    button_rock.place(x=90, y=120)
    button_paper.place(x=240, y=120)
    button_scissors.place(x=390, y=120)

root.mainloop()