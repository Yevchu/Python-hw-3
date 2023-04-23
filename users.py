from random import randint
from datetime import datetime

names = ['Андрій', 'Богдан', 'Віктор', 'Григорій', 'Дмитро', 'Євген', 'Іван', 'Костянтин', 'Лев', 'Максим', 'Назар', 'Олександр', 'Петро', 'Роман', 'Сергій', 'Тарас', 'Уляна', 'Федір', 'Христина', 'Цезар']

users = []

def create_new_user(names: list):

    for el in range(len(names)):
        year = randint(1950, 2005)
        month = randint(1, 12)
        if month == 1:
            day = randint(1, 31)
        if month == 2:
            day = randint(1, 28)
        if month == 3:
            day = randint(1, 31)
        if month == 4:
            day = randint(1, 30)
        if month == 5:
            day = randint(1, 31)
        if month == 6:
            day = randint(1, 30)
        if month == 7:
            day = randint(1, 31)
        if month == 8:
            day = randint(1, 31)
        if month == 9:
            day = randint(1, 30)
        if month == 10:
            day = randint(1, 31)
        if month == 11:
            day = randint(1, 30)
        if month == 12:
            day = randint(1, 31)
        birth_day = datetime(year=year, month=month, day=day).date()
        users.append({'name' : names[el], 'birthday' : birth_day})
        
create_new_user(names)
