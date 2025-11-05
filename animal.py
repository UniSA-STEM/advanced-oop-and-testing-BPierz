'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.'''

# Import to make Animal an abstract class
from abc import ABC, abstractmethod


class Animal(ABC):


    def __init__(self, name: str, species: str, age: int):

        self.__name = name
        self.__species = species
        self.__age = age
        self.__hunger = 0
        self.__thirst = 0
        self.__log = []

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Species: {self.__species}\n"
                f"Age: {self.__age}\n")

    def __repr__(self):
        return (f"{self.__name}: {self.__species}\n")

    def __eq__(self, other):
        if self.__species == other.species:
            if self.__name == other.name:
                return True

    @property
    def log(self):
        return self.__log
    @property
    def name(self):
        return self.__name
    @property
    def species(self):
        return self.__species

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        pass

    def drink(self):
        pass

    def sleep(self):
        pass


    def add_log_entry(self, log_entry):
        self.__log.append(log_entry)

