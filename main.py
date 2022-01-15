from calendar import c
from random import randint

input("Press 'enter' to start...")

while True:
    rps = input("(r)Rock, (p)Paper, or (s)Scissors? ").lower()

    computer = randint(1, 3)
    crps = ""

    if computer == 1:
        crps = "rock"
    elif computer == 2:
        crps = "paper"
    elif computer == 3:
        crps = "scissors"
    
    if rps == "r" and crps == "rock":
        print("Tie!")
    elif rps == "p" and crps == "p":
        print("Tie!")
    elif rps == "s" and crps == "s":
        print("Tie!")

    if rps == "r" and crps == "paper":
        print("Computer wins!")
    elif rps == "r" and crps == "scissors":
        print("You win!")
    elif rps == "p" and crps == "scissors":
        print("You win!")
    elif rps == "p" and crps == "rock":
        print("Computer wins!")
    elif rps == "s" and crps == "scissors":
        print("Computer wins!")
    elif rps == "s" and crps == "paper":
        print("You win!")
    elif rps == "quit":
        break

    #we are now done!
