def sum_numbers(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
number=int(input("Enter a number: "))
print(sum_numbers(number))