'''
File: animal_bird.py
Description: This module defines the Bird subclass used by the zoo system. The Bird class extends the
             abstract Animal class and represents avian species stored within the zoo. It provides
             bird-specific attributes and behaviours.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''

from .animal import Animal

class Bird(Animal):
    """ A subclass of Animal representing avian species within the zoo system.
        This class validates bird species against predefined data and provides
        behaviour specific to bird objects. """


    def __init__(self, name: str, species: str, age: int):
        """ Creates a Bird object and validates that the species exists in the bird database.
            Parameters:
                - name: string
                    The name of the bird object.
                - species: string
                    The species of the bird object.
                - age: integer
                    The age of the bird object in years."""
        super().__init__(name, species, age)


    def make_sound(self):
        """ Produces the characteristic sound of the bird object using species data. """
        info = self.DATA[self.species]
        sound = info.get("sound")
        print (f'{self.name}: "{sound}"\n')

    def eat(self):
        """ Unique eat method that takes into account dietary needs of animal. """
        diet = self.DATA[self.species]["diet"]
        if diet == "carnivore":
            food = "meat"
        if diet == "herbivore":
            food = "plants"
        if diet == "omnivore":
            food = "plants and meat"
        self.__hungry = False
        print (f"{self.__name} ate {food} is no longer hungry.")
