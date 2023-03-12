#What is assertions?
#Assertions are statements that asserts or verifies if a certain condition is true or not.
#If the condition = true | Program continues normally
#If the condition = False | AssertionError is raised stopping the program to execute.

x = 5
assert x > 0
print("5 is greater than 0")
#The next print will not be executed, because the assert returns False.
#See console for the AssertionError
#You can write at the end of the assert, your message
assert x > 10, "My ErrorMessage"
print("5 is not greater than 10")