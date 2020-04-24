from conf_db import User, Base, Athelete


def find_athelete(user_id, session):
    """
    Производит поиск ближайшего к пользователю атлета
    """
    user = session.query(User).get(user_id)
    if user is not None:

        closest_by_birthdate = session.query(Athelete).filter(
            Athelete.birthdate <= user.birthdate
        ).order_by(Athelete.birthdate.desc()).first()

        if closest_by_birthdate is None:
            closest_by_birthdate = session.query(Athelete).filter(
                Athelete.birthdate > user.birthdate
            ).order_by(Athelete.birthdate).first()

        closest_by_height = session.query(Athelete).filter(
            Athelete.height <= user.height
        ).order_by(Athelete.height.desc()).first()

        if closest_by_height is None:
            closest_by_height = session.query(Athelete).filter(
                Athelete.height > user.height
            ).order_by(Athelete.height).first()

        text_for_user = f'|  {user.first_name} {user.last_name} c индификатором - {user.id}, {user.birthdate} года рождения, c ростом {user.height} м.  |'
        text_for_athelete_birthdate = f'|  По дате рождения: {closest_by_birthdate.name} {closest_by_birthdate.birthdate} года рождения.  |'
        text_for_athelete_height = f'|  По весу: {closest_by_height.name}, c ростом {closest_by_height.height} м.  |'

        print('\nДля пользователя:')
        print('-' * len(text_for_user))
        print(text_for_user)
        print('-' * len(text_for_user))
        print('Ближайшие атлеты:')
        print('-' * len(text_for_athelete_birthdate))
        print(text_for_athelete_birthdate)
        print('-' * len(text_for_athelete_birthdate))
        print('-' * len(text_for_athelete_height))
        print(text_for_athelete_height)
        print('-' * len(text_for_athelete_height))

    else:
        print('********** Пользователя с таким идентификатором нет! **********')
