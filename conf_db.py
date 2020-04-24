import sqlalchemy as SA
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


def connect_db(file_db):
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    engine = SA.create_engine(file_db)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


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
    height = SA.Column(SA.Float)


class Athelete(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = 'athelete'

    id = SA.Column(SA.Integer, primary_key=True)
    age = SA.Column(SA.Integer)
    birthdate = SA.Column(SA.Text)
    gender = SA.Column(SA.Text)
    height = SA.Column(SA.Float)
    name = SA.Column(SA.Text)
    weight = SA.Column(SA.Integer)
    gold_medals = SA.Column(SA.Integer)
    silver_medals = SA.Column(SA.Integer)
    bronze_medals = SA.Column(SA.Integer)
    total_medals = SA.Column(SA.Integer)
    sport = SA.Column(SA.Text)
    country = SA.Column(SA.Text)

