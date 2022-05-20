"""Декораторы — это, по сути, "обёртки", которые дают нам возможность изменить поведение функции, не изменяя её код.

Создадим свой декоратор "вручную":"""


def my_decorator(function_to_decorate):
    def wrapper():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функция
        print("А я - код, срабатывающий после")

    return wrapper


def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")


stand_alone_function = my_decorator(stand_alone_function)
stand_alone_function()


@my_decorator
def stand_alone_function():
    print("Оставь меня в покое")

stand_alone_function()

# То есть, декораторы в python — это просто синтаксический сахар для конструкций вида: stand_alone_function = my_decorator(stand_alone_function)

