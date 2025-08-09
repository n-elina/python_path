import random


# While - цикл с предусловием,
# пока пользователь не введёт правильный номер, ...

# while True:
#     print("I'm teapot!")

required_number = 7
user_number = random.randint(0, 10)

while required_number != user_number:
    user_number = random.randint(0, 10)
    print(f'User typed {user_number}')


iterations_count = 10
i = 0

while i < iterations_count:
    print(f'Current iteration {i}')
    i = i + 1
    # i += 1


# For. Итерируем списки и словари

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]

for user in users:
    print(f'{user['name']} is {user['age']} years old')


d = {
    "first": 1,
    "second": 2,
    "third": 3
}

for item in d:
    print(item) # возвтращает только ключи (без значений)

for item in d.keys():
    print(item)

for item in d.items():
    print(item)

for key, value in d.items():
    print(f'Ключ: {key}, Значение: {value}')


# for i in range - цикл с итератором

# print(list(range(0, 10, 2)))

iterations_count = 10

for i in range(iterations_count):
    print(f'Current iteration {i}')


# Break/Continue/Else - прерывание цикла

for i in range(iterations_count):
    if i % 2 == 0:
        continue # позволяет пропустить текущую итерацию цикла, если условие выполняется
        print('I never perform')
    if i > 7:
        break # прерывает цикл, если условие выполняилось
    print(f'Definitely an odd number: {i}')

for i in range(0, 9, 3):
    for j in range(6):
        print(i, j)
        if j == 3:
            continue
        if j == 4:
            break
    if i % 2 == 0:
        break


# enumerate - возвращает пары (индекс, значение)

cities = ['London', 'New York', 'Paris']

# i = 1
for i, city in enumerate(cities):
    print(f'{city} на {i + 1} месте по загрязнению воздуха')
    # i = i + 1
