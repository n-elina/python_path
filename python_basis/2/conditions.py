# Boolean - 3 состояния

b = bool

t = True
f = False
n = None


# if/elif/else

if True:
    print('Я выполняюсь!')

if False:
    print('Я никогда не выполнюсь!')

code = 199
if 200 <= code < 400:
    print('Good response!')
elif 400 <= code < 600:
    print('Bad response!')
else:
    print('Kind of strange code!')


# Пустые объекты - false

user_list = []

if user_list == []:
    pass

items_count = 0

if items_count == 0:
    pass

if 'abc' == '':
    pass
