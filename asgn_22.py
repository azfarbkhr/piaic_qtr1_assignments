'''
Requirements
22.	Write a Python program to calculate body mass index. (https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php)

BMI = weight (kg) ÷ height2 (m2)

BMI	                BMI Category
Less than 15	    Very severely underweight
Between 15 and 16	Severely underweight
Between 16 and 18.5	Underweight
Between 18.5 and 25	Normal (healthy weight)
Between 25 and 30	Overweight
Between 30 and 35	Moderately obese
Between 35 and 40	Severely obese
Over 40	            Very severely obese



'''


# values used
weightKg = 76
heightMeter = 1.8


# input from user
while True:
    try:
        weightKg = float(input("Please enter your weight in KG: "))
        if weightKg <= 0:
            raise ZeroDivisionError
        break
    except ValueError:
        print("Error 01: You have entered an invalid weight.")
    except ZeroDivisionError:
        print("Error 02: Your weight can not be less than or equal to zero.")


while True:
    try:
        heightMeter = float(input("Please enter your height in meter: "))
        if heightMeter <= 0:
            raise ZeroDivisionError
        break
    except ValueError:
        print("Error 01: You have entered an invalid height.")
    except ZeroDivisionError:
        print("Error 02: Your height can not be less than or equal to zero.")


# logic to calculate BMI
def bmi_calculator(weight, height):
    result = {"bmiValue": 0, "bmiCategory": ""}
    result["bmiValue"] = round(weight / (height ** 2), 2)

    bmiCategories = {
        15: "very severely underweight",
        16:	"severely underweight",
        18.5: "underweight",
        25: "normal (healthy weight)",
        30: "overweight",
        35: "moderately obese",
        40: "severely obese"
    }

    for key in bmiCategories:
        if result["bmiValue"] < key:
            result["bmiCategory"] = bmiCategories[key]
            break
        else:
            result["bmiCategory"] = "very severely obese"

    return result


# print output
myBMIStats = bmi_calculator(weightKg, heightMeter)
print("You BMI value is {x}".format(x=myBMIStats["bmiValue"]))
print("You are {x}".format(x=myBMIStats["bmiCategory"]))
