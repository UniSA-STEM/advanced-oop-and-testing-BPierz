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
from zoo_system import ZooSystem
from animal_mammal import Mammal
from staff_veterinarian import Veterinarian

# Creating Animal object of subclass Mammal
#MotoMoto = Mammal("Moto Moto", "Hippopotamus", 5)

# Testing string conversion method
#print(MotoMoto)
# Testing mammal sound making method
#MotoMoto.make_sound()

# Testing adding log entries
# Creating Veterinarian
#Alice = Veterinarian("Alice", 20, "Female", "02/04/2005")

# Veterinarian reports issue on Animal object
#Alice.report_issue(MotoMoto, "04/11/2025", "Is not eating", "MotoMoto has not touched his food for 2 days", 2, "Give appetite medication")
#Alice.report_issue(MotoMoto, "29/12/2026", "Likes them big", "MotoMoto is overweight after appetite medication overdose", 1, "Reduce calories in diet")

# Animal Object log updates
#Alice.read_log(MotoMoto)

ZooSystem = ZooSystem("Simone's Zoo")
ZooSystem.add_animal("Mammal", "MotoMoto", "Hippopotamus", 5)
ZooSystem.report_issue("MotoMoto", "03/12/2024", "Is not eating", "Moto Moto has not touched his food in 2 days", 2, "Give medication")
ZooSystem.report_issue("MotoMoto", "12/12/2024", "Now eats too much", "He is eating everything in sight", 3, "Somebody Stop HIM!")
ZooSystem.add_animal("Bird", "Blue", "Macaw", 10)
ZooSystem.report_issue("Blue", "15/12/2024", "Pecking at own feathers", "Blue is plucking himself, sign of boredom", 2, "Give him toys and a friend so he is not so bored")

print(ZooSystem.log)
print(ZooSystem.animals)
ZooSystem.display_log("MotoMoto")

ZooSystem.remove_animal("Blue")
print(ZooSystem.animals)