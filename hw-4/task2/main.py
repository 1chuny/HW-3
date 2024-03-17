def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat_info = {"id": id, "name": name, "age": age}
                cats_info.append(cat_info)

    except OSError as err:
        print('Помилка доступу до файлу: ', err)

    return cats_info

path = 'task2.txt'
try:
    cats_info = get_cats_info(path)
    for cat in cats_info:
        print(cat)
except ValueError:
    print("Помилка інформації у файлі")