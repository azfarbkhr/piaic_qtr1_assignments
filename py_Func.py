'''
REQUIREMENTS
3.	Write a Python function to check whether a number is completely divisible by another number. Accept two integer values form the user
'''

print("Requirements of the program")
print("Write a Python function to check whether a number is completely divisible by another number. Accept two integer values form the user.")

while True:
    try:
        number1 = int(input("Please enter a value for numerator: "))
        number2 = int(input("Please enter a value for denominator: "))
        break
    except ValueError:
        print("Error 01: You have entered an invalid number.")
