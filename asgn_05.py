'''
REQUIREMENT
5.	Write a Python program to calculate number of days between two dates
'''

# libraries
import datetime # need this to validate and format date inputs


# variables used
userInput = {"dateFrom": ["date from", "", ""], "dateTo":["date to", "", ""]}
dayDiff = 0


# print requirements
print("Requirements: a program to calculate number of days between two dates")
print("")


# getting user input and validating
for item in userInput:
    while True:
        try:
            userInput[item][1] = input("Please enter '{x}' in format (dd-mm-yyyy): ".format(x = userInput[item][0]))
            day, month, year = map(int, userInput[item][1].split('-'))
            userInput[item][2] = datetime.date(year, month, day)
            break
        except:
            print("Error 01: You have entered an invalid value.")


# calculating and print days difference
if userInput["dateTo"][2] >= userInput["dateFrom"][2]:
    dayDiff = userInput["dateTo"][2] - userInput["dateFrom"][2]
else:
    dayDiff = userInput["dateFrom"][2] - userInput["dateTo"][2]

print("The difference in days from {dateFrom} to {dateTo} is {dayDiff} day(s).".format(dateFrom = userInput["dateFrom"][2], dateTo = userInput["dateTo"][2], dayDiff = dayDiff.days))
