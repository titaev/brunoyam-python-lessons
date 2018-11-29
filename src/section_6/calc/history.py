history = []

# Загрузка
def load(filename):
    try:
        f = open(filename, "r")
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
def save(filename):
    f = open(filename, "w")
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
