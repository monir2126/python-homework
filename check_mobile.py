def check_mobile(mobile):
    if len(mobile) == 11 and mobile.isdigit() and mobile.startswith("09"):
        return True
    else:
        return False
mobile=input("Enter your phone number: ")
if check_mobile(mobile):
    print("your phone number have a standard format.")
else:
    print("phone number must be 11 digits and start whit 09*** like this:0913***4081")