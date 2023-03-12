#Dictionaries in python are unordered collection of key-value pairs
#(key:value). Each key is unique and are used to access its corresponding value¨.
#The keys can be of any immutable data, while the values can be any data
#(!Immutable objects are objects whose value cannot be changed after creation.)
#Examples:
crochet = {"singleC": 1, "doubleC": 2, "tripleC": 3, "halfdoubleC": 0}

#To print out the data that is stored for instance in "doubleC" from the dictionary "crochet".
print(crochet["doubleC"])

#To change the value of an existing key
crochet["halfdoubleC"] = 2.5
print(crochet)

#To see if a key exists in a dictionary, simply use ... in ... or ... not in ...
print("singleC" in crochet)         #True
print("slipstitch" in crochet)      #False
print("slipstitch" not in crochet)  #True

#Another method to get the value data is with the get method:
print(crochet.get("singleC"))
print(crochet.get("slipstitch"))                #will return "none" by default
print(crochet.get("slipstitch", "not here"))    #can write your custom default