'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure
from staff import Staff
from animal_mammal import Mammal

# Creating Animal object of subclass Mammal
MotoMoto = Mammal("Moto Moto", "Hippopotamus", 5)

# Testing string conversion method
print(MotoMoto)
# Testing mammal sound making method
MotoMoto.make_sound()


