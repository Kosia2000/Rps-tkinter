from tkinter import Tk, Label, Button
from random import choice

available_choices = ["Paper", "Rock", "Scissors"]


def play(player, cpu):
    win = {"Paper": "Rock", "Rock": "Scissors", "Scissors": 'Paper'}
    if player == cpu:
        return None
    elif win[player] == cpu:
        return True
    else:
        return False


def play_computer(player):
    global text_label
    cpu = choice(available_choices)
    is_user_winner = play(player, cpu)
    if is_user_winner is None:
        text_label.config(text="Tie! Try again!", fg="blue")
    elif is_user_winner:
        text_label.config(text="You win. Let's play again!", fg="green")
    else:
        text_label.config(text="I win!", fg="red")


root = Tk()
root.title = ("Rock, paper, scissors")
root.geometry("310x150")

text_label = Label(root, font=40, text="Let's play rock, paper, scissors!")
text_label.pack()

Button(root, text="1. Paper", font=40, width=10,
       command=lambda: play_computer("Paper")).pack()

Button(root, text="2. Rock", font=40, width=10,
       command=lambda: play_computer("Rock")).pack()

Button(root, text="3. Scissors", font=40, width=10,
       command=lambda: play_computer("Scissors")).pack()


root.mainloop()
