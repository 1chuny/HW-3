import re

phone_number = input("Введіть свій номер телефона: ")

def normalize_phone(phone_number):
    true_number = re.sub(r"[^0-9+]", "", phone_number)
    if (len(true_number) == 10 or len(true_number) == 12 or len(true_number) == 13):
        if (len(true_number) == 10):
            true_number = "+38" + true_number
            return true_number 
        elif (len(true_number) == 12):
            true_number = "+" + true_number
            return true_number
        else:
            return true_number
        
if(normalize_phone(phone_number)):
    print(f"Правильний номер: {normalize_phone(phone_number)}")
else:
    print("Такий номер не може існувати!")