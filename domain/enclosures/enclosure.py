'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from domain.animals.animal import Animal
from domain.animals.animal_mammal import Mammal
from domain.animals.animal_bird import Bird
from domain.animals.animal_reptile import Reptile
from zoodata.zoo_data import *
from exceptions import *

class Enclosure:
    ENCLOSURES = ENCLOSURES


    def __init__(self, size: int, env_type: str, id_code: str):
        self.__contains = []

        if not isinstance(size, int):
            raise TypeError("size must be an integer representing square meters")

        self.__size = size

        if not isinstance(env_type, str):
            raise TypeError("env_type must be an string representing an environment type")

        if env_type not in ENCLOSURES:
            raise ValueError(f"Enviornment '{env_type}' cannot be found in data base")


        self.__type = env_type
        self.__id_code = id_code
        self.__cleanliness = 5
        self.__keepers = []

    def __eq__(self, other):
        if isinstance(other, Enclosure):
            return self.__id_code == other.id
        return False

    def __str__(self):
        animals = [animal.name for animal in self.__contains]
        if animals == []:
            animals_str = "Nothing"
        animals_str = "\n ".join(animals)
        keepers_str = ', '.join(self.keepers)
        return (f"-----------------------\n"
                f"Enclosure ID: {self.__id_code}\n"
                f"Type: {self.__type}\n"
                f"Contains: {animals_str}\n"
                f"Keepers Assigned: {keepers_str}\n"
                f"-----------------------\n")

    @property
    def id(self):
        return self.__id_code
    @property
    def contains(self):
        return self.__contains
    @property
    def cleanliness(self):
        return self.__cleanliness
    @property
    def keepers(self):
        return self.__keepers
    @keepers.setter
    def keepers(self, keepers):
        self.__keepers = keepers
    @property
    def type(self):
        return self.__type



    def __repr__(self):
        return f"Enclosure: {self.__id_code}"

    def report(self):
        print(f"Cleanliness: {self.__cleanliness}/5\n"
              f"Animals: {self.__contains}\n")

    def can_store(self, animal: Animal):

        if animal.enclosure.lower() != self.__type.lower():
           raise IncompatibleEnclosureError ("animal needs different enclosure type")

        if self.__contains != []:
            contained = self.__contains[0]
            if contained.species != animal.species:
                raise IncompatibleEnclosureError ("enclosure already storing different species")

        return True

    def store(self, animal: Animal):
        self.__contains.append(animal)

    def be_cleaned(self):
        self.__cleanliness += 1


