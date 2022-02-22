
def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        wrapper.count += 1
        return wrapper.count

    wrapper.count = 0
    return wrapper
