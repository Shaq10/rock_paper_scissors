'''
This program is a game of rock, paper, scissors between the user and computer
'''

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"] #list storing different options

#possible messages depending on the outcome
message = {
  "tie": "Yawn it's a tie!",
  "won": "Yay you won!",
  "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
    
    #user and computer choices are displayed to the user
    print ("The user has chose: %s" % user_choice)
    print ("The computer has chose: %s" % computer_choice)
    
    #outcome of two choices determines the message output
    if user_choice == computer_choice:
        print (message["tie"])
    elif user_choice == options[0] and computer_choice == options[2]:
        print (message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print (message["won"])
    elif user_choice == options[2] and computer_choice == options[1]:
        print (message["won"])
    else:
        print (message["lost"])

def play_RPS():
    user_choice = input("Enter Rock, Paper or Scissors: ") #user prompted for choice
    user_choice = user_choice.upper()
    computer_choice = options[randint(0,2)] #computer choice randomly chosen
    decide_winner(user_choice, computer_choice)

play_RPS() #call to play game