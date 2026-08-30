def even_number(n):
    count = 0

    for i in range(2, n + 1):
        if i % 2 == 0:
            count += 1

    return count


number = int(input("Enter your number: "))
print(even_number(number))
    
    

