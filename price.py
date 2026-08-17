
base_price=float(input("Enter your bace price: "))
discount=float(input("Enter discount percentage:  "))
tax=float(input("Enter tax percentage:  "))
discount_amount=base_price*discount/100
price_after_discount=base_price-discount_amount
tax_amount=price_after_discount*tax/100
finall_price=price_after_discount+tax_amount
print("final price: ",finall_price)