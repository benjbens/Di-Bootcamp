# # Exercice 1

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self) -> str:
#         return self.name

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Sphynx(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# my_cats = [Cat("Tom", 3),  Cat("Bob", 5), Cat("George", 8)]

# my_pets = Pets(my_cats)

# my_pets.walk()

# print(my_cats[0])


# Exercice 2 

class Dog:
    def __init__(self,name, age, weight):
        self.name = name 
        self.age = age 
        self.weight = weight

        
    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
           print(f"{self.name} won the fight")
        else:
            print(f"{other_dog.name} won the fight")

dog1 = Dog("Tom",10,20)
dog2 = Dog("Bob",7,25)      
dog3 = Dog("George",1,4)


dog1.fight(dog2)
dog3.bark()


