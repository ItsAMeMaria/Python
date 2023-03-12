from list_sentences import list
import random

sentence = random.choice(list)

def replaceSmth(smth):
    smth = sentence.replace(" ", "")
    return(smth)
print(replaceSmth(sentence))

def replace_letter(smth):
    smth = sentence.replace("d", "MAAAAAAAAAAA")
    return(smth)
print(replace_letter(sentence))