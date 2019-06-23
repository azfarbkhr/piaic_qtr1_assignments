'''
Requirements
42.	Write a Python program to construct the following pattern, using a nested for loop
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1

'''

# variables used
length = 6


# logic

for i in range(length):
    for j in range(1, i + 1):
        print(j, end = " ")
    print("")
for i in range(length - 1):
    for j in range(1, length - i -1):
        print(j, end = " ")
    print("")