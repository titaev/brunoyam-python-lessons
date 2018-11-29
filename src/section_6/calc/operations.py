# Сложение
def add(a, b):
    result = a + b
    return result

# Разность
def sub(a, b):
    result = a - b
    return result

# Умножение
def mul(a, b):
    result = a * b
    return result

# Деление
def div(a, b):
    result = a / b
    return result

# Главная программа
history = []
load()

while True:
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Степени числа")
    print("0. Выход")

    p = int(input("Выберите действие: "))
    if p == 1:
        print("Результат:", add(), end="\n\n") 
    elif p == 2:
        print("Результат:", sub(), end="\n\n")
    elif p == 3:
        print("Результат:", mul(), end="\n\n")
    elif p == 4:
        print("Результат:", div(), end="\n\n")
    elif p == 5:
        deg()
    elif p == 0:
        save()
        print("Работа программы завершена")
        break