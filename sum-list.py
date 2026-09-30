def sum_number(numbers):
  total=0
  for number in numbers:
    total+=number
  return total
numbers=list(map(int,input("Enter your numbers whit space").split()))
print("sum numbers: ",sum_number(numbers))

