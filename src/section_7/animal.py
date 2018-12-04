class Animal:
    def __init__(self, name):
        self.name = name
        self.square = None
        self.climat = None


class WhiteBear(Animal):
    def __init__(self, name):
        self.name = name
        self.square = 40
        self.climat = "cold"


class Pinguin(Animal):
    def __init__(self, name):
        self.name = name
        self.square = 7
        self.climat = "cold"


class Horse(Animal):
    def __init__(self, name):
        self.name = name
        self.square = 200
        self.climat = "warm"


class Gepard(Animal):
    def __init__(self, name):
        self.name = name
        self.square = 30
        self.climat = "hot"
