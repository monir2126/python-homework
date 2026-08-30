def sum_numbers(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum
list=[]
count=int(input("How many numbers? "))
for i in range(count):
    value=int(input("enter a number: "))
    list.append(value)
result=sum_numbers(list)
print("The sum is:",result)