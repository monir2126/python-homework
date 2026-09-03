def check_password(password):
    errors =[]
    if len(password)<=8:
        errors.append("The pssword must be longer than 8 characters")
    commen_password=["123456","password","qwerty","123456789","12345678"]
    if password.lower() in commen_password :
        errors.append("The password is commen")
    if not any (char.isdigit() for char in password):
        errors.append("The password must have character digit")
    if not any(char.isalpha() for char in password):
        errors.append("The password must have characters alpha")
    if len(errors)==0:
        print("YOU HAVE A STANDARD PASSWORD")
    else:
        print("YOU DONT HAVE A STANDARD PASSWORD")
        for error in errors:
            print("-",error)

password=input("please enter your password: ")
check_password(password)