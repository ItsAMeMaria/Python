import random
import os

def preparegame():
    guesses= []
    fails = 0
    lines = open('hangmanWords.txt').read().splitlines()
    word = random.choice(lines).upper()
    return word, guesses, fails

def playGame():
    os.system('cls')
    print("╦ ╦┌─┐┌┐┌┌─┐┌┬┐┌─┐┌┐┌")
    print("╠═╣├─┤││││ ┬│││├─┤│││")
    print("╩ ╩┴ ┴┘└┘└─┘┴ ┴┴ ┴┘└┘")
    print("A Genshin Impact recipe hangman.")
    play_game = True
    word, guesses, fails = preparegame()
    while play_game:
        while fails < 7:
            for letter in word:
                if letter in guesses:
                    print(letter, end=" ")       
                elif " " in letter:
                    print(" ", end=" ")
                    guesses.append(" ")
                elif "-" in letter:
                    print("-", end=" ")
                    guesses.append("-")
                elif "'" in letter:
                    print("'", end=" ")
                    guesses.append("'")
                else:    
                    print("_", end=" ")
            print()
            guess = input("Guess a letter: ").upper()

            if guess in guesses:
                os.system('cls')
                print("Already guessed letter.")
                continue

            guesses.append(guess)

            if guess in word:
                print("Correct :D")
            else:
                fails += 1
                drawHangman(fails)
#Game won      
            if set(word) <= set(guesses):
                print("Congratulations, you guessed the word!", word)
                playAgain()
#Game over
            if fails == 7:
                print("GAME OVER, the word was: ", word)
                fails = 0
                playAgain()
               

def drawHangman(fails):
    #Hangman by chrishorton: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c 
    if fails == 1:
        os.system('cls')
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    if fails == 2:
        os.system('cls')
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    if fails == 3:
        os.system('cls')
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("=========")
    if fails == 4:
        os.system('cls')
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("=========")
    if fails == 5:
        os.system('cls')
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("      |")
        print("=========")
    if fails == 6:
        os.system('cls')
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("      |")
        print("=========")
    if fails == 7:
        os.system('cls')
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("      |")
        print("=========")

def playAgain():
    while True:
        play_again = input("Do you want to play again? (yes or no):")
        if play_again == "yes":
            os.system('cls')
            playGame()
        elif play_again == "no":
            os.system('cls')
            miniGame()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def miniGame():
    import miniGames
    miniGames.startmenu()

playGame()
