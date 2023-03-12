print(" _, _ __, __,  _,   ___  _,   _, _ __,")
print(" |\/| |_) |_) (_     |  / \   |\/| |_)")
print(" |  | |_) |   , )    |  \ /   |  | |_)")
print(" ~  ~ ~   ~    ~     ~   ~    ~  ~ ~  ")

    

while True:
    try:
        mbps = float(input("Mbps: "))
        calc = mbps * 0.125
        print("Mbps in MB is: " + str(calc))
    except:
        print("Please type a valid number.")
    try:
        again = input("Would you like to calculate again? Yes or No: ")
        if again == "No" or again == "no":
            print("ok")
            break
    except:
        print("Type either Yes or No.")
 
#What I learnt:
#-------------------#-------------------#-------------------#
#while True with an break.
#So that only when no or No is typed in that it would stop.
#Basicaly you can put anything for yes.