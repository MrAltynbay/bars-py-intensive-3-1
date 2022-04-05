from dataclasses import dataclass
from recordpack.provider import ObjectListProvider, DjangoModelProvider


@dataclass(init=False)
class GridItem:
    """
    Пример класса элемента грида
    """
    id: int
    last_name: str = ''
    first_name: str = ''
    password: str = ''

    def __init__(self, id=None, context=None) -> None:
        self.id = id
        self.first_name = 'name is' + str(id)
        self.last_name = 'last  name is' + str(id)
        self.password = 'password is' + str(id)
        super().__init__()


# Тестовый набор данных, чтобы не использовать БД
test_data = [GridItem(i) for i in range(1, 10)]


class TestProvider(ObjectListProvider):
    """
    Пример провайдера списковых данных
    """
    def _preprocess_record(self, obj, context=None):
        return obj

    def save(self, obj):
        # автогенерация ID для новых записей
        if obj.id is None:
            obj.id = len(test_data) + 1
        super().save(obj)


class ModelProvider(DjangoModelProvider):
    """
        Провайдер для модели User
    """
    def _preprocess_record(self, obj, context=None):
        return obj

    def save(self, obj):
        # автогенерация ID для новых записей
        if obj.id is None:
            obj.id = len(test_data) + 1
            test_data.append(obj)
        try:
            super().save(obj)
        except BaseException:
            # не успел реализовать, чтобы появлялось предупреждение, что такой username уже существует, поэтому
            # оставил плохую затычку
            obj.username = obj.username + str(obj.id)
            super().save(obj)

