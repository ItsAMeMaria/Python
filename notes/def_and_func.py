#from sololearn lesson:
#https://www.sololearn.com/learning/1073/2437/5023/1 

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y


#func is simply another variable, like x and y
def do(func, x, y):
    return func(x, y)


a  = 10
b = 2

print(do(add, a, b))
print(do(sub, a, b))
print(do(mul, a, b))
print(do(div, a, b))
