import datetime
from users import users


def get_birthdays_per_week(users: dict, start_date: datetime, end_date: datetime) -> dict:

    Monday = ''
    Tuesday = ''
    Wednesday = ''
    Thursday = '' 
    Friday = ''
    
    for user in users:
        if start_date.month <= user['birthday'].month <= end_date.month and start_date.day <= user['birthday'].day <= end_date.day:
            
            if user['birthday'].weekday() == 0:
                Monday += user['name'] + ', '

            if user['birthday'].weekday() == 1:
                Tuesday += user['name'] + ', '
            
            if user['birthday'].weekday() == 2:
                Wednesday += user['name'] + ', '
            
            if user['birthday'].weekday() == 3:
                Thursday += user['name'] + ', '
            
            if user['birthday'].weekday() == 4:
                Friday += user['name'] + ', '
            
            if user['birthday'].weekday() == 5 or user['birthday'].weekday() == 6:
                Monday += user['name'] + ', '

    if len(Monday) < 1:
        Monday = 'Немає інменинників'
    if len(Tuesday) < 1:
        Tuesday = 'Немає інменинників'
    if len(Wednesday) < 1:
        Wednesday = 'Немає інменинників'
    if len(Thursday) < 1:
        Thursday = 'Немає інменинників'
    if len(Friday) < 1:
        Friday = 'Немає інменинників'
    if len(Monday) < 1:
        Monday = 'Немає інменинників'
    
    Monday = Monday.strip(' ').removesuffix(',')
    Friday = Friday.strip(' ').removesuffix(',')
    Tuesday = Tuesday.strip(' ').removesuffix(',')
    Wednesday = Wednesday.strip(' ').removesuffix(',')
    Thursday = Thursday.strip(' ').removesuffix(',')
    
    print(f'Monday: {Monday}\n'
          f'Tuesday: {Tuesday}\n'
          f'Wednesday: {Wednesday}\n'
          f'Thursday: {Thursday}\n'
          f'Friday: {Friday}') 

start_date = datetime.datetime.now().date()
end_date = start_date + datetime.timedelta(days=7)
get_birthdays_per_week(users, start_date, end_date)
