from animal import *



class Place:
    def __init__(self, square, climat):
        self.square = square
        self.climat = climat
        self.animals = []
    
    def add_animal(self, animal):
        if animal.climat != self.climat:
            return
        summ = 0
        for a in self.animals:
            summ += a.square
        if self.square - summ >= animal.square:
            self.animals.append(animal)


white_bear = WhiteBear("Tarasik")
pinguin1 = Pinguin("Gunter")
pinguin2 = Pinguin("Ganter")
horse = Horse("Plotva")
gepard = Gepard("Panda")

place = Place(square=50, climat="cold")

place.add_animal(white_bear)
place.add_animal(pinguin1)
place.add_animal(pinguin2)
place.add_animal(horse)
place.add_animal(gepard)

for animal in place.animals:
    print(animal.name, end=" ")
