def check_email(email):
    valid_domains=["gmail.com","yahoo.com","outlook.com","hotmail.com"]
    at_position=email.find("@")
    if at_position ==-1:
        return False
    domain=email[at_position+1:]
    if domain in valid_domains:
        return True
    else:
        return False
email=input("Please enter your email addres: ")
if check_email(email):
    print("Email is valid")
else:
    print("Email is invalid")