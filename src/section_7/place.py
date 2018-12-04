class Place:
    def __init__(self, square, climat):
        self.square = square
        self.climat = climat
        self.animals = []
    
    def add_animal(self, animal):
        raise NotImplemented