#Tuples are a collection of ordered and immutable elements.
#Each Element in a tuple is called an item or component.
#Reassigning a value will cause a TypeError
#Examples:
characters =("Hu Tao", "Ganyu", "Scaramouche")
print(characters[0])

#Tuples can also be created without their parantheses= ():
new_characters = "Hu Tao", "Ganyu", "Scaramouche"
print(new_characters)
#Empty tuple:
emplty_tuple = ()


#Overall diffrences between Tuples and Lists:
# 1)    Tuple has fixed order (cannot be changed)
#       Lists can be changed
# 2)    Tuples are immutable, Elements cannot be changed once created
#       Lists are mutable, meaning elements can be added, removed or modified
# 3)    Tuples use () (or none)
#       Lists use [] 
# 4)    Tuples can contain elements of different data types (Heterogeneity)
#       Lists contain elements of the same data type 
# 5)    Tuples are used for grouping related data together
#       Lists are used for more genereal collections of data that are changeable
