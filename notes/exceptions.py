#From Sololearn lesson: https://www.sololearn.com/learning/1073/2440/5038/1
#Some other possible excceptions:
# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type, but with an inappropriate value. 

#-------------------------------------------------------------------------------------------------------------
#This doc is based on the sololearn lessons: exption and exception handling in Python:
#https://www.sololearn.com/learning/1073/2441/5040/2 

try:
  meaning = 42
  print(meaning / 0)
  #Because meaning is divded by zero, the line "the meaning of life" will be skipped/ignored. 
  # The right excception will be printed.
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")

#-------------------------------------------------------------------------------------------------------------
#From Sololearn lesson: https://www.sololearn.com/learning/1073/2441/5041/1

#The input will be of course a String
print("Enter a number to create your pin:", end="")
pin = input()

try:
    #int() converts a String into an integer
	int(pin)
	print("PIN code is created")	
except ValueError:
	print("Please enter a number")

#-------------------------------------------------------------------------------------------------------------
#From Sololearn lesson: https://www.sololearn.com/learning/1073/2442/5043/1

#The list with the diffrent types of coffees
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]
#declare user input
choice = int(input())

try:
    #We will print the list here by writing coffe and the square brackets [] to indicate that it is a list we need 
    #to display.
    #choice is being put inside the brackets, so that the user iinput can be used as the index.
	print(coffee[choice])
except:
    #an exception occurs, when the user input does not match the amount of coffee types in the list
	print("Invalid number")
#Prints the statement anyway.
finally:
	print("Have a good day")

#-------------------------------------------------------------------------------------------------------------
#From Sololearn lesson: https://www.sololearn.com/learning/1073/2443/5045/2
#Raising Exceptions

num = input("Type any number:")
try:
  #This line checks if the number is less than 0. If it is, then it raises a ValueError with a message.
  if float(num) < 0:
    raise ValueError("Negative!")
  #If its not below zero, it will print "hi"
  else:
    print("hi")
except TypeError:
  print("Inavlid input, please type a valid number")


