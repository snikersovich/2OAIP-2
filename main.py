import json
with open('name.json', 'r') as f:
    data = json.load(f)

ages = [d['age'] for d in data.values()]
average_age = sum(ages) / len(ages)
print(f'Средний возраст: {average_age}')

city = [d['sity'] for d in data.values()][0]
print(f'Город: {city}')