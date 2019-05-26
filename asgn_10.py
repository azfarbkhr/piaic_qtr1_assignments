'''
REQUIREMENTS
10.	Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

'''


# variables used
userInput = 0


# get and validate input from user
while True:
    try:
        userInput = int(input("Please enter a number to check if it is even or odd: "))
        break
    except:
        print("Error 01: You have entered an invalid input. only non-negative integers allowed")


# logic to check if num is even or odd
def check_even_num(n):
    if n % 2 == 0:
        return True
    else:
        return False


# print output 
if check_even_num(userInput):
    print("This is an even number.")
else:
    print("This is an odd number")