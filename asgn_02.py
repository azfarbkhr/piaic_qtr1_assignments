'''
Requirements
2.	Write a Python program to check if a number is positive, negative or zero
'''

while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Error 01: You have entered an invalid number.")

if number > 0:
    print("this is a positive number which is greater than zero")
elif number == 0:
    print("the number is zero")
else:
    print("this is a negative number which is less than zero")