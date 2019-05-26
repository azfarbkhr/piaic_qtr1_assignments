'''
REQUIREMENTS
3.	Write a Python function to check whether a number is completely divisible by another number. Accept two integer values form the user
'''

print("Requirements of the program:")
print("Write a Python function to check whether a number is completely divisible by another number. Accept two integer values form the user.")

inputValues = {"number1": 0, "number2": 0}


for i in inputValues:
    while True:
        try:
            inputValues[i] = int(input("Please enter a number: "))
            if inputValues[i] == 0:
                raise ZeroDivisionError
            break
        except ZeroDivisionError:
            print("Error 02: You have entered second number as zero and nothing is divisible by zero.")
        except:
            print("Error 01: You have entered an invalid number.")



def isDivisible(a, b):
    try:
        if inputValues["number1"] % inputValues["number2"] > 0:
            return False
        else:
            return True
    except ZeroDivisionError:
        return False


if isDivisible(inputValues["number1"], inputValues["number2"]):
    print("The first number is completely divisible by the second number.")
else:
    print("The first number is not completely divisible by the second number.")

