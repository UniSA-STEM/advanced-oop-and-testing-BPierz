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
        self.__in_enclosure = None
        self.__hungry = True
        self.__thirsty = True
        self.__asleep = False
        self.__treatment = False
        self.__treated_by = None

    def __str__(self):
        if self.__in_enclosure == None:
            enclosure = f"{self.__name} is currently not in an enclosure (temporary storage)!"
        else:
            enclosure = self.__in_enclosure
        if self.__hungry == True or self.__treatment == True or self.__thirsty == True:
            important = (f"{self.__name} needs attention (Possibly hungry or in treatment)")
        else:
            important = (f"{self.__name} is not in need of immediate attention)")

        return (f"-----------------------\n"
                f"Name: {self.__name}\n"
                f"Species: {self.__species}\n"
                f"Age: {self.__age}\n"
                f"In Enclosure: {enclosure}\n"
                f"Important: {important}\n"
                f"-----------------------\n")

    def __repr__(self):
        return f"{self.__name}: {self.__species}\n"

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
    @property
    def hungry(self):
        return self.__hungry
    @property
    def treatment(self):
        return self.__treatment
    @property
    def treated_by(self):
        return self.__treated_by
    @property
    def in_enclosure(self):
        return self.__in_enclosure
    @in_enclosure.setter
    def in_enclosure(self, in_enclosure):
        self.__in_enclosure = in_enclosure


    @treatment.setter
    def treatment(self, treatment: bool):
        self.__treatment = treatment


    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        self.__hungry = False
        print (f"{self.__name} ate and is no longer hungry.")

    def drink(self):
        self.__thirsty = False
        print (f"{self.__name} drank and is no longer thirsty.")

    def sleep(self):
        self.__asleep = True
        print(f"{self.__name} has fallen asleep.")

    def add_log_entry(self, log_entry):
        self.__log.append(log_entry)

