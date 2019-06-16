'''
Requirement
21.	Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

# variables used
days = 0 
hours = 0 
minutes = 0
seconds = 0


# constants 
seconds_in_day = 86400 
seconds_in_hour = 3600
seconds_in_minute =  60

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
print("time in days: " + str(second_to_days(second)))
print("time in hours: " + str(second_to_hours(second)))
print("time in minutes: " + str(second_to_minutes(second)))


if second >= seconds_in_day:
    days = second // seconds_in_day
    second = second - (days * seconds_in_day)
if second >= seconds_in_hour:
    hours = second // seconds_in_hour
    second = second - (hours * seconds_in_hour)
if second >= seconds_in_minute:
    minutes = second // seconds_in_minute
    second = second - (minutes * seconds_in_minute)


print("this is equivalent to {days} day(s), {hours} hour(s), {minutes} minutes(s) and {second} second(s)".format(
    days = days,
    hours = hours, 
    minutes = minutes,
    second = second
))