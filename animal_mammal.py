'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.'''

from animal import Animal
from zoo_data import MAMMAL_DATA

class Mammal(Animal):
    DATA = MAMMAL_DATA
    MAMMALS = list(DATA.keys())

    def __init__(self, name: str, species: str, age: int):
        super().__init__(name, species, age)
        self.__enclosure = self.DATA[self.species]["enclosure"]

        if species not in self.MAMMALS:
            raise ValueError(f"Mammal: {species} not in database")

    @property
    def enclosure(self):
        return self.__enclosure



    def make_sound(self):
        info = self.DATA[self.species]
        sound = info.get("sound")
        print (f'{self.name}: "{sound}"\n')

