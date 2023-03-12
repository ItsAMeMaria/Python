#------------------------------------------------------------------------------------------
#The write method is used to write in the file
#!!!The "w" will create a new file if it doesnt exist or overwrite the existing one!!!
txtfile = open("notes/files/txtfile.txt", "w")
txtfile.write("Y'all already know who I am.")
txtfile.close

txtfile = open("notes/files/txtfile.txt", "r")
print(txtfile.read())
txtfile.close()

