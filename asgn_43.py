'''
Requirement
43.	Write a Python program to construct the following pattern, using a nested loop number. 
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''

# variables used
length = 10

# logic 
for i in range(length):
    for j in range(1, i + 1):
        print(i, end = " ")
    print("")