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


    def __init__(self, size: int, env_type: str, id_code: str):
        self.__contains = []
        self.__size = size
        if env_type not in ENCLOSURES:
            raise ValueError(f"Invalid enclosure type: {env_type}")
        self.__type = env_type
        self.__id_code = id_code
        self.__cleanliness = 0

    def __eq__(self, other):
        if isinstance(other, Enclosure):
            return self.__id_code == other.id
        return False

    @property
    def id(self):
        return self.__id_code
    @property
    def contains(self):
        return self.__contains


    def __repr__(self):
        return f"Enclosure: {self.__id_code}"

    def report(self):
        print(f"Cleanliness: /5\n"
              f"Animals: {self.__contains}\n")

    def can_store(self, animal: Animal):

        if animal.enclosure.lower() != self.__type.lower():
            return False, "animal needs different enclosure type"

        if self.__contains != []:
            contained = self.__contains[0]
            if contained != animal.species:
                return False, "enclosure already storing different species"

        return True

    def store(self, animal: Animal):
        self.__contains.append(animal)

