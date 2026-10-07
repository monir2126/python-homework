class UserManager:

    def __init__(self):
        self.users = []
        self.current_user = None

    # =========================
    # ثبت نام
    # =========================
    def register(self):

        print("\n========== ثبت نام ==========")

        first_name = input("نام: ")
        last_name = input("نام خانوادگی: ")
        username = input("نام کاربری: ")
        email = input("ایمیل: ")
        mobile = input("شماره موبایل: ")
        password = input("رمز عبور: ")
        confirm_password = input("تکرار رمز عبور: ")

        # بررسی خالی نبودن اطلاعات
        if first_name == "" or last_name == "":
            print("نام و نام خانوادگی نمی‌توانند خالی باشند.")
            return

        if username == "":
            print("نام کاربری نمی‌تواند خالی باشد.")
            return

        # بررسی تکراری نبودن نام کاربری
        for user in self.users:

            if user["username"] == username:
                print("این نام کاربری قبلاً ثبت شده است.")
                return

        # بررسی تکراری نبودن ایمیل
        for user in self.users:

            if user["email"] == email:
                print("این ایمیل قبلاً ثبت شده است.")
                return

        # بررسی ایمیل
        if "@" not in email:
            print("ایمیل وارد شده معتبر نیست.")
            return

        # بررسی شماره موبایل
        if len(mobile) != 11 or not mobile.isdigit():
            print("شماره موبایل باید 11 رقم باشد.")
            return

        # بررسی طول رمز
        if len(password) < 6:
            print("رمز عبور باید حداقل 6 کاراکتر باشد.")
            return

        # بررسی یکسان بودن رمزها
        if password != confirm_password:
            print("رمز عبور و تکرار آن یکسان نیستند.")
            return

        # ساخت کاربر
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "mobile": mobile,
            "password": password,
            "active": True
        }

        # اضافه کردن کاربر
        self.users.append(user)

        print("ثبت نام با موفقیت انجام شد.")


    # =========================
    # ورود
    # =========================
    def login(self):

        print("\n========== ورود ==========")

        username = input("نام کاربری: ")
        password = input("رمز عبور: ")

        attempts = 3

        while attempts > 0:

            for user in self.users:

                if user["username"] == username:

                    # بررسی فعال بودن حساب
                    if user["active"] == False:
                        print("این حساب غیرفعال است.")
                        return

                    # بررسی رمز عبور
                    if user["password"] == password:

                        self.current_user = user

                        print("ورود با موفقیت انجام شد.")
                        print("خوش آمدید", user["first_name"])

                        return

                    else:

                        attempts = attempts - 1

                        print("رمز عبور اشتباه است.")
                        print("تعداد تلاش باقی مانده:", attempts)

                        if attempts == 0:
                            print("تعداد تلاش‌ها تمام شد.")

                        return

            print("نام کاربری پیدا نشد.")
            return


    # =========================
    # خروج
    # =========================
    def logout(self):

        if self.current_user is None:

            print("هیچ کاربری وارد نشده است.")

        else:

            print(
                "خداحافظ",
                self.current_user["first_name"]
            )

            self.current_user = None

            print("با موفقیت خارج شدید.")


    # =========================
    # نمایش اطلاعات حساب
    # =========================
    def show_profile(self):

        if self.current_user is None:

            print("ابتدا باید وارد حساب شوید.")
            return

        user = self.current_user

        print("\n========== اطلاعات حساب ==========")

        print("نام:", user["first_name"])
        print("نام خانوادگی:", user["last_name"])
        print("نام کاربری:", user["username"])
        print("ایمیل:", user["email"])
        print("موبایل:", user["mobile"])

        if user["active"]:
            print("وضعیت حساب: فعال")
        else:
            print("وضعیت حساب: غیرفعال")


    # =========================
    # تغییر رمز عبور
    # =========================
    def change_password(self):

        if self.current_user is None:

            print("ابتدا باید وارد حساب شوید.")
            return

        old_password = input("رمز عبور فعلی: ")

        if old_password != self.current_user["password"]:

            print("رمز عبور فعلی اشتباه است.")
            return

        new_password = input("رمز عبور جدید: ")
        confirm_password = input("تکرار رمز عبور جدید: ")

        if len(new_password) < 6:

            print("رمز عبور باید حداقل 6 کاراکتر باشد.")
            return

        if new_password != confirm_password:

            print("رمزهای عبور یکسان نیستند.")
            return

        self.current_user["password"] = new_password

        print("رمز عبور با موفقیت تغییر کرد.")


    # =========================
    # غیرفعال کردن حساب
    # =========================
    def deactivate_account(self):

        if self.current_user is None:

            print("ابتدا باید وارد حساب شوید.")
            return

        answer = input(
            "آیا مطمئن هستید؟ (yes/no): "
        )

        if answer == "yes":

            self.current_user["active"] = False

            print("حساب شما غیرفعال شد.")

            self.current_user = None

        else:

            print("عملیات لغو شد.")


# ====================================
# ساخت سیستم
# ====================================

system = UserManager()


# ====================================
# منوی اصلی
# ====================================

while True:

    print("\n")
    print("========== سیستم کاربران ==========")

    if system.current_user is None:

        print("1. ثبت نام")
        print("2. ورود")
        print("3. خروج از برنامه")

        choice = input("انتخاب شما: ")

        if choice == "1":

            system.register()

        elif choice == "2":

            system.login()

        elif choice == "3":

            print("برنامه پایان یافت.")
            break

        else:

            print("گزینه نامعتبر است.")

    else:

        print("1. مشاهده پروفایل")
        print("2. تغییر رمز عبور")
        print("3. غیرفعال کردن حساب")
        print("4. خروج از حساب")

        choice = input("انتخاب شما: ")

        if choice == "1":

            system.show_profile()

        elif choice == "2":

            system.change_password()

        elif choice == "3":

            system.deactivate_account()

        elif choice == "4":

            system.logout()

        else:

            print("گزینه نامعتبر است.")