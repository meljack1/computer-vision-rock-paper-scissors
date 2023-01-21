import random

def get_computer_choice():
    rps_list = ["Rock", "Paper", "Scissors"]
    return random.choice(rps_list)

def get_prediction():
    return

def get_user_choice():
    user_choice = input("Rock, paper, scissors?")
    return user_choice

def get_winner(computer_choice, user_choice):
    if (computer_choice == user_choice):
        print("It is a tie!") 
    elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
        print("You won!")
    else:
        print("You lost!")

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)
