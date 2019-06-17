'''
Requirement
23.	Write a Python program to convert temperatures to and from Celsius, Fahrenheit
'''

# get user input
temperatureInput = input("Please enter temperature to convert (Expected Usage is 28F or 102C): ")

# variables used
temperatureValue = float(temperatureInput[:-1])
temperatureUnit = temperatureInput[-1]

# logic to convert 
def celsious_to_farenheit (temp):
    return round((9 * temp + ( 32 * 5) ) / 5, 2)

def fahrenheit_to_celsious (temp):
    return round((5 * (temp - 32)) / 9, 2)

# print output

if temperatureUnit.lower() == "c":
    print("The temperature {x} celsious is converted to {y} farenheit.".format(
        x = temperatureValue, y = celsious_to_farenheit(temperatureValue)
    ))
elif temperatureUnit.lower() == "f":
    print("The temperature {x} farenheit is converted to {y} celsious.".format(
        x = temperatureValue, y = fahrenheit_to_celsious(temperatureValue)
    ))
else:
    print("You have entered an incorrect temperature unit or unit not exists.")