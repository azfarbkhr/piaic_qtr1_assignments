'''
Requirement
41.	Write a Python program to construct the following pattern, using a nested for loop
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''

# variables used
length = 10


# logic 
for i in range(length):
    for j in range(i + 1):
        print("*", end = " ")
    print("")
for i in range(length - 1):
    for j in range(length - i -1):
        print("*", end = " ")
    print("")