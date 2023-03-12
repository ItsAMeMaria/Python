#from sololearn lesson:
#https://www.sololearn.com/learning/1073/2494/5276/2

def sum(x):
    res = 0
    for i in range(x):
        res += i
    #Have the funtion outside of the loop, so that it doesn't immediately return 0!
    return res

print (sum(10))
#Here is the result 45, because:
#A range always starts with the number 0 as the first position
#res = 0, means 0 is the first defiend number in the range of x (10)
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9
#So the first position is 0 and counting all the other positions to 10, we will get 9 as the last position