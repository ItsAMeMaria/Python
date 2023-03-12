import random
import os

def prepareGame():
    min = 1
    max = 100
    computer = random.randint(min, max)
    attempts = 10
    return computer, attempts

def playGame():
    os.system('cls')
    print(" _  _ __  __ __  __ ____ ____ ____     ___ __  __ ____ ___ ___ ____ ____   ")
    print("( \( (  )(  (  \/  (  _ ( ___(  _ \   / __(  )(  ( ___/ __/ __( ___(  _ \  ")
    print(" )  ( )(__)( )    ( ) _ <)__) )   /  ( (_-.)(__)( )__)\__ \__ \)__) )   /  ")
    print("(_)\_(______(_/\/\_(____(____(_)\_)   \___(______(____(___(___(____(_)\_) ")
    play_game = True
    computer, attempts = prepareGame()
    while play_game:
        try:
            guess = int(input("Guess the number: "))
            attempts -= 1
            if(guess > computer):
                os.system('cls')
                print("You guessed too much. Number of attempts left: " + str(attempts))
            elif(guess < computer):
                os.system('cls')
                print("You have to guess more. Number of attempts left: " + str(attempts))
            else:
                os.system('cls')
                print("You got the right number! it is:" + str(computer))
                print("number of attempts left: " + str(attempts))
                print("------------------------------------------")
                print("Thanks for playing")
                playAgain()
                
            if attempts == 0:
                os.system('cls')
                print("You used all your attempts :(")
                print("The number was: " + str(computer))
                playAgain()
        except:
            print("Please type in a number.")

def miniGame():
    import miniGames
    miniGames.startmenu()

def playAgain():
    while True:
        play_again = input("Do you want to play again? (yes or no):")
        if play_again == "yes":
            playGame()
        elif play_again == "no":
            miniGame()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


playGame()

