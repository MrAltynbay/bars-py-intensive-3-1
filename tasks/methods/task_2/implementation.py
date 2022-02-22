from tasks.common import MyException


class ClassFather:

    def register(self):
        if self.__class__ == ClassFather:
            raise MyException
        self.registered_list.append(self.__class__)

    def get_name(self):
        if self.__class__ in self.registered_list:
            return self._name
        else:
            raise MyException
    _name = None
    registered_list = []


class User1(ClassFather):
    _name = '1'


class User2(ClassFather):
    _name = '1'

