contacts={}
def add_contact():
    name=input("نام مخاطب:  ")
    phone=input("شماره مخاطب:  ")
    contacts[name]=phone
    print("مخاطب با موفقیت اضافه شد")
def find_contact():
    name=input("نام مخاطب را وارد کنید:  ")
    if name in contacts:
        print("شماره: ",contacts[name])
    else:
        print("مخاطب پیدا نشد")
def delete_contact():
    name=input("نام مخاطبی که میخواهید حذف کنید را وارد کنید:  ")
    if name in contacts:
        del contacts[name]
        print("مخاطب حذف شد")
    else:
        print("مخاطب پیدا نشد")
def show_contact():
    if len(contacts)==0:
        print("دفترچه تلفن خالی است")
    else:
        print("\nمخاطب ها:  ")
        for name in contacts:
            print(name,":",contacts[name])
while True:
    print("\n---دفترچه تلفن---")
    print("1.اضافه کردن محاطب")
    print("2.پیدا کردن شماره مخاطب")
    print("3.حذف مخاطب")
    print("4.نمایش همه مخاطب ها")
    print("5.خروج")
    choice=input("یک گزینه انتخاب کنید")
    if choice=="1":
       add_contact()
    elif choice=="2":
       find_contact()
    elif choice=="3":
        delete_contact()
    elif choice=="4":
        show_contact()
    elif choice=="5":
        print("برنامه بسته شد")
        break
    else:
        print("گزینه وارد شده صحیح نیست")
    
       

