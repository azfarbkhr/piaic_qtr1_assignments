'''
Requirement
11.	Write a Python program to test whether a passed letter is a vowel or not
'''

# variables used
userInput = ""
vowels = ["a", "e", "i", "o", "u"]

# get user input
while True:
    try:
        userInput = input("Please enter a valid vowel: ")
        if len(userInput) != 1:
            raise ValueError
        if not userInput.isalpha():
            raise ValueError
        break
    except:
        print("Error 01: You have entered an invalid input. The input should be a single character from english alphabets.")

# logic to check vowels
def check_vowel(alphabet):
    for i in vowels:
        if alphabet.lower() == i:
            return True
    return False

# print output
if check_vowel(userInput):
    print("Yes, this is a vowel.")
else:
    print("No, this is not a vowel.")