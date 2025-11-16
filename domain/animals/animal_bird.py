'''
File: animal_bird.py
Description: This module defines the Bird subclass used by the zoo system. The Bird class extends the
             abstract Animal class and represents avian species stored within the zoo. It provides
             bird-specific behaviours.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''
from exceptions import AnimalAsleepError
from .animal import Animal

class Bird(Animal):
    """ A subclass of Animal representing avian species within the zoo system.
        This class validates bird species against predefined data and provides
        behaviour specific to bird objects. """


    def __init__(self, name: str, species: str, age: int, enclosure: str, diet: list, sound: str):
        """ Creates a Bird object and validates that the species exists in the bird database.
            Parameters:
                - name: string
                    The name of the bird object.
                - species: string
                    The species of the bird object.
                - age: integer
                    The age of the bird object in years."""
        super().__init__(name, species, age, enclosure, diet, sound)

    def move(self):
        """ Represents the specific animal moving"""
        if self.asleep:
            raise AnimalAsleepError (f"{self.name} cannot move as is currently sleeping.")
        print (f"{self.name} flies through the air.")

    def sleep(self):
        """ Represents the specific animal sleeping"""
        print(f"{self.name} tucks its head under its wing.")
        print (super().sleep())
