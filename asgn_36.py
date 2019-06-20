'''
Requirement
36.	Write a program to check whether given input is palindrome or not
'''



# variables used
inputText = "radar"


# logic used
def is_Palindrome (text):
    reversedtext = ""
    for i in reversed(text):
        reversedtext += i
    
    if reversedtext == text:
        return True


# print output
if is_Palindrome(inputText):
    print("Yes, {x} is palindrome string.".format(x = inputText))
else:
    print("No, {x} is not a palindrome string.".format(x = inputText))