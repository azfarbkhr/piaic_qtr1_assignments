'''
Requirement
30.	Write a Python program to count the number occurrence of a specific character in a string
'''

# variables used
character = "a"
sentence = "this is a book"

# business logic 
def count_Char (char, sent):
    countOfChar = 0
    for i in sent:
        if char == i:
            countOfChar += 1
    return countOfChar
        

# print output
print("The count of character '{x}' in sentence '{y}' is {z} counts.".format(
    x = character, 
    y = sentence, 
    z = count_Char(char= character, sent= sentence)
    ))
