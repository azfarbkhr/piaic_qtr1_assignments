'''
REQUIREMENTS
4.	Write a Python program that accepts an integer (n) and computes the value of (n + nn + nnn)
'''


# list of variables to be used
number = 0
sumOfNumber = 0
tempNumber = str("")
sumExpress = str("")

# print requirements
print("Requirements: ")
print("a Python program that accepts an integer (n) and computes the value of (n + nn + nnn)")


# accept input from user and validate it
while True:
    try:
        number = int(input("Please enter a number (n): "))
        if number <= 0:
            raise ZeroDivisionError
        break
    except ValueError:
        print("Error 01: You have entered an invalid number.")
    except ZeroDivisionError:
        print("Error 02: You have entered a number less than or equal to zero.")


# print n times a number n
for count in range(1, number+1):
    tempNumber = ""
    for i in range(count):
        tempNumber = int(str(tempNumber) + str(number))
    sumExpress = sumExpress + " + " + str(tempNumber)
    sumOfNumber = sumOfNumber + int(tempNumber)

print("the value of expression ({x} ) computes to {y}.".format(x = sumExpress, y = sumOfNumber))
