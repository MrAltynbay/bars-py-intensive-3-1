from tasks.common import MyException


class Value:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other

    def __sub__(self, other):
        return self.num - other

    def __mul__(self, other):
        return self.num * other

    def __truediv__(self, other):
        if other:
            return self.num / other
        else:
            raise MyException



