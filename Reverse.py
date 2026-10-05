numbers = list(map(int, input("لیست را وارد کنید: ").split()))

new_list = []

for i in range(len(numbers) - 1, -1, -1):
    new_list.append(numbers[i])

print(new_list)
