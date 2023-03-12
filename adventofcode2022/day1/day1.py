#part one------------------------------------------------------------------
with open("adventofcode2022\day1\input.txt", "r") as inputFile:
    elf_sum = 0
    #Empty list to store the sum of each elf
    elves_sums = []
    for line in inputFile:
        calories = line.strip()
        if calories != '':
            elf_sum += int(calories)
        else:
            #if there is an empty line then, the sum of the elf, will be stored
            #at the end of our elves list.
            elves_sums.append(elf_sum)
            #the sum of the elf will be set to 0, to show that we are calculating the sum of the next elf
            elf_sum = 0
    #find the maximum of the elves list
    print(max(elves_sums))

#part two------------------------------------------------------------------
    #Reveres = True means, that the list should be sorted in descending order.
    #[:3] is grabbing the first three elements of the list
    #and those three elements are here summed together.
    max_elves_sums = sorted(elves_sums, reverse = True)[:3]
    print(sum(max_elves_sums))

            


