import math
from abc import ABC, abstractmethod


class AbstractStrategy(ABC):
    '''
        Абстрактный класс стратегии
    '''
    @abstractmethod
    def build(self, x, y, height):
        pass


class Square(AbstractStrategy):
    '''
        Стратегия - Квадрат
    '''
    def build(self, x, y, height):
        return 4 * x * height


class Circle(AbstractStrategy):
    '''
        Стратегия - Круг
    '''
    def build(self, x, y, height):
        return math.ceil(math.pi * x * height)


class Ellipse(AbstractStrategy):
    '''
        Стратегия - Эллипс
    '''
    def build(self, x, y, height):
        return math.ceil(2 * math.pi * math.sqrt((x ** 2 + y ** 2)/8) * height)


class HouseBuilder:
    '''
        Класс HouseBuilder скрывает реализацию рассчетов
    '''
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: AbstractStrategy):
        self.strategy = strategy

    def calculate(self, x, y, height):
        print(f'Количество блоков, необходимых для строительства дома, равно  {self.strategy.build(x, y, height)}')


house_builder = HouseBuilder()
house_builder.set_strategy(Square())
house_builder.calculate(10, 10, 20)

house_builder.set_strategy(Circle())
house_builder.calculate(10, 10, 20)

house_builder.set_strategy(Ellipse())
house_builder.calculate(10, 20, 20)
