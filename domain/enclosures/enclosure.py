'''
File: enclosure.py
Description: This module defines the Enclosure class used by the zoo system. The Enclosure class models
             real habitat structures that store animal objects and provides attributes and behaviours
             related to habitat type, size, cleanliness, contained animals, and assigned keepers.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''

from domain.animals.animal import Animal
from zoodata.zoo_data import *
from exceptions import *

class Enclosure:
    """ A class representing an enclosure within the zoo system.
        This class models real habitat structures that store animal objects and
        provides behaviours related to habitat type, size, cleanliness, assigned
        keepers, and the animals currently stored in the enclosure. """
    ENCLOSURES = ENCLOSURES


    def __init__(self, size: int, env_type: str, id_code: str):
        """ Creates an Enclosure object and initialises enclosure attributes.
            Parameters:
                - size: integer
                    The size of the enclosure in square meters.
                - env_type: string
                    The environmental type of the enclosure.
                - id_code: string
                    The unique enclosure identification code."""
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
        """ Returns a formatted string representation of the enclosure object. """
        animals = [animal.name for animal in self.__contains]
        if isinstance(other, Enclosure):
            return self.__id_code == other.id
        return False

    def __str__(self):
        """ Returns a formatted string representation of the enclosure object. """
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
        """ Returns the enclosure identification code. """
        return self.__id_code
    @property
    def contains(self):
        """ Returns the list of animals currently stored in the enclosure. """
        return self.__contains
    @property
    def cleanliness(self):
        """ Returns the cleanliness value of the enclosure. """
        return self.__cleanliness
    @cleanliness.setter
    def cleanliness(self, cleanliness):
        """ Sets the cleanliness value of the enclosure. """
        self.__cleanliness = cleanliness
    @property
    def keepers(self):
        """ Returns the keeper_ids assigned to the enclosure. """
        return self.__keepers
    @keepers.setter
    def keepers(self, keepers):
        """ Sets the keeper_ids assigned to the enclosure. """
        self.__keepers = keepers
    @property
    def type(self):
        """ Returns the type of the enclosure. """
        return self.__type
    @property




    def __repr__(self):
        """ Returns a concise string representation of the enclosure object. """
        return f"Enclosure: {self.__id_code}"

    def report(self):
        """ Prints a simple enclosure report including cleanliness and stored animals. """
        print(f"Cleanliness: {self.__cleanliness}/5\n"
              f"Animals: {self.__contains}\n")

    def can_store(self, animal: Animal):
        """ Determines whether an animal can be stored in this enclosure.
                    Parameters:
                        - animal: Animal
                            The animal object being checked against enclosure conditions.
                    Returns:
                        - True: if the enclosure can store the animal."""

        if animal.enclosure.lower() != self.__type.lower():
           raise IncompatibleEnclosureError ("animal needs different enclosure type")

        if self.__contains != []:
            contained = self.__contains[0]
            if contained.species != animal.species:
                raise IncompatibleEnclosureError ("enclosure already storing different species")

        return True

    def store(self, animal: Animal):
        """ Stores an animal object inside the enclosure. """
        self.__contains.append(animal)

    def be_cleaned(self):
        """ Increases the cleanliness level of the enclosure by one point. """
        self.__cleanliness += 1


