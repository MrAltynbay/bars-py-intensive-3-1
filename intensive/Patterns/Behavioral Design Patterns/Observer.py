from abc import ABC, abstractmethod


class AbstractNotificationSystem(ABC):
    '''
        Абстрактный класс для объявления методов управления подписчиками
    '''
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class SpotifyNotificationSystem(AbstractNotificationSystem):
    '''
        Система уведомлений сервиса Spotify
    '''

    def __init__(self):
        self.__observers = set()

    def attach(self, observer):
        self.__observers.add(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.notify_user()


class AbstractObserver(ABC):
    '''
        Абстрактный класс подписчика
    '''
    @abstractmethod
    def notify_user(self):
        pass


class SpotifyUser(AbstractObserver):
    '''
        Пользователь сервиса Spotify
    '''

    def __init__(self, name):
        self.name = name

    def notify_user(self):
        print(f'{self.name}, уведомление для вас ...')


# 5 пользователей(подписчиков)
user1 = SpotifyUser('Павел')
user2 = SpotifyUser('Андрей')
user3 = SpotifyUser('Салават')
user4 = SpotifyUser('Антон')
user5 = SpotifyUser('Максим')

# Система уведомлений Spotify
spotify_system = SpotifyNotificationSystem()

# Подключаем всех подписчиков к системе уведомлений
spotify_system.attach(user1)
spotify_system.attach(user2)
spotify_system.attach(user3)
spotify_system.attach(user4)
spotify_system.attach(user5)

# Присылаем всем уведомление
spotify_system.notify()

# Убираем из подписчиков 1,3,5 пользователя
spotify_system.detach(user1)
spotify_system.detach(user3)
spotify_system.detach(user5)

# Опять всех уведомляем
spotify_system.notify()
