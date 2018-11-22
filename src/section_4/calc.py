# Сложение
def add():
    a = int(input("Введите первое слагаемое: "))
    b = int(input("Введите второе слагаемое: "))
    result = a + b
    history_append("add", result, a, b)
    return result

# Разность
def sub():
    a = int(input("Введите уменьшаемое: "))
    b = int(input("Введите вычитаемое: "))
    result = a - b
    history_append("sub", result, a, b)
    return result

# Умножение
def mul():
    a = int(input("Введите первый множитель: "))
    b = int(input("Введите второй множитель: "))
    result = a * b
    history_append("mul", result, a, b)
    return result

# Деление
def div():
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    result = a / b
    history_append("div", result, a, b)
    return result

# Возведение в степень
def deg():
    def pow(base):
        result = 1
        while True:
            result *= base
            yield result
    
    base = int(input("Введите основание: "))
    gen = pow(base)
    p = "y"
    while p.lower() == "y" or p.lower() == "yes":
        result = next(gen)
        print("Основание:", result)
        p = input("Вывести следующую степень числа %s? [Y/n] " % base)
    history_append("deg", result, base)

# Загрузка
def load():
    try:
        f = open("history.txt", "r")
    except:
        return
    for line in f:
        line = line.rstrip().split(" ")
        dct = {
            "action": line[0],
            "args": [float(arg) for arg in line[1:-2]],
            "result": float(line[-1]),
        }
        history.append(dct)
    f.close()

# Сохранение
def save():
    f = open("history.txt", "w")
    for h in history:
        string = h["action"] + " "
        string += " ".join(map(str, h["args"])) + " "
        string += str(h["result"]) + "\n" 
        f.write(string)
    f.close()

# Добавление в историю
def history_append(action, result, *args):
    dct = {
        "action": action,
        "args": args,
        "result": result,
    }
    history.append(dct)

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