def total_salary(path):
    total_sum = 0
    count = 0

    try:
        with open(path, 'r') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total_sum += salary
                count += 1
    except OSError as err:
        print('Помилка доступу до файлу: ', err)

    if count > 0:
        average_salary = total_sum / count
        return total_sum, average_salary

path = 'task1.txt'

try:
    total_sum, average_salary = total_salary(path)
    print(f'Загальна сума заробітної плати: {total_sum}')
    print(f'Середня заробітна плата: {average_salary}')
except ValueError:
    print("Помилка інформації у файлі")
