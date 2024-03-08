from datetime import datetime

date_string = input("Введіть дату у форматі - рік.місяць.число: ")

try:
    date = datetime.strptime(date_string, "%Y.%m.%d")
except ValueError:
    print("Ви ввели дату неправильно!")

def get_days_from_today(date):
    today = datetime.today()
    days_between_dates = today.toordinal() - date.toordinal()
    return days_between_dates

print("Кількість днів між заданою датою і поточною датою -", get_days_from_today(date))
