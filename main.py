from users import request_data, connect_db
from find_athlete import find_athlete

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db(DB_PATH)

    text_welcome = 'Выберите действие: ' \
                   '\n\t - Записать пользователя в базу данных, жмите - 1 ' \
                   '\n\t - Найти ближайшего к пользователю атлета, жмите - 2' \
                   '\n\t - Если захотите выйти, нажмите - q'

    print(text_welcome)
    user_command = input("ввод: ")

    if user_command == '1':
        user = request_data(session)
        session.add(user)
        session.commit()
        text_result = f'|   Данные о пользователе {user.first_name} {user.last_name} сохранены под индификатором - {user.id}   |'
        print('-' * len(text_result))
        print(text_result)
        print('-' * len(text_result))
    elif user_command == '2':
        # TODO: Осталось доделать выборку из find_athlete
        pass
    elif user_command == 'q':
        exit()
    else:
        print('Такой команды нету...')


if __name__ == '__main__':
    main()