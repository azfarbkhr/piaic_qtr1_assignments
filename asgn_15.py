'''
Requirement
15.	Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
'''

# values used
principalAmount = 500
interestRate = 0.05
periodInYear = 5

# logic to find future value of principal amount
def futureValue(PV, r, n):
    return round( PV * (1 + r) ** n , 2)

# print output
print(futureValue(principalAmount, interestRate, periodInYear))