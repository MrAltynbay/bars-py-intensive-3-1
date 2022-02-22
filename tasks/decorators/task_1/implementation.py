import time


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выпонения функции {func.__name__} составляет {end - start} секунд')
        return result

    return wrapper

