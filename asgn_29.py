'''
Requirements
29.	Write a program to convert Hexadecimal number to Decimal number
''' 

# variabled used
hexaDecimalNum = "23F"


# logic to convert
def hexaDecimal_to_decimal (temp):
    decimalNum = 0
    hexDigits = "0123456789ABCDEF"

    for i in range(len(temp)):
        digit = temp[-i-1].upper()
        digitValueInDecimal = hexDigits.index(digit)
        decimalNum = decimalNum + ( digitValueInDecimal * (16 ** int(i)))

    return decimalNum


# print output
print("the hexdecimal value of {x} is equal to {y} in decimal.".format(x = hexaDecimalNum, y = hexaDecimal_to_decimal(hexaDecimalNum)))