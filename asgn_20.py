'''
Requirement
20.	Write a Python program to convert all units of time into seconds.
'''

# variables used
time = {
    "day": 0,
    "hour": 0,
    "minute": 0,
    "second": 0    
}

# get user input 
for item in time:
    while True:
        try:
            time[item] = int(input("Please enter {x}: ".format(x = item)))
            break
        except:
            print("Error 01: You have entered an invalid value.")

# logic to calculate time
def calculateTimeSeconds(days, hour, minute, second):
    TimeInSeconds = (days * 24 * 60 * 60) + (hour * 60 * 60) + (minute * 60) + (second)
    return TimeInSeconds

# print output
print("the total time in seconds is equal to: " + str(calculateTimeSeconds(time["day"],time["hour"],time["minute"],time["second"])))