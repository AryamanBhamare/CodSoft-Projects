import random

print("Welcome to Game of Rock-Paper-Scissors")
options = ("rock","paper","scissors")

running = True


while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors):")

    print(f"Player:{player}")
    print(f"Computer:{computer} ")

    if player == computer:
        print("It's a Tie Whoops!")
    elif player == "rock" and computer == "scissors":
        print("Congrats You win ")
    elif player == "paper" and computer == "rock":
        print("Congrats You win ")
    elif player == "scissors" and computer == "paper":
        print("Congrats You win ")
    else:
        print("You Lose Better Luck Next Time")

    play_again = input("play again? (y/n)").lower()
    if not play_again == "y":
        running = False

print("Thanks For Playing ")
