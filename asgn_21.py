'''
Requirement
21.	Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

# variables used
days = 0 
hours = 0 
minutes = 0
seconds = 0

# get user input
while True:
    try:
        second = int(input("Please enter a time taken in seconds: "))
        break
    except:
        print("Error 01: You have entered an invalid input.")


# logic to convert
# day to seconds
def second_to_days(seconds):
    return round(seconds / 60 / 60 / 24, 4)

# hour to seconds
def second_to_hours(seconds):
    return round(seconds / 60 / 60, 2)

# minutes to seconds
def second_to_minutes(seconds):
    return round(seconds / 60, 2)

# print output 
print("time in days: " + str(second_to_days(days)))