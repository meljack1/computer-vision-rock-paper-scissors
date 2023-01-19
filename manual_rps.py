import random

def get_computer_choice():
    rps_list = ["rock", "paper", "scissors"]
    return random.choice(rps_list)

def get_user_choice():
    user_choice = input("Rock, paper, scissors?")
    return user_choice