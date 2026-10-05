#def count_number(numbers, target):
   # count = 0
  #  for num in numbers:
        #if num == target:
            #count += 1

    #return count


#numbers = list(map(int, input("لیست را وارد کنید: ").split()))
#target = int(input("عدد مورد نظر را وارد کنید: "))

#print("تعداد تکرار:", count_number(numbers, target))
def count_number(numbers, target):
    return numbers.count(target)


numbers = list(map(int, input("لیست را وارد کنید: ").split()))
target = int(input("عدد را وارد کنید: "))

print(count_number(numbers, target))
