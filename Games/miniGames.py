import os

def startmenu():
    os.system('cls')
    print("███    ███ ██ ███    ██ ██      ██████   █████  ███    ███ ███████ ███████ ")
    print("████  ████ ██ ████   ██ ██     ██       ██   ██ ████  ████ ██      ██      ")
    print("██ ████ ██ ██ ██ ██  ██ ██     ██   ███ ███████ ██ ████ ██ █████   ███████ ")
    print("██  ██  ██ ██ ██  ██ ██ ██     ██    ██ ██   ██ ██  ██  ██ ██           ██ ")
    print("██      ██ ██ ██   ████ ██      ██████  ██   ██ ██      ██ ███████ ███████ ")

    print("Welcome to Mini Games")
    print("Here are the available Mini Games you can choose from:")
    print("| For Number Guesser choose 1")
    print("| For Hangman choose 2")
    print("| For Roll the Dice choose 3")
    print("| For Rock Paper Scissors choose 4")
    print("To Leave Mini Games type 5")
    game = int(input("Choose a minigame: "))
    if game == 1:
        numberGuesser()
    elif game == 2:
        hangman()
    elif game == 3:
        rollTheDice()
    elif game == 4:
        rockPaperScissors()
    elif game == 5:
        exit()
    else:
        print("type in a number")

def numberGuesser():
    import numberGuesser
    numberGuesser.playGame()

def hangman():
    import hangman
    hangman.playGame()

def rollTheDice():
    import rollthedice
    rollthedice.playGame()

def rockPaperScissors():
    import rock_paper_scissors
    rock_paper_scissors.playGame()

startmenu()
    

