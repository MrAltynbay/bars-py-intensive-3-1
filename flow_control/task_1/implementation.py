def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    numbers = []
    for i in range(1000, 2000):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)
    return numbers
