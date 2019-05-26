'''
REQUIREMENTS
7.	Write a Python program to get the difference between a given number and 17, difference cannot be negative
'''

# print requirements
print("Requirement: a Python program to get the difference between a given number and 17, difference cannot be negative")


# variables used
number = 0
numbDiff = 0
AfterOrBefore = ""


# getting user input
while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Error 01: You have entered an invalid number. (Only whole number allowed)")


# calculating and printing number difference
if number >= 17:
    numbDiff = number - 17
    AfterOrBefore = "after"
else:
    numbDiff = 17 - number
    AfterOrBefore = "before"


print("this number is {x} count(s) {y} 17.".format(x = numbDiff, y = AfterOrBefore))