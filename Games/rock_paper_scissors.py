import random
import os

def prepareGame():
    choice =  ["Rock", "Paper", "Scissors"]
    computer = random.choice(choice)
    return choice, computer

def playGame():
    os.system('cls')
    play_game = True
    choice, computer = prepareGame()
    while play_game:
            player = input("Choose one: Rock Paper or Scissors: ")
            if(player == computer):
                print("tie!")
                playAgain()
            elif(player == "Rock"):
                if(computer == "Paper"):
                    print("Game Over! Computer chose " + computer)
                    playAgain()
                else:
                    print("You Won! Computer chose " + computer)
                    playAgain()
            elif(player == "Paper"):
                if(computer == "Scissors"):
                    print("Game Over! Computer chose " + computer)
                    playAgain()
                else:
                    print("You Won! Computer chose " + computer)
                    playAgain()
            elif(player == "Scissors"):
                if(computer == "Rock"):
                    print("Game Over! Computer chose " + computer)
                    playAgain()
                else:
                    print("You Won! Computer chose " + computer)
                    playAgain()
            computer = random.choice(choice)

def miniGame():
    import miniGames
    miniGames.startmenu()

def playAgain():
    while True:
        play_again = input("Do you want to play again? (yes or no):").lower()
        if play_again == "yes":
            playGame()
        elif play_again == "no":
            miniGame()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

playGame()