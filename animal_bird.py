'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.'''

from animal import Animal
from zoo_data import BIRD_DATA

class Bird(Animal):
    BIRDS = list(BIRD_DATA.keys())

    def __init__(self, name: str, species: str, age: int):
        super().__init__(name, species, age)

        if species not in self.BIRDS:
            raise ValueError(f"Bird: {species} not in database")

    def make_sound(self):
        print("Squaaaak")
