#With this simple code I can check if the file can be found or not.
#helps if an error like "File not found" occurs.
import os

if os.path.exists("notes/files/txtfile.txt"):
    print("File exists")
else:
    print("File not found")


#--------------------------------------------------------------------------------------
#Files
#Before you can edit a file, you have to open it.
#with open() you can open the file. 
#there are modes for opening a file:
    #write mode => "w"
    #read mode => "r"
    #binary write mode => "wb"
    #binary read mode => "rb"
#--------------------------------------------------------------------------------------
#See file_read and file_write before continuing with this file.
#--------------------------------------------------------------------------------------
#"try and finally" with files
try:
    txtfile = open("notes/files/txtfile.txt", "r")
    print(txtfile.read())
finally:
    txtfile.close()
#It's important to close a file when working with files
#The "finally" block ensurers that the file is closed after a "try" block
#Even if the "try" block might raise an exception / Error, the "finally" block will always be executed.
#--------------------------------------------------------------------------------------
#The with statement
#The with statement opens a file and automatically closes it after the intended codeblock is executed.
#It's the same with Finally. When an error/exception occurrs, the with statemnt will always be executed.
with open("notes/files/txtfile.txt", "r") as txtfile:
    print(txtfile.read())
#--------------------------------------------------------------------------------------