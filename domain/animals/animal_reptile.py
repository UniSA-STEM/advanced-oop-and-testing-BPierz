'''
File: animal_reptile.py
Description: This module defines the Reptile subclass used by the zoo system. The Reptile class extends the
             abstract Animal class and represents reptilian species stored within the zoo. It provides
             reptile-specific attributes and behaviours.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''


from .animal import Animal
from zoodata.zoo_data import REPTILE_DATA

class Reptile(Animal):
    """ A subclass of Animal representing reptilian species within the zoo system.
        This class validates reptile species against predefined data and provides
        behaviours specific to reptiles. """

    REPTILES = list(REPTILE_DATA.keys())
    DATA = REPTILE_DATA


    def __init__(self, name: str, species: str, age: int):
        """ Creates a Reptile object and validates that the species exists in the reptile database.
            Parameters:
                - name: string
                    The name of the reptile object.
                - species: string
                    The species of the reptile object.
                - age: integer
                    The age of the reptile object in years. """
        super().__init__(name, species, age)

        if species not in self.REPTILES:
            raise ValueError(f"{species} not in Reptile database")


    def make_sound(self):
        """ Produces the characteristic sound of the reptile object using species data. """
        info = self.DATA[self.species]
        sound = info.get("sound")
        print (f'{self.name}: "{sound}"\n')
