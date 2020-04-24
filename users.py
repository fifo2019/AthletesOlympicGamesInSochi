import datetime
from validator import valid_email, valid_gender, valid_day, valid_month, valid_year, valid_height
from conf_db import User


def request_data(session):
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    WARNING = "********** Введены некорректные данные! **********"

    def _command_exit(command):
        if command.lower() == 'q':
            return exit()

    print("Введите данные!")

    while True:
        first_name = input("  Имя (пример ввода - Иван) \nввод: ").strip().title()
        _command_exit(first_name)
        last_name = input("  Фамилия (пример ввода - Иванов) \nввод: ").strip().title()
        _command_exit(last_name)
        valid_user = session.query(User).filter(User.first_name == first_name, User.last_name == last_name).first()
        if valid_user is not None:
            print('********** Пользователь с таким именем и фамилией существует! **********')
        else:
            break

    while True:
        gender = input("  Пол (пример ввода - м/ж) \nввод: ").strip().lower()
        _command_exit(gender)
        if not valid_gender(gender):
            print(WARNING)
        else:
            break

    while True:
        email = input("  Адрес электронной почты (пример ввода - ivanov@mail.ru) \nввод: ").strip().lower()
        _command_exit(email)
        if not valid_email(email):
            print(WARNING)
        else:
            break

    print("Дата рождения:")

    while True:
        day = input("  День (пример ввода - 12) \n    ввод: ")
        _command_exit(day)
        if not valid_day(day):
            print(WARNING)
        else:
            break

    while True:
        month = input("  Месяц (пример ввода - 05) \n    ввод: ")
        _command_exit(month)
        if not valid_month(month):
            print(WARNING)
        else:
            break

    while True:
        year = input("  Год (пример ввода - 1988) \n    ввод: ")
        _command_exit(year)
        if not valid_year(year):
            print(WARNING)
        else:
            break

    birthdate = str(datetime.date(int(year), int(month), int(day)))

    while True:
        height = input("  Рост (пример ввода - 1.86 / 2) \nввод: ")
        _command_exit(height)
        if not valid_height(height):
            print(WARNING)
        else:
            break

    height = round(float(height), 2)

    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )

    return user

