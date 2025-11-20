'''
File: keeper.py
Description: This module defines the Keeper subclass used by the zoo system. The Keeper class extends the
             Staff class and provides behaviours related to enclosure care, feeding tasks, and taking care of animals.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''

from domain.staff.staff import Staff
from domain.enclosures.enclosure import Enclosure
from domain.animals.animal import Animal
from exceptions import *

class Keeper(Staff):
    """ A subclass of Staff representing a zoo-keeper within the zoo system.
        This class manages keeper-specific responsibilities, including working
        in assigned enclosures, performing cleaning tasks, and feeding animals.
        It stores information about assigned enclosures and the enclosure the
        keeper is currently working in. """

    def __init__(self, name, age, gender, birthday, id):
        """ Creates a Keeper object and initialises keeper-specific attributes.
            Parameters:
                - name: string
                    The full name of the keeper.
                - age: integer
                    The age of the keeper in years.
                - gender: string
                    The gender of the keeper.
                - birthday: string
                    The date of birth of the keeper.
                - id: string
                    The unique identification code of the keeper."""

        super().__init__(name, age, gender, birthday, id)
        self.role = "Keeper"
        self.__assigned_enclosures = []
        self.__working_enclosure = None

    def __str__(self):
        """ Returns a formatted string representation of the keeper object. """
        if self.__working_enclosure is None:
            working = "Nothing"
        else:
            working = self.__working_enclosure.id
        base = super().__str__()
        return f"{base} | Assigned Enclosures: {len(self.__assigned_enclosures)} | Currently Working: {working}"

    @property
    def assigned_enclosures(self):
        """ Returns the list of enclosures assigned to this keeper. """
        return self.__assigned_enclosures

    @assigned_enclosures.setter
    def assigned_enclosures(self, assigned_enclosures):
        """ Updates the list of enclosures assigned to this keeper. """
        self.__assigned_enclosures = assigned_enclosures

    @property
    def working_enclosure(self):
        """ Returns the enclosure that this keeper is currently working on. """
        return self.__working_enclosure

    @working_enclosure.setter
    def working_enclosure(self, working_enclosure):
        """ Updates the enclosure that this keeper is currently working on. """
        self.__working_enclosure = working_enclosure

    def accept_assignment (self, enclosure: Enclosure):
        """ Assigns an enclosure to this keeper unless it is already assigned.
                    Parameters:
                        - enclosure: Enclosure
                            The enclosure object being assigned to the keeper."""
        if enclosure in self.__assigned_enclosures:
            raise DuplicateError (f"Enclosure {enclosure} already assigned to this Keeper")

        self.__assigned_enclosures.append(enclosure)

    def get_assigned_enclosure(self, enclosure_id: str):
        """ Retrieves an assigned enclosure based on an enclosure id.
            Parameters:
                - enclosure_id: string
                    The identifier of the enclosure to retrieve.
            Returns:
                - enclosure: Enclosure or None
                    The assigned enclosure object if found, otherwise None. """

        if self.__assigned_enclosures == []:
            raise NoAssignedEnclosuresError

        for enclosure in self.__assigned_enclosures:
            if enclosure_id == enclosure.id:
                return enclosure

        return None

    def set_working_enclosure(self, enclosure_id: str):
        """ Sets the enclosure this keeper is currently working in.
            Parameters:
                - enclosure_id: string
                    The identifier of the assigned enclosure to work in."""
        enclosure = self.get_assigned_enclosure(enclosure_id)
        if enclosure is None: raise EnclosureNotAvailableError
        self.__working_enclosure = enclosure

    def clean_enclosure(self):
        """ Cleans the enclosure the keeper is currently working in. """
        self.__working_enclosure.be_cleaned()

    def feed_animals(self, food: str):
        """Feeds all animals located in the enclosure the keeper is working in with the given food.
           Each animal decides whether it can eat this food (diet, sleep state, etc.)."""
        if self.__working_enclosure is None:
            raise EnclosureNotAvailableError("Keeper is not currently working in an enclosure.")

        print(f"{self.name} fed all animals in enclosure {self.__working_enclosure.id} with {food}")

        for animal in self.__working_enclosure.contains:
            try:
                animal.eat(food)
            except WrongFoodError as e:
                # Animal rejects food (wrong diet, asleep, not hungry, etc.)
                print(f"Could not feed {animal.name}: {e}")

    def feed_animal(self, animal: Animal, food: str):
        """Keeper attempts to feed a single animal with the given food."""
        print(f"{self.name} fed {animal.name} with {food}")
        animal.eat(food)

    def health_check(self, animal_name:str = None, enclosure_id:str = None):

        if animal_name is None and enclosure_id is None:
            found_any = False
            for enclosure in self.__assigned_enclosures:
                for animal in enclosure.contains:
                    if animal.ailment:
                        print(f"{self.id}: {animal.name} is in need of medical attention!")
                        found_any = True
            if not found_any:
                print(f"No animals need medical attention!")

        enclosures_to_check = self.__assigned_enclosures
        if enclosure_id:
            enclosures_to_check = [ e for e in self.__assigned_enclosures if e.id == enclosure_id ]
            if not enclosures_to_check:
                print(f"{self.id} is not assigned to enclosure {enclosure_id}.")
            else:
                enclosures_to_check = self.__assigned_enclosures

        if animal_name:
            for enclosure in self.__assigned_enclosures:
                for animal in enclosure.contains:
                    if animal.name == animal_name:
                        if animal.ailment:
                            print(f"{self.id}: {animal.name} is in need of medical attention!")
                        else:
                            print(f"{self.id}: {animal.name} is not in need of medical attention!")
                        return
            print (f"{animal_name} is not in keepers assigned enclosures.")

        if enclosure_id:
            enclosure = enclosures_to_check[0]
            found_any = False
            for animal in enclosure.contains:
                if animal.ailment:
                    print(f"{self.id}: {animal.name} is in need of medical attention!")
                    found_any = True
            if not found_any:
                print("No animals in this enclosure need medical attention.")




