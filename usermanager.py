class UserManager:

    def __init__(self):
        self.users = []

    # اضافه کردن کاربر
    def add_user(self):

        first_name = input("نام را وارد کنید: ")
        last_name = input("نام خانوادگی را وارد کنید: ")
        national_code = input("کد ملی را وارد کنید: ")
        mobile = input("شماره موبایل را وارد کنید: ")

        # بررسی تکراری نبودن کد ملی
        for user in self.users:
            if user["national_code"] == national_code:
                print("این کد ملی قبلاً ثبت شده است.")
                return

        # ساخت کاربر
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "national_code": national_code,
            "mobile": mobile,
            "active": True
        }

        # اضافه کردن کاربر به لیست
        self.users.append(user)

        print("کاربر با موفقیت اضافه شد.")


    # پیدا کردن کاربر با کد ملی
    def find_user(self):

        national_code = input("کد ملی کاربر را وارد کنید: ")

        for user in self.users:
            if user["national_code"] == national_code:
                print("کاربر پیدا شد.")
                print("نام:", user["first_name"])
                print("نام خانوادگی:", user["last_name"])
                print("کد ملی:", user["national_code"])
                print("شماره موبایل:", user["mobile"])

                if user["active"]:
                    print("وضعیت: فعال")
                else:
                    print("وضعیت: غیرفعال")

                return

        print("کاربر پیدا نشد.")


    # غیرفعال کردن کاربر
    def deactivate_user(self):

        national_code = input("کد ملی کاربر را وارد کنید: ")

        for user in self.users:

            if user["national_code"] == national_code:

                user["active"] = False

                print("کاربر با موفقیت غیرفعال شد.")
                return

        print("کاربر پیدا نشد.")


    # حذف کاربر
    def delete_user(self):

        national_code = input("کد ملی کاربر را وارد کنید: ")

        for user in self.users:

            if user["national_code"] == national_code:

                self.users.remove(user)

                print("کاربر با موفقیت حذف شد.")
                return

        print("کاربر پیدا نشد.")


    # نمایش تمام کاربران
    def show_users(self):

        if len(self.users) == 0:
            print("هیچ کاربری وجود ندارد.")
            return

        for user in self.users:

            print("--------------------")

            print("نام:", user["first_name"])
            print("نام خانوادگی:", user["last_name"])
            print("کد ملی:", user["national_code"])
            print("شماره موبایل:", user["mobile"])

            if user["active"]:
                print("وضعیت: فعال")
            else:
                print("وضعیت: غیرفعال")


    # نمایش کاربران فعال
    def show_active_users(self):

        found = False

        for user in self.users:

            if user["active"]:

                found = True

                print("--------------------")

                print("نام:", user["first_name"])
                print("نام خانوادگی:", user["last_name"])
                print("کد ملی:", user["national_code"])
                print("شماره موبایل:", user["mobile"])
                print("وضعیت: فعال")

        if found == False:
            print("هیچ کاربر فعالی وجود ندارد.")


# ساخت شیء
manager = UserManager()


# منوی اصلی
while True:

    print("\n========== مدیریت کاربران ==========")
    print("1. اضافه کردن کاربر")
    print("2. پیدا کردن کاربر")
    print("3. غیرفعال کردن کاربر")
    print("4. حذف کاربر")
    print("5. نمایش همه کاربران")
    print("6. نمایش کاربران فعال")
    print("7. خروج")

    choice = input("گزینه مورد نظر را انتخاب کنید: ")


    if choice == "1":

        manager.add_user()


    elif choice == "2":

        manager.find_user()


    elif choice == "3":

        manager.deactivate_user()


    elif choice == "4":

        manager.delete_user()


    elif choice == "5":

        manager.show_users()


    elif choice == "6":

        manager.show_active_users()


    elif choice == "7":

        print("برنامه پایان یافت.")
        break


    else:

        print("گزینه وارد شده صحیح نیست.")