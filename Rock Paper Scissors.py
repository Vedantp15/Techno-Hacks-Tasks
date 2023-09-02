import random
import tkinter as tk
from tkinter import messagebox

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "Rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "Rock" else "Computer wins!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

def play_game(user_choice):
    # user_choice.geometry("400x350")
    choices = ["Rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    messagebox.showinfo("Result", message)

def main():
    root = tk.Tk()
    root.title("Rock Paper Scissors Game")
    root.geometry("400x300")
    label = tk.Label(root, text="Choose your move:")
    label.pack()

    choices = ["rock", "paper", "scissors"]
    for choice in choices:
        button = tk.Button(root, text=choice.capitalize(), command=lambda c=choice: play_game(c))
        button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
