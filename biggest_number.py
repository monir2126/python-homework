def find_biggest(list):
    biggest=list[0]
    for value in list:
        if value>biggest:
            biggest=value
    return biggest
list=[]
count=int(input("How many number do you want to enter? "))
for i in range (count):
    value=int(input("enter number: "))
    list.append(value)
result=find_biggest(list)
print("the biggest number is: ",result)

 
