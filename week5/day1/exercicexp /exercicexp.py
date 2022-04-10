# import time
# class RPG_CHARACTER():
#     def __init__(self, name, strength, health, stamina, intelligence):
#         self.name = name
#         self.strength = strength
#         self.stamina = stamina
#         self.intelligence = intelligence
#         self.is_dead = False
#         self.character_class = "Warrior"
#         self.health = health
#         self.level = 0
#         print(f"RPG CHARACTER {self.name} INSTANTIATED!")
    
#     def __repr__(self):
#         return f"{self.name}'s' stats:\nlevel: {self.level}\nstrength: {self.strength}\nstamina: {self.stamina}\nintelligenct: {self.intelligence}\nclass: {self.character_class}"
#     def walk(self):
#         print(f"{self.name} is walking...")
#     def jump(self):
#         print(f"{self.name} is jumping...")
#     def run(self):
#         print(f"{self.name} is running...")
#     def strike(self, monster):
#         print(f"{self.name} is striking {monster.name}")
#         monster.health -= self.strength
#     def life_bar(self):
#         if self.health < 0:
#             self.is_dead = True
#             print(f"{self.name} is dead!")
#         print(f"{self.name}'s health: {self.health}")
# class Monster():
#     def __init__(self, name, level, health, strength):
#         self.name = name
#         self.level = level
#         self.health = health
#         self.strength = strength
#         self.is_dead = False
#     def strike(self, hero):
#         print(f"{self.name} is striking {hero.name}")
#         hero.health -= self.strength
        
#     def life_bar(self):
#         if self.health < 0:
#             self.is_dead = True
#             print(f"{self.name} is dead!")
#         print(f"{self.name}'s health: {self.health}")
# joe = RPG_CHARACTER("Joe", 100, 200, 75, 20)
# zina = RPG_CHARACTER("Zina", 120, 300, 150, 100)
# print(joe)
# print()
# print(zina)
# print()
# print(zina.level)
# monster = Monster("Kraken", 2, 500, 4)

# while zina.is_dead == False:
#     time.sleep(0.2)
#     zina.strike(monster)
#     monster.life_bar()

#     if monster.is_dead:
#         break
#     monster.strike(zina)
#     zina.life_bar()
#     time.sleep(0.2)





# Exercice 1 

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat_list = [Cat("Bob", 6),Cat("George", 9),Cat("Tom", 2)]





# oldest_cat = cat_list[0]
# for cat in cat_list:

#         if oldest_cat.age < cat.age:

#             oldest_cat = cat

# print('Maximum value:', oldest_cat.age)


# print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# Exercice 2 

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height


#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):

#         print(f"{self.name} jumps {self.height*2} cm high!”.")

# tom = Dog("Tom", 10)
# bob = Dog("Bob", 18)

# tom.bark()
# tom.jump()


# davids_dog = Dog("Rex", 50)
# print(f"{davids_dog.name}  {davids_dog.height}")
# davids_dog.bark()
# davids_dog.jump()


# sarahs_dog = Dog("Teacup", 20)
# print(f"{sarahs_dog.name}  {sarahs_dog.height}")
# sarahs_dog.bark()
# sarahs_dog.jump()

# if sarahs_dog.height > davids_dog.height:
#     sarahs_dog.winner = True
#     davids_dog.winner = False

# else:
#     davids_dog.winner = True
#     sarahs_dog.winner = False

# print(f"Davids_dog win: {davids_dog.winner} ")


# Exercice 3 

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for word in self.lyrics:
#             print(word)

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
         


# stairway.sing_me_a_song()


# Exercice 4


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.new_animal = []


    def add_animal(new_animal):

    