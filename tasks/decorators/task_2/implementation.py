from tasks.common import MyException


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    cache = {}

    def wrapper(argum):

        if isinstance(argum, int) and argum >= 0:
            key = func.__name__ + str(argum)
            if key in cache:
                return cache[key]
            cache[key] = func(argum)
            return cache[key]
        else:
            raise MyException

    return wrapper

