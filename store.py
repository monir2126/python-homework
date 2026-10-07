class Store:

    def __init__(self):

        # لیست محصولات فروشگاه
        self.products = []

        # سبد خرید
        self.cart = []

        # شماره سفارش
        self.order_number = 1


    # ==============================
    # اضافه کردن محصول
    # ==============================

    def add_product(self):

        print("\n========== اضافه کردن محصول ==========")

        name = input("نام محصول: ")

        price = float(input("قیمت محصول: "))

        stock = int(input("تعداد موجودی: "))

        # بررسی قیمت
        if price <= 0:

            print("قیمت باید بیشتر از صفر باشد.")
            return

        # بررسی موجودی
        if stock < 0:

            print("موجودی نمی‌تواند منفی باشد.")
            return

        # بررسی تکراری نبودن محصول
        for product in self.products:

            if product["name"] == name:

                print("این محصول قبلاً ثبت شده است.")
                return

        # ساخت محصول
        product = {

            "name": name,

            "price": price,

            "stock": stock
        }

        # اضافه کردن محصول به لیست
        self.products.append(product)

        print("محصول با موفقیت اضافه شد.")


    # ==============================
    # نمایش محصولات
    # ==============================

    def show_products(self):

        print("\n========== محصولات ==========")

        if len(self.products) == 0:

            print("هیچ محصولی وجود ندارد.")

            return

        for product in self.products:

            print("--------------------")

            print("نام:", product["name"])

            print("قیمت:", product["price"])

            print("موجودی:", product["stock"])


    # ==============================
    # جستجوی محصول
    # ==============================

    def search_product(self):

        name = input("نام محصول را وارد کنید: ")

        for product in self.products:

            if product["name"] == name:

                print("\nمحصول پیدا شد.")

                print("نام:", product["name"])

                print("قیمت:", product["price"])

                print("موجودی:", product["stock"])

                return

        print("محصول پیدا نشد.")


    # ==============================
    # حذف محصول
    # ==============================

    def delete_product(self):

        name = input("نام محصول برای حذف: ")

        for product in self.products:

            if product["name"] == name:

                self.products.remove(product)

                print("محصول حذف شد.")

                return

        print("محصول پیدا نشد.")


    # ==============================
    # اضافه کردن محصول به سبد
    # ==============================

    def add_to_cart(self):

        name = input("نام محصول: ")

        for product in self.products:

            if product["name"] == name:

                # بررسی موجودی
                if product["stock"] == 0:

                    print("این محصول موجود نیست.")

                    return

                quantity = int(
                    input("تعداد مورد نظر: ")
                )

                # بررسی تعداد
                if quantity <= 0:

                    print("تعداد باید بیشتر از صفر باشد.")

                    return

                # بررسی موجودی
                if quantity > product["stock"]:

                    print("موجودی کافی نیست.")

                    return

                # بررسی اینکه محصول قبلاً در سبد هست یا نه
                for item in self.cart:

                    if item["name"] == name:

                        item["quantity"] += quantity

                        print(
                            "تعداد محصول در سبد افزایش پیدا کرد."
                        )

                        return

                # اضافه کردن محصول جدید به سبد
                cart_item = {

                    "name": product["name"],

                    "price": product["price"],

                    "quantity": quantity
                }

                self.cart.append(cart_item)

                print(
                    "محصول به سبد خرید اضافه شد."
                )

                return

        print("محصول پیدا نشد.")


    # ==============================
    # نمایش سبد خرید
    # ==============================

    def show_cart(self):

        print("\n========== سبد خرید ==========")

        if len(self.cart) == 0:

            print("سبد خرید خالی است.")

            return

        total = 0

        for item in self.cart:

            amount = (
                item["price"]
                * item["quantity"]
            )

            total += amount

            print("--------------------")

            print("نام:", item["name"])

            print("قیمت:", item["price"])

            print("تعداد:", item["quantity"])

            print("مبلغ:", amount)

        print("--------------------")

        print("مبلغ کل:", total)


    # ==============================
    # حذف محصول از سبد
    # ==============================

    def remove_from_cart(self):

        name = input(
            "نام محصول برای حذف از سبد: "
        )

        for item in self.cart:

            if item["name"] == name:

                self.cart.remove(item)

                print(
                    "محصول از سبد حذف شد."
                )

                return

        print(
            "این محصول در سبد وجود ندارد."
        )


    # ==============================
    # پرداخت
    # ==============================

    def checkout(self):

        print("\n========== پرداخت ==========")

        if len(self.cart) == 0:

            print("سبد خرید خالی است.")

            return

        total = 0

        # محاسبه مبلغ کل
        for item in self.cart:

            amount = (
                item["price"]
                * item["quantity"]
            )

            total += amount

        print("مبلغ قابل پرداخت:", total)

        answer = input(
            "آیا پرداخت را انجام می‌دهید؟ (yes/no): "
        )

        if answer != "yes":

            print("پرداخت لغو شد.")

            return

        # بررسی دوباره موجودی
        for item in self.cart:

            for product in self.products:

                if product["name"] == item["name"]:

                    if item["quantity"] > product["stock"]:

                        print(
                            "موجودی محصول کافی نیست."
                        )

                        return

        # کم کردن موجودی
        for item in self.cart:

            for product in self.products:

                if product["name"] == item["name"]:

                    product["stock"] -= item["quantity"]

        # نمایش شماره سفارش
        print(
            "شماره سفارش:",
            self.order_number
        )

        print(
            "خرید با موفقیت انجام شد."
        )

        # افزایش شماره سفارش
        self.order_number += 1

        # خالی کردن سبد
        self.cart.clear()

        print(
            "سبد خرید شما خالی شد."
        )


# =====================================
# ساخت فروشگاه
# =====================================

store = Store()


# =====================================
# منوی اصلی
# =====================================

while True:

    print("\n")
    print("========== فروشگاه ==========")

    print("1. اضافه کردن محصول")

    print("2. نمایش محصولات")

    print("3. جستجوی محصول")

    print("4. حذف محصول")

    print("5. اضافه کردن به سبد خرید")

    print("6. نمایش سبد خرید")

    print("7. حذف از سبد خرید")

    print("8. پرداخت")

    print("9. خروج")

    choice = input(
        "گزینه مورد نظر را انتخاب کنید: "
    )


    if choice == "1":

        store.add_product()


    elif choice == "2":

        store.show_products()


    elif choice == "3":

        store.search_product()


    elif choice == "4":

        store.delete_product()


    elif choice == "5":

        store.add_to_cart()


    elif choice == "6":

        store.show_cart()


    elif choice == "7":

        store.remove_from_cart()


    elif choice == "8":

        store.checkout()


    elif choice == "9":

        print("از فروشگاه خارج شدید.")

        break


    else:

        print("گزینه وارد شده صحیح نیست.")