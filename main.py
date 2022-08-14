__author__ = "mooreallen"

import random

while True:

    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, Paper or Scissors: ").lower()

    if player == computer:
        print("Compter", "choose the", computer)
        print("And you", "choose the", player)
        print("Draw!")

    elif player == "rock":
        if computer == "paper":
            print("Compter", "choose the", computer)
            print("And you", "choose the", player)
            print("Computer Win!")
        if computer == "scissors":
            print("Compter", "choose the", computer)
            print("And you", "choose the", player)
            print("You Win!")

    elif player == "paper":
        if computer == "scissors":
            print("Compter", "choose the", computer)
            print("And you", "choose the", player)
            print("Computer Win!")
        if computer == "rock":
            print("Compter", "choose the", computer)
            print("And you", "choose the", player)
            print("You Win!")

    elif player == "scissors":
        if computer == "rock":
            print("Compter", "choose the", computer)
            print("And you", "choose the", player)
            print("Computer Win!")
        if computer == "paper":
            print("Compter", "choose the", computer)
            print("And you", "choose the", player)
            print("You Win!")