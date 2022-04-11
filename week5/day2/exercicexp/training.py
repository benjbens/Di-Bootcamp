# Exercice 3

from exercicexp import Dog
import random

class PetDog(Dog):
    def __init__(self,name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, other_dog):
        print(f"{other_dog.name} and {self.name} all play together")


    def do_a_trick(self):
        sentences = ["does a barrel rol","stands on his back legs", "shakes your hand", "plays dead"]
        sentence = random.choice(sentences)
        print(self.name, sentence)




dog1 = PetDog("Tom",10,20)
dog2 = PetDog("Bob",7,25)      
dog3 = PetDog("George",1,4)

dog1.play(dog2)
dog1.do_a_trick()
dog2.do_a_trick()
dog3.do_a_trick()
dog3.do_a_trick()
