'''
Requirement
34.	Input a text and count the occurrences of vowels and consonant 
'''

# variables used
text = "hi my name is azfar"


# logic performed 
def count_Char (sentence):
    countVowels = 0
    countConsonant = 0
    countNonAlphabets = 0
    vowels = "aeiou"
    consonant = "bcdfghjklmnpqrstvwxyz"
    for i in sentence.lower().replace(" ", ""):     # converting all characters to lower case and then replacing the spaces with blank string to enure that spaces are not counted in non alphabets
        if i in vowels:
            countVowels += 1
        elif i in consonant:
            countConsonant += 1
        else:
            countNonAlphabets += 1

    return {"countVowels": countVowels , "countConsonant": countConsonant, "countNonAlphabets": countNonAlphabets}

# print output
for k, v in count_Char(text).items():
    print(k, " = ", v)