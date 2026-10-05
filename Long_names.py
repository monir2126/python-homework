def long_names(names):
    result = []

    for name in names:
        if len(name) > 5:
            result.append(name)

    return result


names = input("اسم‌ها را وارد کنید: ").split()

print(long_names(names))
