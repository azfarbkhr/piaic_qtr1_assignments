'''
REQUIREMENTS
9.	Write a Python program to get a string which is n (non-negative integer) copies of a given string
'''

# variables used
stringToCopy = ""
numberOfCopies = 0


# get and validate input from user
while True:
    try:
        stringToCopy = input("Please enter a string to copy: ")
        break
    except:
        print("Error 01: You have entered an invalid input.")

while True:
    try:
        numberOfCopies = int(input("Please enter the number of copies required for the string: "))
        if numberOfCopies <= 0:
            raise ValueError
        break
    except:
        print("Error 01: You have entered an invalid input. only non-negative integers allowed")

# logic to copy string
def copy_this_String(p_string, n):
    concatString = ""
    for i in range(n):
        concatString = concatString + p_string
    return concatString

# print output 
print(copy_this_String(stringToCopy, numberOfCopies))
