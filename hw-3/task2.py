import random

def get_numbers_ticket(min, max, quantity):
    random_set = set(random.randint(min, max) for _ in range(quantity))
    return random_set

min = int(input("Введіть початкове значення: "))
max = int(input("Введіть кінцеве значення: "))
quantity = int(input("Введіть кількість значеннь: "))

print(f"Ваш набір унікальних випадкових чисел: {get_numbers_ticket(min, max, quantity)}")