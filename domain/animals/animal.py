'''
File: animal.py
Description: This module defines the Animal class and the animal subclass hierarchy used by the zoo system.
             The Animal class is an abstract class and provides shared attributes and behaviours for all animals.
             Subclasses extend this behaviour to represent specific groups including Mammal, Bird, and Reptile,
             These classes model real animals and represent the core data holders for animals within the zoo system.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''


from abc import ABC, abstractmethod
from zoodata.zoo_data import *
from exceptions import *


class Animal(ABC):
    """ An abstract class representing a generic animal object within the zoo system.
           This class provides shared attributes and behaviours for all animals, including
           basic state information and core interactions such as eating, drinking, and sleeping. """

    ANIMAL_DATA = animal_data
    FOOD_ITEMS = all_food_items
    ANIMALS = animals
    ENCLOSURES = all_enclosures

    @abstractmethod
    def __init__(self, name: str, species: str, age: int, enclosure: str, diet: list, sound: str):
        """ Creates an Animal object and initialises shared animal attributes.
                    Parameters:
                        - name: string
                            The name of the animal object.
                        - species: string
                            The species of the animal object.
                        - age: integer
                            The age of the animal object in years."""

        self.__name = name
        self.__species = species
        self.__age = age
        self.__enclosure = enclosure
        self.__diet = diet
        self.__sound = sound

        self.__in_enclosure = None
        self.__ailment = False
        self.__hungry = True
        self.__thirsty = True
        self.__asleep = False
        self.__treatment = False
        self.__treated_by = None

    def __str__(self):
        """ Returns a formatted string representation of the animal object."""
        if self.__in_enclosure == None:
            enclosure = f"{self.__name} is currently not in an enclosure (temporary storage)!"
        else:
            enclosure = self.__in_enclosure

        status = []
        if self.__hungry:
            status.append("hungry")
        if self.__thirsty:
            status.append("thirsty")
        if self.__asleep:
            status.append("sleeping")
        if self.__ailment:
            status.append("in need of medical attention")
        if self.__treatment:
            status.append(f"being treated by {self.__treated_by}")

        if self.__ailment and not self.__treatment:
            status.append("in need of medical attention and not in treatment!")

        if not status:
            status.append("Not in any need")

        status_str = ", ".join(status) + "."

        return (f"-----------------------\n"
                f"Name: {self.__name}\n"
                f"Species: {self.__species}\n"
                f"Age: {self.__age}\n"
                f"In Enclosure: {enclosure}\n"
                f"Status: {status_str}\n"
                f"-----------------------\n")

    def __repr__(self):
        """ Returns a concise string representation for debugging and internal displays. """
        return f"{self.__name}: {self.__species}\n"

    def __eq__(self, other):
        """ Determines equality between two animal objects based on matching name and species. """
        if self.__species == other.species:
            if self.__name == other.name:
                return True

    @property
    def name(self):
        """ Returns the name of the animal object. """
        return self.__name
    @property
    def species(self):
        """ Returns the species of the animal object. """
        return self.__species
    @property
    def hungry(self):
        """ Returns the hungry status of the animal object. """
        return self.__hungry
    @property
    def treatment(self):
        """ Returns the treatment status of the animal object. """
        return self.__treatment
    @property
    def treated_by(self):
        """ Returns the ID of the Veterinarian treated by of the animal object. """
        return self.__treated_by
    @treated_by.setter
    def treated_by(self, treated_by):
        """ Sets the ID of the Veterinarian treating the animal object. """
        self.__treated_by = treated_by

    @property
    def enclosure(self):
        """ Returns the ID of the Enclosure in which the animal object has to be stored in from database. """
        return self.__enclosure
    @property
    def diet(self):
        """ Returns a list of food items that the animal can eat from database. """
        return self.__diet

    @property
    def in_enclosure(self):
        """ Returns the ID of the Enclosure in which the animal object is currently in. """
        return self.__in_enclosure
    @in_enclosure.setter
    def in_enclosure(self, in_enclosure):
        """ Sets the ID of the Enclosure in which the animal object is currently in. """
        self.__in_enclosure = in_enclosure
    @property
    def asleep(self):
        """ Returns True if the animal object is currently sleeping. """
        return self.__asleep
    @property
    def ailment(self):
        """ Returns Ailment status of the animal object. """
        return self.__ailment
    @ailment.setter
    def ailment(self, ailment):
        """ Sets the ailment status of the animal object. """
        if not isinstance(ailment, bool):
            raise TypeError (f"ailment: {ailment} must be a boolean")
        self.__ailment = ailment
    @treatment.setter
    def treatment(self, treatment: bool):
        """ Sets the treatement status of the animal. """
        self.__treatment = treatment
    @property
    def age(self):
        """ Returns the age of the animal object. """
        return self.__age
    @property
    def enclosure(self):
        """ Returns the ID of the Enclosure in which the animal object can be stored. """
        return self.__enclosure
    @hungry.setter
    def hungry(self, hungry):
        """ Sets the hungry status of the animal object. """
        self.__hungry = hungry




    def make_sound(self):
        """ Produces the characteristic sound of the animal object. """
        sound = self.__sound
        print(f'{self.name}: "{sound}"\n')

    def can_eat(self, food: str):
        """Returns True if the food passed in is contained in animal dietary requirements.
            Parameters:
                food: string
                A string representing the food item being fed to animal"""
        if self.__asleep == True:
            raise AnimalAsleepError (f"{self.name} cannot eat as is currently sleeping.")

        return food in self.__diet

    def eat(self, food: str):
        """ Allows the animal object to eat and updates its hunger state. """
        if not self.can_eat(food):
            raise WrongFoodError (f"Animal cannot eat {food}")
        if self.__asleep:
            raise AnimalAsleepError (f"{self.name} cannot eat as is currently sleeping.")

        if not self.__hungry:
            print(f"{self.name} is not hungry right now.")
            return

        self.__hungry = False
        print(f"{self.name} the {self.species.title()} eats {food}.")

    def drink(self):
        """ Allows the animal object to drink and updates its thirst state. """
        if self.__asleep:
            raise AnimalAsleepError(f"{self.name} cannot eat as is currently sleeping.")

        self.__thirsty = False
        print (f"{self.__name} drank and is no longer thirsty.")

    def sleep(self):
        """ Allows the animal object to sleep and updates its sleep state. """
        self.__asleep = True
        print(f"{self.__name} has fallen asleep.")



