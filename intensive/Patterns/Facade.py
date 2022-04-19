class Water(object):
    '''
    Бутылка воды
    '''

    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def give(self, text):
        if self._count > 0:
            self._count -= 1
        print(text)


class VendingMachine(object):
    '''
    Автомат выдачи продуктов
    '''

    def error(self, msg):
        print(f'Ошибка: {msg}')

    def print_(self, product, text):
        if product.get_count() > 0:
            product.give(text)

        else:
            self.error('Товар закончился')


class Facade(object):
    '''
    Фасад
    '''

    def __init__(self):
        self._vending_machine = VendingMachine()
        self._water = Water(2)

    def give_product(self, text):
        self._vending_machine.print_(self._water, text)


f = Facade()
f.give_product('Выдал товар')  # Выдал товар
f.give_product('Выдал товар')  # Выдал товар
f.give_product('Выдал товар')  # Ошибка: Бумага закончилась
