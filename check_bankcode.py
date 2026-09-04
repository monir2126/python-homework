bank_codes={
    "603799":"Melli Bank",
    "589210":"Sepah Bank",
    "627648":"Toseh saderat Bank",
    "603770":"Keshavarzy Bank",
    "627961":"Sanat & madan Bank",
    "608023":"Maskan Bank",
    "627760":"Post Bank Iran",
    "502229":"Pasargod Bank",
    "610433":"Melat Bank",
    "603769":"Saderat Bank",
    "627353":"Tejarat Bank"
}
def get_bank(card_number):
    bank_code=card_number[:6]
    if bank_code in bank_codes and len(card_number)==16:
        return bank_codes[bank_code]
    else:
        return "Unknown Bank"
card_number=input("Enter your card number: ")
print(get_bank(card_number))
    