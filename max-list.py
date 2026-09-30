# def max_number(numbers):
#     return max(numbers)


# numbers=list(map(int,input("Enter your numbers whit space").split()))
# print("max numbers: ",max_number(numbers))
def max_number(numbers):
    biggest = numbers[0]

    for number in numbers:
        if number > biggest:
            biggest = number

    return biggest


numbers =list(map(int,input("Enter numbers whit space: ").split()))

print("The biggest number is:",max_number(numbers))
