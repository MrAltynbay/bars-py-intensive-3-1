"""
Что будет выведено после выполнения кода? Почему?
"""


def print_msg(number):
    def printer():
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)


print_msg(9)

"""
Будет выведено:
3
3

Сначала вызывается функция print_msg с переменной number равной 9, затем вызывается функция printer,
в которой написано nonlocal number это означает, что это ссылка на number, которую передали с 
функцией print_msg, затем идет присвоение переменной number значения 3 и вывод, потом после работы
функции printer идет вывод переменной number, которая равна 3, потому что изменилась внутри функции
printer.
"""
