'''
File: animal_mammal.py
Description: This module defines the Mammal subclass used by the zoo system. The Mammal class extends the
             abstract Animal class and represents mammalian species stored within the zoo. It provides
             mammal-specific behaviours.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''
from exceptions import AnimalAsleepError
from .animal import Animal

class Mammal(Animal):
    """ A subclass of Animal representing mammalian species within the zoo system.
        This class validates mammal species against predefined data and provides
        behaviours and attributes specific to mammals. """


    def __init__(self, name: str, species: str, age: int, enclosure: str, diet: list, sound: str):
        """ Creates a Mammal object and validates that the species exists in the mammal database.
            Parameters:
                - name: string
                    The name of the mammal object.
                - species: string
                    The species of the mammal object.
                - age: integer
                    The age of the mammal object in years."""
        super().__init__(name, species, age, enclosure, diet, sound)


    def move(self):
        """ Represents the specific animal moving"""
        if self.asleep:
            raise AnimalAsleepError (f"{self.name} cannot move as is currently sleeping.")
        return f"{self.name} walks on four legs."


    def sleep(self):
        """ Represents the specific animal sleeping"""
        print(f"{self.name} curls up into a soft bundle.")
        return super().sleep()
