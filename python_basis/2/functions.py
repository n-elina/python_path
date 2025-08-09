from operator import itemgetter
from pprint import pprint


# Функции с позиционными аргументами

def sum_numbers(a: int, b: int):
    print(a + b)

sum_numbers(1, 2)
sum_numbers(1000000, 2500000)
sum_numbers(-1200000, 1200000)
sum_numbers(5, 8)
# sum_numbers('adw', 'adwaw')


# Функция с именованными аргументами

sum_numbers(b=2, a=3)
sum_numbers(a=2, b=3)


# Функция с аргументами по умолчанию

def multiply_numbers(n: int, mult: int = 2):
    print(n * mult)

multiply_numbers(25, mult=25)
multiply_numbers(25)

# print(1, 34, sep=' || ', end=' || ')


# Возвращаем  значение

def summ (a: int, b: int):
    return a * b

s = summ(7, 8)
print(s)


# Возвращаем несколько значений

def return_tuple():
    return 1, 2, 3

t = return_tuple()
print(t)

t1, t2, t3 = return_tuple()
print(t1, t2, t3)

t1, *t2 = return_tuple()
print(t1, t2)

t1, t2, *t3 = return_tuple()
print(t1, t2, t3)

t1, *_ = return_tuple()
print(t1)


# Переменнное количество аргументов на примере print


print('--------')

def custom_print(*args):
    # for arg in args:
    #     print(arg)

    print(args)
    print(*args)

custom_print(1, 2, 3, 4, 5)


# Переменное кол-во именованных аргументов

def custom_named_print(*args, **kwargs):
    print(args, kwargs)
    print(*args, **kwargs)

custom_named_print(1, 2, 3, 4, 5, end='!\n', sep=' | ')


# Область видимости переменных

print('--------')

v = 123

def my_awesome_func():
    v = 456
    print(v)

print(v)
my_awesome_func()
print(v)


# Функция - тоже объект

print('--------')

p = print # функция print() определена в переменную p

p(1, 2, 3)


users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]

def get_age(user):
    return user["age"]

users.sort(key=get_age)

# users.sort(key=lambda user: user['age'])

# users.sort(key=itemgetter('age'))

pprint(users)
