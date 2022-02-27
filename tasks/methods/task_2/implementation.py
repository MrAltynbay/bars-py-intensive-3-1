from tasks.common import MyException


class ClassFather:
    @classmethod
    def register(cls):
        if cls == ClassFather:
            raise MyException
        ClassFather.registered_list.append(cls)

    @classmethod
    def get_name(cls):
        if cls in ClassFather.registered_list:
            return cls._name
        else:
            raise MyException
    _name = None
    registered_list = []


class User1(ClassFather):
    _name = '1'


class User2(ClassFather):
    _name = '1'

