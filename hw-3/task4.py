from datetime import datetime, timedelta  

users = [  
    {"name": "Andrey Chunakov", "birthday": "2006.02.15"},
    {"name": "Bob", "birthday": "1990.01.27"},
    {"name": "Sam", "birthday": "1999.03.11"},
    {"name": "James", "birthday": "2001.03.13"},
    {"name": "Ken", "birthday": "1990.03.10"},
]

def find_next_weekday(d, weekday: int):  
    """
     Ф-ція для знаходження наступного заданого дня тижня після заданої дати
    :param d: datetime.date - початкова дата
    :param weekday: int - день тижня від 0 (понеділок) до 6 (неділя)
    :return:
    """
    days_ahead = weekday - d.weekday()  
    if days_ahead <= 0:  
        days_ahead += 7  
    return d + timedelta(days=days_ahead)  

def prepare_users(users):
    prepared_users = []  
    for user in users:  
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  
            prepared_users.append({"name": user['name'], 'birthday': birthday})  
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')  
    return prepared_users

def get_upcoming_birthdays(prepared_users, days = 7):
    today = datetime.today().date()  

    upcoming_birthdays = []  
    for user in prepared_users:  
        birthday_this_year = user["birthday"].replace(year=today.year) 

        if birthday_this_year < today:  
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  

        if 0 <= (birthday_this_year - today).days <= days:  
            if birthday_this_year.weekday() >= 5:  
                birthday_this_year = find_next_weekday(birthday_this_year, 0)  

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  
            upcoming_birthdays.append({  
                "name": user["name"],
                "congratulation_date": congratulation_date_str
        })
    return upcoming_birthdays

prepared_users = prepare_users(users)
upcoming_birthdays = get_upcoming_birthdays(prepared_users)
print(upcoming_birthdays)
