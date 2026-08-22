bmi=float(input("Enter your BMI: "))
def BMI(bmi):
    if bmi<18.5:
        return "underweight"
    elif bmi<25:
        return "normal"
    elif bmi<30:
        return "overweight"
    else:
        return "obese"
print("your BMI status: ",BMI(bmi))