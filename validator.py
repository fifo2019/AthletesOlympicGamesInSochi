def valid_gender(gender):
    """ Проверяет на валидность пол пользователя"""
    if gender == 'м' or gender == 'ж':
        return True


def valid_email(email):
    """ Проверяет на валидность адрес почты"""
    if email.count('@') == 1:
        name, domain = email.split('@')
        if domain.count('.') > 0:
            return True
        else:
            return False
    else:
        return False


def valid_day(day):
    """ Проверяет на валидность день"""
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
    """ Проверяет на валидность месяц"""
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
    """ Проверяет на валидность год"""
    if len(year) != 4:
        return False
    try:
        year = int(year)
        if 1930 < year < 2012:
            return True
        else:
            return False
    except ValueError:
        return False
    else:
        return True


def valid_height(height):
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