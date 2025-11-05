from collections import defaultdict

from enclosure import Enclosure
from animal import Animal
from animal_mammal import Mammal
from animal_bird import Bird
from animal_reptile import Reptile
from health_entry import Entry
from collections import defaultdict

class ZooSystem:
    ANIMAL_TYPES = ['Mammal', 'Bird', 'Reptile']

    def __init__(self, zoo_name: str):
        self.__zoo_name = zoo_name
        self.__enclosures = []
        self.__animals = []
        self.__staff = []
        self.__health_log = defaultdict(dict)

    @property
    def log(self):
        return self.__health_log
    @property
    def animals(self):
        return self.__animals


    def get_animal(self, animal_name: str):

        for i in self.__animals:
            if i.name == animal_name:
                return i
        return None


    def add_enclosure(self, size, type):
        new_enclosure = Enclosure(size, type)
        self.__enclosures.append(new_enclosure)

    def add_animal(self, type, name, species, age):

        if type not in self.ANIMAL_TYPES:
            raise ValueError('Invalid animal type')

        if type == 'Mammal':
            new_animal = Mammal(name, species, age)
        if type == 'Bird':
            new_animal = Bird(name, species, age)
        if type == 'Reptile':
            new_animal = Reptile(name, species, age)

        self.__animals.append(new_animal)

    def remove_enclosure(self, enclosure: Enclosure):
        self.__enclosures.remove(enclosure)

    def remove_animal(self, animal_name: str):
        animal = self.get_animal(animal_name)

        if animal_name in self.__health_log:
            del self.__health_log[animal_name]

        self.__animals.remove(animal)

    def assign_animal(self, animal: Animal, enclosure: Enclosure):
        pass

    def assign_staff(self, animal: Animal, enclosure: Enclosure):
        pass

    def report_issue(self, animal_name: str, date: str, issue: str, details: str, severity: int, treatment: str):
        animal = self.get_animal(animal_name)

        if animal not in self.__animals:
            print (f"Animal is not in the zoo system")

        log_entry = Entry(date, issue, details, severity, treatment)
        animal.add_log_entry(log_entry)
        self.__health_log[animal.name][date] = log_entry


    def display_log(self, animal_name: str):

        print(f"---- {animal_name} Health Records ----")
        for date, entry in self.__health_log[animal_name].items():

            print(entry)
        print(f"---- End of Health Records ----")


