import datetime
import sqlalchemy as SA
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from validator import valid_email, valid_gender, valid_day, valid_month, valid_year, valid_height

Base = declarative_base()


class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = 'user'

    id = SA.Column(SA.Integer, primary_key=True)
    first_name = SA.Column(SA.Text)
    last_name = SA.Column(SA.Text)
    gender = SA.Column(SA.Text)
    email = SA.Column(SA.Text)
    birthdate = SA.Column(SA.Text)
    height = SA.Column(SA.REAL)


def connect_db(file_db):
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    engine = SA.create_engine(file_db)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def request_data(session):
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    WARNING = "Вы ввели некорректные данные!"

    def _command_exit(command):
        if command.lower() == 'q':
            return exit()

    print("Введите данные!")

    while True:
        first_name = input("Имя (пример ввода - Иван) \n\tввод: ").strip().title()
        _command_exit(first_name)
        last_name = input("Фамилия (пример ввода - Иванов) \n\tввод: ").strip().title()
        _command_exit(last_name)
        valid_user = session.query(User).filter(User.first_name == first_name).filter(User.last_name == last_name).first()
        if valid_user is not None:
            print('Пользователь с таким именем и фамилией существует!')
        else:
            break

    while True:
        gender = input("Пол (пример ввода - м/ж) \n\tввод: ").strip().lower()
        _command_exit(gender)
        if not valid_gender(gender):
            print(WARNING)
        else:
            break

    while True:
        email = input("Адрес электронной почты (пример ввода - ivanov@mail.ru) \n\tввод: ").strip().lower()
        _command_exit(email)
        if not valid_email(email):
            print(WARNING)
        else:
            break

    print("Дата рождения:")

    while True:
        day = input("\tДень (пример ввода - 12) \n\t\tввод: ")
        _command_exit(day)
        if not valid_day(day):
            print(WARNING)
        else:
            break

    while True:
        month = input("\tМесяц (пример ввода - 05) \n\t\tввод: ")
        _command_exit(month)
        if not valid_month(month):
            print(WARNING)
        else:
            break

    while True:
        year = input("\tГод (пример ввода - 1988) \n\t\tввод: ")
        _command_exit(year)
        if not valid_year(year):
            print(WARNING)
        else:
            break

    birthdate = str(datetime.date(int(year), int(month), int(day)))

    while True:
        height = input("Рост (пример ввода - 1.86 / 2) \n\tввод: ")
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

