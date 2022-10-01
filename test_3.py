from typing import Annotated


class Animal:
    # legs = 4
    # tail = True
    # can_fly = False
    # nickname = "Fluffy"
    # eats_meat = True
    # i like using sane common default values whenever possible
    def __init__(self, legs=4, tail=True, can_fly=False, nickname="", eats_meat=True):
        self.legs = legs
        self.tail = tail
        self.can_fly = can_fly
        self.nickname = nickname
        self.eats_meat = eats_meat

    def make_noise(self):
        print(f"Animal Noise from {self.nickname}")

# print uses __str__ - the human readable representation of the object
    def __str__(self):
        return f"{self.nickname} is an animal with {self.legs} legs and {self.tail} tail"   

# __repr__ is the machine readable representation of the object used by list etc
    def __repr__(self):
        return f"Animal({self.legs}, {self.tail}, {self.can_fly}, {self.nickname}, {self.eats_meat})"

tom = Animal(legs=4, tail=True, can_fly=False, nickname="Tom", eats_meat=True) # so tom is an instance of Animal class
Animal.make_noise()
# print(tom.tail)
# print("Can Fly?", tom.can_fly)
# print("Eats meat?", tom.eats_meat)
# tom.is_cat = True # you can add more attributes to the object later on
# # not good practice to add attributes to the object after it has been created but you can do it
