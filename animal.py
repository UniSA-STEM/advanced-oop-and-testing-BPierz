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

        self.name = name
        self._species = species
        self.__age = age
        self.__hunger = 0
        self.__thirst = 0
        self.__log = []



    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Species: {self._species}\n"
                f"Age: {self.__age}\n")

    def __repr__(self):
        return (f"{self._species}: {self.name}\n")

    def __eq__(self, other):
        if self._species == other._species:
            if self.name == other.name:
                return True

    @property
    def log(self):
        return self.__log

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

