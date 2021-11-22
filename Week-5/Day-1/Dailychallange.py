
# Daily - Challange

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.quantity = []
    def add_animal(self, new_animal, quantity=0):
        self.animals.append(new_animal)
        self.quantity.append(quantity)

    def get_info(self):
        print(f'{self.name} farm has {self.animals} in quantity of{self.quantity} E-I-E-I-0!')
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep,')
macdonald.add_animal('sheep,')
macdonald.add_animal('goat', 12)


print(macdonald.get_info())