"""
Напишите модуль find_athlete.py поиска ближайшего к пользователю атлета. Логика работы модуля такова:
- запросить идентификатор пользователя;
- если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю;
- если пользователя с таким идентификатором нет, вывести соответствующее сообщение.
"""
def find_athlete(id, session):
    """
    Производит поиск ближайшего к пользователю атлета
    """

