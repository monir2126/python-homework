cart = {}

n = int(input("How many products? "))

for i in range(n):
    name = input("Enter product name: ")
    price = int(input("Enter price: "))
    count = int(input("Enter count: "))

    cart[name] = {
        "price": price,
        "count": count
    }

total = 0

for product in cart:
    price = cart[product]["price"]
    count = cart[product]["count"]

    total = total + price * count

print("Total price:", total)