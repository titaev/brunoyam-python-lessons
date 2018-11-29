from calc import history, operations

history.load()

while True:
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("0. Выход")

    p = int(input("Выберите действие: "))
    if p == 1:
        a = float(input("Введите первое слагаемое: "))
        b = float(input("Введите второе слагаемое: "))
        result = operations.add(a, b)
        history.append("add", result, a, b)
        print("Результат:", result, end="\n\n") 
    elif p == 2:
        a = float(input("Введите уменьшаемое: "))
        b = float(input("Введите вычитаемое: "))
        result = operations.sub(a, b)
        history.append("sub", result, a, b)
        print("Результат:", result, end="\n\n")
    elif p == 3:
        a = float(input("Введите первый множитель: "))
        b = float(input("Введите второй множитель: "))
        result = operations.mul(a, b)
        history.append("mul", result, a, b)
        print("Результат:", result, end="\n\n")
    elif p == 4:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        result = operations.div(a, b)
        print("Результат:", result, end="\n\n")
    elif p == 0:
        history.save()
        print("Работа программы завершена")
        break