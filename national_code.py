import json
with open("city_codes.json","r",encoding="utf-8") as file:
    city_codes=json.load(file)
national_code=input("please enter your national code: ")
def check_national_code(national_code):
    if len(national_code)==10 and national_code.isdigit():
        return True
    else:
        return False

def get_city(national_code):
    city_code=national_code[:3]
    if city_code in city_codes:
        return city_codes[city_code][1]
    else:
        return "city not found"
    
if check_national_code(national_code):
    print("The national ID format is crrect.")
    print("Place of issue: ", get_city(national_code))
else:
    print("The national code must be 10 character and it most be digit")

    