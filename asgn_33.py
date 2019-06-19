'''
Requirement
33.	Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
'''

# variables used
firstName = ""
lastName = ""

# input from user
firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")


# logic used 
def name_to_american_style (firstName, lastName):
    return(lastName + ", " + firstName)

# print output
print("Your name in american style is {x}".format(
    x = name_to_american_style(firstName = firstName, lastName = lastName
    )))