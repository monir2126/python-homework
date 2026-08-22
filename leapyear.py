year=int(input("Enter year: "))
def leap_year(year):
    if year%400==0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False
if leap_year(year):
    print("this is a leap year")
else:
    print("this is not a leap year")
    