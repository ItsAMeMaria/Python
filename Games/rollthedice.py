import random;
import os;

def playGame():
    os.system('cls')
    numbers = [1,2,3,4,5,6]
    player = False
    while player == False:
        desicion = input("Do you want to roll the dice? Yes or No? ").lower()
        if(desicion == "yes"):
            print("Rolling . . . " + str(random.choice(numbers)))
        else:
            miniGame()

def miniGame():
    import miniGames
    miniGames.startmenu()

playGame()