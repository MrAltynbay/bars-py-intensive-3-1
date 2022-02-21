from datetime import date


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """

    year, month, day = some_date.year, some_date.month, some_date.day
    days_in_month = {1: 31,
                     2: 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28,
                     3: 31,
                     4: 30,
                     5: 31,
                     6: 30,
                     7: 31,
                     8: 31,
                     9: 30,
                     10: 31,
                     11: 30,
                     12: 31,
                     }

    if day == days_in_month[month]:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    elif month == 12:
        month = 1
        year += 1
    else:
        day += 1

    return date(year, month, day)

