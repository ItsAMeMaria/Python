#Python Copy

y = [1,2,4,5]

x = y.copy()

print(y is x)
#The is keyword is used to test if two variables refer to the same object.
#The is keyword will then return either True or False
#
#In this case it will return False, becuase y and x refer to two diffrent objects.
#y and x might have the same contents, but by using copy(), x is asigned a newly created list object.