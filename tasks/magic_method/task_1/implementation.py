class Multiplier:
    """Родительский класс для арифмитических операций"""
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return int(self.value)

    def __add__(self, other):
        new_val = self.value + other.value
        return Multiplier(new_val)

    def __sub__(self, other):
        new_val = self.value - other.value
        return Multiplier(new_val)

    def __mul__(self, other):
        new_val = self.value * other.value
        return Multiplier(new_val)

    def __truediv__(self, other):
        new_val = self.value / other.value
        return Multiplier(new_val)


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        super().__init__(value * 100)


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        super().__init__(value * 1000)


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        super().__init__(value * 1000000)


