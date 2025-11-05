'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from animal_mammal import Mammal
from animal_bird import Bird
from animal_reptile import Reptile
from zoo_data import *

class Enclosure:
    ENCLOSURES = ENCLOSURES


    def __init__(self, size: int, env_type: str):
        self.__contains = []
        self.__size = size
        if env_type not in ENCLOSURES:
            raise ValueError(f"Invalid enclosure type: {env_type}")

        self.__type = env_type
        self.__cleanliness = 0


    def report(self):
        print(f"Cleanliness: /5\n"
              f"Animals: {self.__contains}\n")


    def store_animal(self, animal: Animal):
        if isinstance(animal,Mammal):
            animal_data = MAMMAL_DATA[animal.name]
        if isinstance(animal, Bird):
            animal_data = BIRD_DATA[animal.name]
        if isinstance(animal, Reptile):
            animal_data = REPTILE_DATA[animal.name]

        enclosure_type = animal_data["enclosure"]

        if enclosure_type != self.__type:
            print (f"cannot store {animal.name} in {self.__type} enclosure")
            return

        if self.__contains != []:
            contained = self.__contains[0]
            if contained != animal.name:
                print (f"cannot store {animal.name} in this enclosure as enclosure occupied by different species")


