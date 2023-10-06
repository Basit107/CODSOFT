import random, tkinter
from tkinter import *
from tkinter import ttk
from random import randint

root = tkinter.Tk()
root.title("Rock Paper Scissors game")
root.config(bg="#229B2D")

app_width = 450
app_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (app_width/2))
y = int((screen_height/2) - (app_height/2))

root.geometry(f"{app_width}x{app_height}+{x-34}+{y-20}")

list_frame = tkinter.Frame(root)
list_frame.pack()

options = ["rock", "paper", "scissors"]
player_win_count = 0
computer_win_count = 0

# Functions for buttons
def start_game():
    global player_win_count, computer_win_count

    play_game_button.configure(state=NORMAL)
    user_choice.configure(state=NORMAL)
    result.configure(text="\t\t\t\n\t\n\n")
    player_win_count = 0
    computer_win_count = 0

    score_track.configure(text="Computer   vs   Player\n {} \t \t {}".format(computer_win_count, player_win_count))

def play_game():
    comp_choice = random.randint(0, 2)
    global player_win_count, computer_win_count

    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2

    if user_choice_value == 0: #Rock
        if comp_choice == 0:
            result.configure(text="You picked:  rock \n Computer picked:     rock \n\n Its a Tie...")
        elif comp_choice == 1:
            result.configure(text="You picked:  rock \n Computer picked: Paper \n\n Computer Wins!!")
            computer_win_count += 1
            score_track.configure(text="Computer   vs   Player\n {} \t    \t{}".format(computer_win_count, player_win_count))
        elif comp_choice == 2:
            result.configure(text="You picked:  rock \n Computer picked: Scissors \n\n You Win!!")
            player_win_count += 1
            score_track.configure(text="Computer   vs   Player\n {} \t    \t{}".format(computer_win_count, player_win_count))

    if user_choice_value == 1: #Paper
        if comp_choice == 0:
            result.configure(text="You picked: Paper \n Computer picked:    rock \n\n You Win!!")
            player_win_count += 1
            score_track.configure(text="Computer   vs   Player\n {} \t    \t{}".format(computer_win_count, player_win_count))
        elif comp_choice == 1:
            result.configure(text="You picked: Paper \n Computer picked: Paper \n\n Its a Tie...")
        elif comp_choice == 2:
            result.configure(text="You picked: Paper \n Computer picked: Scissors \n\n Computer Wins!!")
            computer_win_count += 1
            score_track.configure(text="Computer   vs   Player\n {} \t    \t{}".format(computer_win_count, player_win_count))
    
    if user_choice_value == 2: #Scissors
        if comp_choice == 0:
            result.configure(text="You picked: Scissors \n Computer picked:     rock \n\n Computer Wins!!")
            computer_win_count += 1
            score_track.configure(text="Computer   vs   Player\n {} \t    \t{}".format(computer_win_count, player_win_count))
        elif comp_choice == 1:
            result.configure(text="You picked: Scissors \n Computer picked: Paper \n\n You Win!!")
            player_win_count += 1
            score_track.configure(text="Computer   vs   Player\n {} \t    \t{}".format(computer_win_count, player_win_count))
        elif comp_choice == 2:
            result.configure(text="You picked: Scissors \n Computer picked: Scissors \n\n Its a Tie...")

#  GUI starts from here
title = tkinter.Label(root,text="Welcome Player, to\n Rock Paper Scissors Game \n Press New game to play ",font=("Candara",24, "bold"),fg="White", bg="#229B2D", highlightbackground="black")
title.pack(padx=3, pady=3)

score = tkinter.Label(root, text="SCORE:", font=("hp Simplified", 20, "bold"), foreground="Blue", background="#229B2D", justify=CENTER)
score.pack(pady=24)

score_track = tkinter.Label(root, text="Computer   vs   Player\n 0 \t  0", font=("hp Simplified",18, "bold"), foreground="black", background="white", justify=CENTER)
score_track.pack(side=tkinter.TOP)

user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"), font=("hp Simplified",16), width=20, state=DISABLED)
user_choice.current(0)
user_choice.pack()

new_game_button = tkinter.Button(root, text="New Game", font=("arial", 13, "bold"), fg="white", background="red", command=start_game)
new_game_button.pack(side=tkinter.RIGHT, pady=15)

play_game_button = tkinter.Button(root, text="Play Game", font=("arial", 13, "bold"), fg='white', background="blue", state=DISABLED, command=play_game)
play_game_button.pack(side=tkinter.RIGHT, pady=50)

result = tkinter.Label(root, text="\t\t\t\n\t\n\n", font=("hp Simplified",16, "bold"), background="white")
result.pack(pady=53)

# Places for widgets and buttons
user_choice.place(x=100, y=310)
play_game_button.place(x=175, y=360)
result.place(x=98, y=410)
new_game_button.place(x=175, y=540)

root.mainloop()
