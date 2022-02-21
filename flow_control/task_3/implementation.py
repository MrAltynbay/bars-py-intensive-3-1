def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    if month == 'январь' or month == 'март' or month == 'май' or month == 'август' or month == 'июль' \
            or month == 'октябрь' or month == 'декабрь':
        return 31
    elif month == 'апрель' or month == 'июнь' or month == 'сентябрь' or month == 'ноябрь':
        return 30
    elif month == 'февраль':
        return 28
    else:
        return 0
