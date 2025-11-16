'''
File: animal_reptile.py
Description: This module defines the Reptile subclass used by the zoo system. The Reptile class extends the
             abstract Animal class and represents reptilian species stored within the zoo. It provides
             reptile-specific behaviours.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''

from exceptions import AnimalAsleepError
from .animal import Animal


class Reptile(Animal):
    """ A subclass of Animal representing reptilian species within the zoo system.
        This class validates reptile species against predefined data and provides
        behaviours specific to reptiles. """


    def __init__(self, name: str, species: str, age: int, enclosure: str, diet: list, sound: str):
        """ Creates a Reptile object and validates that the species exists in the reptile database.
            Parameters:
                - name: string
                    The name of the reptile object.
                - species: string
                    The species of the reptile object.
                - age: integer
                    The age of the reptile object in years. """
        super().__init__(name, species, age, enclosure, diet, sound)


    def move(self):
        """ Represents the specific animal moving"""
        if self.asleep:
            raise AnimalAsleepError (f"{self.name} cannot move as is currently sleeping.")
        return f"{self.name} slithers or crawls quietly."


    def sleep(self):
        """ Represents the specific animal sleeping"""
        print(f"{self.name} finds a warm rock and gets still.")
        return super().sleep()



