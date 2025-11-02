'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.'''

from animal import Animal
from zoo_data import REPTILE_DATA

class Reptile(Animal):
    REPTILES = list(REPTILE_DATA.keys())


    def __init__(self, name: str, species: str, age: int):
        super().__init__(name, species, age)

        if species not in self.REPTILES:
            raise ValueError(f"Reptile: {species} not in database")


    def make_sound(self):
        print("Hissssss")