def test_function():                                         #ПРОСТРАНСТВО ИМЕН ин
    def inner_function():                                    # создайте фунцию внутри функции
        print("Я в области видимости функции test_function") # функция печатает значение

    inner_function()                                         # вызов функции внутри функции test_function


test_function()                                              # вызов фунции вне функции  test_function
