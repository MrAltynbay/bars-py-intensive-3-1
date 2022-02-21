from datetime import datetime


def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    year = datetime.now().year
    days_in_month = {'январь': 31,
                     'февраль': 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28,
                     'март': 31,
                     'апрель': 30,
                     'май': 31,
                     'июнь': 30,
                     'июль': 31,
                     'август': 31,
                     'сентябрь': 30,
                     'октябрь': 31,
                     'ноябрь': 30,
                     'декабрь': 31,
                     }
    if month in days_in_month:
        return days_in_month[month]
    else:
        return 0
