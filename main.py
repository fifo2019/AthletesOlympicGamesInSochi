from users import request_data
from conf_db import connect_db
from find_athlete import find_athelete
from validator import valid_user_id


DB_PATH = "sqlite:///sochi_athletes.sqlite3"

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db(DB_PATH)

    text_welcome = 'Выберите действие:\n ' \
                   ' - Записать пользователя в базу данных, жмите - 1\n ' \
                   ' - Найти ближайшего к пользователю атлета, жмите - 2\n ' \
                   ' - Если захотите выйти, нажмите - q '

    print(text_welcome)
    user_command = input("ввод: ")

    if user_command == '1':
        """ Записать пользователя в базу данных """
        user = request_data(session)
        session.add(user)
        session.commit()
        text_result = f'|   Данные о пользователе {user.first_name} {user.last_name} сохранены под индификатором - {user.id}   |'
        print('-' * len(text_result))
        print(text_result)
        print('-' * len(text_result))
    elif user_command == '2':
        """ Найти ближайшего к пользователю атлета """
        print('  Введите индификатор пользователя (вводить целое число)')

        while True:
            user_id = input('ввод: ')
            if not valid_user_id(user_id):
                print('***** Введен некоректный индификатор, проверте правильнось заполнения! Индификатор - целое число! *****')
            else:
                break

        find_athelete(user_id, session)

    elif user_command == 'q':
        """ Выйти из программы """
        exit()
    else:
        print('Такой команды нету...')


if __name__ == '__main__':
    main()