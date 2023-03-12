#playerone:         playertwo:
#A = Rock           Y = Paper
#B = Paper          X = Rock
#C = Scissors       Z = Scissors


with open("adventofcode2022\day2\input.txt", "r") as inputFile:
    player_one = []
    player_two = []
    for line in inputFile:
        parting = line.strip().split(' ')
        player_one.append(parting[0])
        player_two.append(parting[1])

    if(player_one == "A" and player_two == "X"):
        print("tie")


