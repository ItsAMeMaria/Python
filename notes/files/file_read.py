txtfile = open("notes/files/txtfile.txt", "r")
#With the read Method it can literally read the file. not that hard
#to read a certain amount of characters of a file, type a number in read.
content = txtfile.read(7)
#With that you can also print the content inside of the file.
print(content)
txtfile.close()


#readlines is used to read each line in a file. An element is a line in the file.
txtfile = open("notes/files/txtfile.txt", "r")
txtfile2 = open("notes/files/txtfile.txt", "r")
content = txtfile.readlines()
print(content)
for line in txtfile2:
    print(line)
txtfile.close()

#readline -> one line at the time. the lines will be shown in the console beaneath eachother
#readliens -> makes a list that looks like this: ['Hello World\n', 'Hello Worl\n', 'Hello Wor']

#But what if you want to get a line with a user input?

txtfile = open("notes/files/txtfile.txt", "r")
n = int(input())
content = txtfile.readlines()
print(content[n])

txtfile.close()