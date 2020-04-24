def valid_gender(gender):
    """ Проверяет на валидность ввода пола пользователя"""
    if gender == 'м' or gender == 'ж':
        return True


def valid_email(email):
    """ Проверяет на валидность ввода адреса почты пользователя"""
    if email.count('@') == 1:
        name, domain = email.split('@')
        if domain.count('.') > 0:
            return True
        else:
            return False
    else:
        return False


def valid_day(day):
    """ Проверяет на валидность ввода деня рождения пользователя"""
    try:
        day = int(day)
        if 0 < day < 32:
            return True
        else:
            return False
    except ValueError:
        return False
    else:
        return True


def valid_month(month):
    """ Проверяет на валидность ввода месяца рождения пользователя"""
    try:
        month = int(month)
        if 0 < month < 13:
            return True
        else:
            return False
    except ValueError:
        return False
    else:
        return True


def valid_year(year):
    """ Проверяет на валидность ввода года рождения пользователя"""
    if len(year) != 4:
        return False
    try:
        year = int(year)
        if 1959 < year < 2010:
            return True
        else:
            return False
    except ValueError:
        return False
    else:
        return True


def valid_height(height):
    """ Проверяет на валидность ввода роста пользователя"""
    try:
        height = round(float(height), 2)
        if 1 < height < 3:
            return True
        else:
            return False
    except ValueError:
        return False
    else:
        return True


def valid_user_id(user_id):
    """ Проверяет на валидность ввода индификатора пользователя"""
    try:
        user_id = int(user_id)
    except ValueError:
        return False
    else:
        return True
