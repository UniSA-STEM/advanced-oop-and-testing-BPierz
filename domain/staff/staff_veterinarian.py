'''
File: veterinarian.py
Description: This module defines the Veterinarian subclass used by the zoo system. The Veterinarian class
             extends the Staff class and provides behaviours related to animal health, treatment tasks,
             and medical care.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''

from domain.staff.staff import Staff
from domain.animals.animal import Animal
from domain.records.health_entry import Entry
from exceptions import *

class Veterinarian(Staff):
    """ A subclass of Staff representing a veterinarian within the zoo system.
        This class manages veterinarian-specific responsibilities, including
        treating animals. """

    def __init__(self, name, age, gender, birthday, id):
        """ Creates a Veterinarian object and initialises veterinarian-specific attributes.
            Parameters:
                - name: string
                    The full name of the veterinarian.
                - age: integer
                    The age of the veterinarian in years.
                - gender: string
                    The gender of the veterinarian.
                - birthday: string
                    The date of birth of the veterinarian.
                - id: string
                    The unique identification code of the veterinarian."""
        super().__init__(name, age, gender, birthday, id)
        self.role = "Veterinarian"
        self.__assigned_animals = []
        self.__working_animal = None

    def __str__(self):
        """ Returns a formatted string representation of the veterinarian object. """
        if self.__working_animal is None:
            working = "Nothing"
        else:
            working = self.__working_animal.name
        base = super().__str__()
        return f"{base} | Assigned Animals: {len(self.__assigned_animals)} | Currently Treating: {working}"


    @property
    def assigned_animals(self):
        """ Returns the list of animals assigned to this veterinarian. """
        return self.__assigned_animals

    @assigned_animals.setter
    def assigned_animals(self, assigned_animals):
        """ Updates the list of animals assigned to this veterinarian. """
        self.__assigned_animals = assigned_animals

    @property
    def working_animal(self):
        """ Returns the animal currently being treated by this veterinarian. """
        return self.__working_animal

    @working_animal.setter
    def working_animal(self, working_animal):
        """ Updates the animal currently being treated by this veterinarian. """
        self.__working_animal = working_animal

    def accept_assignment(self, animal: Animal):
        """ Assigns an animal to this veterinarian for potential treatment.
            Parameters:
                - animal: Animal
                    The animal object being assigned."""
        self.__assigned_animals.append(animal)

    def get_assigned_animal(self, animal_name: str):
        """ Retrieves an assigned animal based on its name.
            Parameters:
                - animal_name: string
                    The name of the animal to retrieve."""
        if self.__assigned_animals == []:
            raise NoAssignedAnimalsError

        for animal in self.__assigned_animals:
            if animal_name == animal.name:
                return animal
        return None


    def treat_animal(self, animal_name: str):
        """ Begins treatment on an assigned animal and updates its medical state.
            Parameters:
                - animal_name: string
                    The name of the animal to treat."""
        previous_animal = self.__working_animal

        new_animal = self.get_assigned_animal(animal_name)

        if new_animal is None:
            raise AnimalNotAvailableError(f"Animal is not in Vet Assigned Animals")
        if not new_animal.ailment:
            raise AnimalHealthyError (f"Animal doesn't require treatment at the moment")
        if previous_animal != None:
            self.stop_treating_animal()

        self.__working_animal = new_animal

        new_animal.treatment = True
        self.__working_animal.treated_by = self.id

        print(f"{self.id} is treating {animal_name}.")

    def stop_treating_animal(self):
        self.__working_animal.treatment = False
        self.__working_animal.treated_by = None

        if self.__working_animal.ailment:
            print(f"{self.id} has stopped treating {self.__working_animal.name} but animal still in need of medical attention.")
            self.__working_animal = None
        else:
            print(f"{self.id} has stopped treating {self.__working_animal.name}")
            self.__working_animal = None

    def heal_animal(self):
        self.__working_animal.ailment = False
        print(f"{self.id} has successfully treated {self.__working_animal.name}.")
        self.stop_treating_animal()

    def health_check(self, animal_name: str = None):

        if animal_name is None:
            for animal in self.__assigned_animals:
                if animal.ailment:
                    print(f"{self.id}: {animal.name} is in need of medical attention!")
                else:
                    print(f"{self.id}: {animal.name} is not in need of medical attention!")
            return

        for animal in self.__assigned_animals:
            if animal_name == animal.name:
                if animal.ailment:
                    print(f"{self.id}: {animal.name} is in need of medical attention!")
                else:
                    print(f"{self.id}: {animal.name} is not in need of medical attention!")
                return

        print(f"{animal_name} is not assigned to {self.id}!")


