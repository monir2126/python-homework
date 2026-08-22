number=int(input("Enter a number: "))
def check_prime(number):
    if number<2:
        return False
    for i in range (2,number):
        if number%i == 0:
            return False
    return True
if check_prime(number):
    print("عدد اول است")
else:
    print("عدد اول نیست")