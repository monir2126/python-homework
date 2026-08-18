second=int(input("Enter seconds: "))
hours=second//3600
minutes=(second%3600)//60
second=second%60
print(hours,"ساعت",minutes,"دقیقه",second,"ثانیه")
