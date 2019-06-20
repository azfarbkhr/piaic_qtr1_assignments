'''
Requirement
40.	Write a Python program that accepts a string and calculate the number of digits and letters Sample Data : Python 3.2, Expected Output : Letters 6, Digits 2
'''

# variables used
userInput = "test1231234567890"
alphabetCount = 0
numberCount = 0

# logic used
def count_Char (sentence):
    alphabetCount = 0
    numberCount = 0

    alphabtes = "abcdefghijklmnopqrstuvwxyz"
    digits = "1234567890"
    for i in sentence.lower().replace(" ", ""):     # converting all characters to lower case and then replacing the spaces with blank string to enure that spaces are not counted in non alphabets
        if i in alphabtes:
            alphabetCount += 1
        elif i in digits:
            numberCount += 1

    return {"alphabetCount": alphabetCount , "numberCount": numberCount}

# print output
for k, v in count_Char(userInput).items():
    print(k, " = ", v)