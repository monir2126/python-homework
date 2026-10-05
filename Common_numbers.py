def common_numbers(list1, list2):
    common = []

    for num in list1:
        if num in list2:
            common.append(num)

    return common


list1 = list(map(int, input("لیست اول: ").split()))
list2 = list(map(int, input("لیست دوم: ").split()))

print(common_numbers(list1, list2))
