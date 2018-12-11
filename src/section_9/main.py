class Class:
    static = "static"

    def __init__(self):
        self.dynamic = "dynamic"

obj = Class()

dictionary = {
    "string": "string",
    "int": 80,
    "float": 34.5,
    "list": ["field1", 2, 3.75, "field4"],
    "tuple": ("field1", 2, 3.75, "field4"),
    "set": {"field1", 2, 3.75, "field4"},
}

# Имея 3 объекта (Class, obj, dictionary), вывести их на экран и  сериализовать (сохранить) их с помощью pickle, json, yaml в файлы "test.pk", "test.json", "test.yml" соответственно.
# После загрузить их из файлов и вывести на экран.