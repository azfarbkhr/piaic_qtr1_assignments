'''
Requirements
28.	Write a program to convert Octal number to Decimal number
''' 

# variabled used
octalNum = 345

# logic to convert
def octal_to_decimal (number):
    decimalNum = 0
    temp = str(number)      # store num as a string variable so that we can iterate over its each digit
    index = 0               # this is an index of the position at which we stand when iterating over our number
    for i in reversed(temp):
        decimalNum = decimalNum + (int(i) * (8 ** index))
        index += 1
    return decimalNum


# print output
print("the octal value of {x} is equal to {y} in decimal.".format(x = octalNum, y = octal_to_decimal(octalNum)))