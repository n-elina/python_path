from datetime import time
from pygments.lexers import func


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23, minute=00, second=00)
    '''TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)'''

    # is_dark_theme = current_time.hour > 22 or current_time.hour < 6
    # is_dark_theme = time(hour=22) <= current_time <= time(hour=6)

    if current_time > time(hour=22) or current_time < time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    '''TODO переключите темную тему в зависимости от времени суток,'''
    '''но учтите что темная тема может быть включена вручную'''

    # is_dark_theme = None
    # if dark_theme_enabled_by_user is True:
    #     is_dark_theme = True
    # elif dark_theme_enabled_by_user is False:
    #     is_dark_theme = False
    # elif dark_theme_enabled_by_user is None:
    #     if current_time.hour >= 22 or current_time.hour < 6:
    #         is_dark_theme = True
    #     else:
    #         is_dark_theme = False

    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    elif current_time > time(hour=22) or current_time < time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    '''TODO найдите пользователя с именем "Olga'''

    suitable_users = None
    for user in users:
        if user['name'] == 'Olga':
            suitable_users = user
            break

    # suitable_users = [user for user in users if user['name'] == 'Olga'][
    #     0
    # ]  # возможный вариант, но менее удобный, так как возвращает список всех совпадений

    assert suitable_users == {"name": "Olga", "age": 45}

    '''TODO найдите всех пользователей младше 20 лет'''

    # suitable_users = []
    # for user in users:
    #     if user['age'] < 20:
    #         suitable_users.append(user)

    suitable_users = [
        user for user in users if user['age'] < 20
    ]  # здесь list comprehension более удобен, так как как раз возвращает список всех совпадений

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(
        page_url="https://companyname.com/login", button_text="Register"
    )


def print_function_name_and_args(func, *args, **kwargs):
    function_name = func.__name__.replace('_', ' ').title()
    argument_name = ", ".join([*args, *kwargs.values()])
    print(f'{function_name} [{argument_name}]')
    return f'{function_name} [{argument_name}]'


def open_browser(browser_name):
    actual_result = print_function_name_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_name_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_name_and_args(
        find_registration_button_on_login_page, page_url, button_text
    )
    assert (
        actual_result
        == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
    )
