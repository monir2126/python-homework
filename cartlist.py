cart = {}

n = int(input("How many products? "))

for i in range(n):

    name = input("Enter product name: ")
    price = int(input("Enter price: "))
    count = int(input("Enter count: "))

    if name in cart:
        cart[name]["count"] = cart[name]["count"] + count
    else:
        cart[name] = {
            "price": price,
            "count": count
        }

total = 0
expensive_product = ""
max_price = 0

print("\n--- Product List ---")

for product in cart:

    price = cart[product]["price"]
    count = cart[product]["count"]

    amount = price * count

    print(product, "Price:", price, "Count:", count, "Amount:", amount)

    total = total + amount

    if price > max_price:
        max_price = price
        expensive_product = product

print("\nTotal price:", total)
print("Most expensive product:", expensive_product)
print("Price:", max_price)