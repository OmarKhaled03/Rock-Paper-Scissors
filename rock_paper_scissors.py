import math
import random
from enum import Enum

class Choices(Enum):
    rock = 1
    paper = 2
    scissors = 3

def player_choice():
    question = input("Rock, Paper or Scissors? ")
    player_choice.choice = question.lower()

    if (player_choice.choice in Choices.__members__):
        print("You chose: " + player_choice.choice.lower())
    else:
        print("Uhh that doesn't sound right...")
        player_choice()

def computer_choice():
    computer_choice.choice = random.choice(list(Choices))
    print("The computer chose: " + computer_choice.choice.name)

def winner():
    player_choice()
    computer_choice()

    winner_cases = {
        0: player_choice.choice == computer_choice.choice.name,
        1: player_choice.choice == "rock" and computer_choice.choice.name == "paper",
        2: player_choice.choice == "paper" and computer_choice.choice.name == "rock",
        3: player_choice.choice == "scissors" and computer_choice.choice.name == "rock",
        4: player_choice.choice == "rock" and computer_choice.choice.name == "scissors",
        5: player_choice.choice == "paper" and computer_choice.choice.name == "scissors",
        6: player_choice.choice == "scissors" and computer_choice.choice.name == "paper"
    }

    if(winner_cases[0]):
        print("It's a tie! Play again? (Please type in Yes or No)")

    elif(winner_cases[1] or winner_cases[3] or winner_cases[5]):
        print('Computer wins :( Try again?')

    elif(winner_cases[2] or winner_cases[4] or winner_cases[6]):
        print('You win! Play Again?')

    else:
        print("Uhh that doesn't sound right...")
        winner()

    play_again()

def play_again():
    decision = input().lower()
    if(decision == "yes"):
        winner()
    elif(decision == "no"):
        exit
    else:
        print("Uhh that doesn't sound right... Play again?")
        play_again()

winner()
