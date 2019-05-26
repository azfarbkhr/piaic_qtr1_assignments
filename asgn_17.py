'''
Requirement
17.	Write a Python program to convert height (in feet and inches) to centimetres.
'''

# values used
length_cm = 0
length_ft = 0
length_in = 0


# get user input
while True:
    try:
        length_cm = int(input("Please enter a number in centimeters to convert: "))
        if length_cm < 0:
            raise ValueError
        break
    except:
        print("Error 01: You have entered an invalid input. only non-negative integers allowed")

while True:
    try:
        print("following operations can be performed; 1 - feet to centimeter; 2 - inch to centimeter")
        operation = int(input("Please select an operation id to perform: "))
        if operation != 1 and operation != 2:
            raise ZeroDivisionError
        break
    except ZeroDivisionError:
        print("Error 02: Such operation ID does not exists")
    except:
        print("Error 01: You have entered an invalid input.")


# logic to convert
def ft_to_cm(ft_length):
    return round(ft_length * 30.48, 4)

def in_to_cm(in_lenth):
    return round(in_lenth * 2.54, 4)

# print output
if operation == 1:
    print(ft_to_cm(length_cm))
elif operation == 2:
    print(in_to_cm(length_cm))
