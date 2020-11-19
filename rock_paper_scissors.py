'''
Anas Albedaiwi
albedaiwi1994@gmail.com
'''
import random
user = input("Choose one from the options [rock, paper, scissors]: ")
list = ["rock","paper","scissors"]
computer = random.choice(list)
if user in list:
    print("Your Choice: " + user)
    print("computer Choice: " + computer)
    if user == computer:
        print("You and computer chooses same option.")
    elif user == "scissors" and computer == "rock":
        print(" You loose and computer won ")
    elif user == "scissors" and computer == "paper":
        print("You won and computer loose")
    elif user == "rock" and computer == "scissors":
        print("You won and computer loose")
    elif user == "rock" and computer == "paper":
        print("you loose")
    elif user == "paper" and computer == "scissors":
        print("You loose and computer won")
    else:
        print("You loose and computer won")
