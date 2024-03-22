import calendar
def find_day_of_week(month, day, year):
    n = calendar.weekday(year, month, day)
    day_of_week = calendar.day_name[n]
    return day_of_week.upper()

