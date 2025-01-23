import random

def main():
    
    myScore = 0
    computerScore = 0

    while myScore < 3 and computerScore < 3:

        userPick = input("rock, paper scissors: ")
        computerPick = random.choice(["rock", "paper", "scissors"])

        if userPick == computerPick:
            print("even")
        elif (userPick == "rock" and computerPick == "scissors") or (userPick == "paper" and computerPick == "rock") or (userPick == "scissors" and computerPick == "paper"):
            myScore += 1
            print("You won")
        else:
            computerScore += 1
            print("Computer won")
    
    if myScore == 3:
        print("You won the game!")
    else:
        print("Computer won the game!")


main()