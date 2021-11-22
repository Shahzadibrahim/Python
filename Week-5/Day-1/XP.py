# XP Ex-1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.cat_name = cat_name
        self.cat_age = cat_age

cat1 = Cat('Lucy',3)
cat2 = Cat('Milo',2)
cat3 = Cat('Lily',5)

def oldest(list_of_cats):
    list_of_ages = []

    for cat in list_of_cats:
        list_of_ages.append(cat.cat_age)
    return max(list_of_ages), list_of_cats[list_of_ages.index(max(list_of_ages))].cat_name
list_of_cats = [cat1, cat2, cat3]

print(f'The oldest cat is {oldest(list_of_cats)[1]} and is {oldest(list_of_cats)[0]} years old.')


# Ex- 2

class Dog:
    def __init__(self, name, height=23):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high!') if type(self.height) == int else print(
            f'{self.height} is not a num')

    def details(self):
        print(self.name, self.height)

    def actions(self):
        self.jump()
        self.bark()


davids_dog = Dog('rex', 22)
davids_dog.details()
davids_dog.actions()

sarahs_dog = Dog('Teacup', 20)
sarahs_dog.details()
sarahs_dog.actions()

bigger_dog = sarahs_dog.name if sarahs_dog.height > davids_dog.height else davids_dog.name
print(bigger_dog)


# Ex- 3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold","and she’s buying a stairway to heaven"]).sing_me_a_song()


# Ex - 4

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} already exists")

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
            if animal_sold in self.animals:
                self.animals.remove(animal_sold)
            else:
                print(f"{animal_sold} not in the zoo")

    def sort_animals(self):
        self.animals.sort()
        self.animals = [list(filter(lambda animal: animal[0] == l, self.animals)) for l in sorted(list(set([animal[0] for animal in self.animals])))]

    def get_groups(self):
        for animal in self.animals:
            print(animal)

ramat_gan_safari = Zoo('Ramat Gan Safari')

ramat_gan_safari.add_animal('lion')
ramat_gan_safari.add_animal('giraffe')
ramat_gan_safari.add_animal('zebra')
ramat_gan_safari.add_animal('tiger')
ramat_gan_safari.add_animal('elephant')
ramat_gan_safari.add_animal('monkey')
ramat_gan_safari.add_animal('beer')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('zebra')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
ramat_gan_safari.get_animals()


