# защищенный метод _start_engine

class Car:

    def _start_engine(self):
        return "Запускается мотор"

    def run(self):
        return self._start_engine()


if __name__ == '__main__':
    car = Car()

    print(car.run())


# Полиморфные методы ;)
class Motorbike:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a motorbike. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("whoaaah")


class Truck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a truck. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("whoooooooooooooooooooooh")


cat1 = Motorbike("Honda GL 1800", 10)
dog1 = Truck("KAMAZ", 20)

for car in (cat1, dog1):
    car.make_sound()
    car.info()
    car.make_sound()


# Множественное наследование
class A:
    def __init__(self):
        super().__init__()
        self.aa = 2


class B:
    def __init__(self):
        super().__init__()
        self.ab = 3


class C(A, B):
    pass


c = C()
print(c.aa, c.ab)
