'''
File: animal_mammal.py
Description: This module defines the Mammal subclass used by the zoo system. The Mammal class extends the
             abstract Animal class and represents mammalian species stored within the zoo. It provides
             mammal-specific attributes and behaviours.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''

from .animal import Animal

class Mammal(Animal):
    """ A subclass of Animal representing mammalian species within the zoo system.
        This class validates mammal species against predefined data and provides
        behaviours and attributes specific to mammals. """


    def __init__(self, name: str, species: str, age: int):
        """ Creates a Mammal object and validates that the species exists in the mammal database.
            Parameters:
                - name: string
                    The name of the mammal object.
                - species: string
                    The species of the mammal object.
                - age: integer
                    The age of the mammal object in years."""
        super().__init__(name, species, age)


    def make_sound(self):
        """ Produces the characteristic sound of the mammal object using species data. """
        info = self.DATA[self.species]
        sound = info.get("sound")
        print (f'{self.name}: "{sound}"\n')


