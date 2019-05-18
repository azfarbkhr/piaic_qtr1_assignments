'''
REQUIREMENTS
4.	Write a Python program that accepts an integer (n) and computes the value of (n + nn + nnn)
'''

# list of variables
number = 0


# accept input from user and validate it
while True:
    try:
        number = int(input("Please enter radius of circle: "))
        if number <= 0:
            raise ZeroDivisionError
        break
    except ValueError:
        print("Error 01: You have entered an invalid number.")
    except ZeroDivisionError:
        print("Error 02: You have entered a number less than or equal to zero.")


# print n times a number n 
for n in range(number):
    print(n)