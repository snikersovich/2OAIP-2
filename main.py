#Задача 1
import json
with open('name.json', 'r') as f:
    data = json.load(f)

ages = [d['age'] for d in data.values()]
average_age = sum(ages) / len(ages)
print(f'Средний возраст: {average_age}')

city = [d['sity'] for d in data.values()][0]
print(f'Город: {city}')

#Задача 2
import json

data = {
    "Фамилия": "Хайруллин",
    "Имя": "Виктор",
    "Отчество": "Тимофеевич",
    "Телефон": "+7 (9145630338)",
    "Год рождения": "2005",
    "Город рождения": "Свободный",
    "Место учёбы": "БГПУ"
}

with open("data.json", "w") as file:
    json.dump(data, file)

#Задача 3
import json
with open('data.json') as file:
    data = json.load(file)
key = input('Введите ключ, который вы хотите изменить: ')
if key in data:
    value = input('Введите новое значение для ключа ' + key + ': ')
    data[key] = value

#Задача 4
