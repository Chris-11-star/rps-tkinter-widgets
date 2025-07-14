import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="f0f0f0")

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    comp_choice = random.choice(choices)
    result = ""
    if user_choice == comp_choice:
        result = "It's a draw!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    user_label.config(text="You chose: " + user_choice)
    comp_label.config(text="Computer chose: " + comp_choice)
    result_label.config(text=result)

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20), bg="f0f0f0")
title.pack(pady=10)

user_label = tk.Label(root, text="", font=("Arial", 14), bg="f0f0f0")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="", font=("Arial", 14), bg="f0f0f0")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="f0f0f0")
result_label.pack(pady=20)

button_frame = tk.Frame(root, bg="f0f0f0")
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10, pady=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10, pady=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
