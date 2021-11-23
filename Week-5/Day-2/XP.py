## XP - Ex-1

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Russian(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# my_cats = [Bengal('Kity', 4), Chartreux('Mimi', 5), Russian('Lily', 3)]
#
# my_pets = Pets(my_cats)
#
# my_pets.walk()


## XP - Ex-2

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking!"

    def run_speed(self):
        return (self.weight / (self.age * 10))

    def fight(self, other_dog):
        if other_dog.run_speed() > self.run_speed():
            print(f"{other_dog.name} Won the fight")
        else:
            print(f"{self.name} Won the fight")

x1 = Dog("billy", 12, 110)
x2 = Dog("bob", 9, 100)
x3 = Dog("rock", 6, 70)

x1.bark()
x1.fight(x3)
x2.fight(x1)
x3.fight(x2)



# XP Ex-3

import main as dogFile

class PetDog(dogFile.Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.name = name
        self.trained = trained


    def trained(self, trained=True):
        return Dog.bark()

    def play(self, *args):
        print(f"{self.name} are all playing together")

    def do_a_trick(self):
        if self.trained == True:
            tricks = [f'{self.name} does a barrel roll', f'{self.name} stands on his back legs',
                      f'{self.name} shakes your hand', f'{self.name} plays dead']
            print(random.choices(tricks))


new_dog1 = PetDog("boby", 2, 10)
new_dog = PetDog("tom", 5, 20)
new_dog1.play()


