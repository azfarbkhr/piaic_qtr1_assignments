'''
REQUIREMENTS
8.	Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged
'''


# print requirements
print("Requirements: a Python program to get a new string from a given string where 'is' has been added to the front. If the given string already begins with 'is' then return the string unchanged")

# variables used
userInput = ""

# getting user input
while True:
    try:
        userInput = input("Please enter a string: ")
        break
    except:
        print("Error 01: You have entered an invalid input.")


# new string function
def addIs(someText):
    lowerSomeText = someText.lower()
    if lowerSomeText[:2] != "is" and len(someText) >= 2:
        return "Is " + someText + "?"
    else:
        return someText


# add is to input and printing it
print(addIs(userInput))
