birth_year=int(input("birth year: "))
birth_month=int(input("birth month: "))
birth_day=int(input("birthday: "))

today_year=int(input("today year: "))
today_month=int(input("today month: "))
today_day=int(input("today day: "))

age_year=today_year-birth_year
age_month=today_month-birth_month
age_day=today_day-birth_day

if age_day<0:
    age_month=age_month-1
    age_day=age_day+30
if age_month<0:
    age_year=age_year-1
    age_month=age_month+12
    print("age year: ",age_year,"age month: ",age_month,"age day: ",age_day)
# ابتدا سال و ماه و روز فعلی را از سال و ماه و روز تولد کم میکنیم
# در صورتی که پاسخ منها عددی منفی باشد یعنی باید از ماه و سال قرض یگیریم 
# پس از شرط استفاده میکنیم تا محاسبه را دقیق تر کنیم
# نکته:در تاریخ شمسی بعضی ماه ها 30 یا 31 روزه یا مثلا سال کبیسه داریم این قسمتو بلد نبودم حساب کنم