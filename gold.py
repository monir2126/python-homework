gold_price=float(input("Enter gold price per gram:  "))
weight=float(input("Enter gold weight(grams): "))
ojrat=float(input("Enter emount of ojrat(%): "))
profit=float(input("Enter emount of profit(%): "))
tax=float(input("Enter emount of tax(%): "))
gold_valu=weight*gold_price
ojrat_amount=gold_valu*ojrat/100
price_befor_profit=gold_valu+ojrat_amount
profit_amount=price_befor_profit*profit/100
price_befor_tax=price_befor_profit+profit_amount
tax_amount=(ojrat_amount+profit_amount)*tax/100
final_price=price_befor_tax+tax_amount
print("Gold_price: ",gold_valu,"\nweight: ",weight,"\nojrat: ",ojrat_amount,"\nprofit: ",profit_amount,"\ntax: ",tax_amount,"\nFinal price: ",final_price)