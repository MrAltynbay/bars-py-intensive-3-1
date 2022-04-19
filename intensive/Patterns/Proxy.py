from abc import ABCMeta, abstractmethod, ABC
import datetime


class Subject(ABC):
    @abstractmethod
    def get_data(self):
        pass


class RealSubject(Subject):
    def get_data(self):
        return 'private data'


class Proxy(Subject):
    def __init__(self, db):
        self.db = db

    def get_data(self):
        self.write_log()
        return self.db.get_data()

    def write_log(self):
        print('request data in:', datetime.datetime.now())


class User:
    def __init__(self, data_obj):
        self.data_obj = data_obj

    def request_data(self):
        return self.data_obj.get_data()


db = RealSubject()
user1 = User(db)
print(user1.request_data())  # private data
proxy = Proxy(db)
user2 = User(proxy)
print(user2.request_data())  # request data in: 2022-04-19 14:13:35.335993
                             # private data

# 1 юзер(админ) обращается напрямую к бд
# 2 юзер запрашивает данные через прокси
