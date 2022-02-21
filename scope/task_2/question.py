"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

"""
Будет выведено:
Test message
None

Test message будет выведен, потому что после вызова функции transmit_to_space ей передается переменная 
message со значением "Test message", после вызывется функция data_transmitter без аргументов, в которой 
происходит вывод переменной message, но data_transmitter не находит переменную message и ищет ее на уровень
выше, где он ее находит и выводит
None будет выведен, потому что функция transmit_to_space не имеет оператора return, а если его нет, то возвращается
None
"""