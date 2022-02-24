class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """
    def __init__(self, *args):
        self.tuple_arguments = args

    def __getitem__(self, item):
        return self.tuple_arguments[item]

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        summer = 0
        for val in self.tuple_arguments:
            if value == val:
                summer += 1

        return summer

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """

        for i, val in enumerate(self.tuple_arguments):
            if value == val:
                return i

        raise ValueError

