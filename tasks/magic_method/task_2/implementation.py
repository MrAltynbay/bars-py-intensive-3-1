class MathClock:
    def __init__(self):
        self.minutes = 0

    def get_time(self):
        minutes = self.minutes % 60
        hours = (self.minutes // 60) % 24
        return f'{hours:02}:{minutes:02}'

    def __add__(self, other):
        self.minutes += other
        return self.minutes

    def __sub__(self, other):
        self.minutes -= other
        return self.minutes

    def __mul__(self, other):
        self.minutes = self.minutes + other * 60
        return self.minutes

    def __truediv__(self, other):
        self.minutes = self.minutes - other * 60
        return self.minutes
