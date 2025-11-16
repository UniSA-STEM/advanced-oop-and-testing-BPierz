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


class Animal(ABC):
    """ An abstract class representing a generic animal object within the zoo system.
           This class provides shared attributes and behaviours for all animals, including
           basic state information and core interactions such as eating, drinking, and sleeping. """

    def __init__(self, name: str, species: str, age: int):
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
        self.__in_enclosure = None
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
        """ Returns a concise string representation for debugging and internal displays. """
        return f"{self.__name}: {self.__species}\n"

    def __eq__(self, other):
        """ Determines equality between two animal objects based on matching name and species. """
        if self.__species == other.species:
            if self.__name == other.name:
                return True

    @property
    def log(self):
        """ Returns the internal log data for this animal object. """
        return self.__log
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
    @property
    def in_enclosure(self):
        """ Returns the ID of the Enclosure in which the animal object is currently in. """
        return self.__in_enclosure
    @in_enclosure.setter
    def in_enclosure(self, in_enclosure):
        """ Sets the ID of the Enclosure in which the animal object is currently in. """
        self.__in_enclosure = in_enclosure

    @treatment.setter
    def treatment(self, treatment: bool):
        """ Sets the treatement status of the animal. """
        self.__treatment = treatment

    @abstractmethod
    def make_sound(self):
        """ Produces the characteristic sound of the animal object. """
        pass

    def eat(self):
        """ Allows the animal object to eat and updates its hunger state. """
        self.__hungry = False
        print (f"{self.__name} ate and is no longer hungry.")

    def drink(self):
        """ Allows the animal object to drink and updates its thirst state. """
        self.__thirsty = False
        print (f"{self.__name} drank and is no longer thirsty.")

    def sleep(self):
        """ Allows the animal object to sleep and updates its sleep state. """
        self.__asleep = True
        print(f"{self.__name} has fallen asleep.")

    def add_log_entry(self, log_entry):
        self.__log.append(log_entry)

