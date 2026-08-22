number1=int(input("Enter number1: "))
number2=int(input("Enter number2: "))
def largest(number1,number2):
    if number1>number2:
        return number1
    return number2
print("The largest: ",largest(number1,number2))
