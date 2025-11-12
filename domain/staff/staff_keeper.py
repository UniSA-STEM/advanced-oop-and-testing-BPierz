from domain.staff.staff import Staff
from domain.animals.animal import Animal
from domain.enclosures.enclosure import Enclosure
from exceptions import *

class Keeper(Staff):

    def __init__(self, name, age, gender, birthday, id):
        super().__init__(name, age, gender, birthday, id)
        self.role = "Keeper"
        self.__assigned_enclosures = []
        self.__working_enclosure = None

    def __repr__(self):
        super().__repr__()
        return (f"Currently Working on: {self.__working_enclosure}"
                f"Assigned enclosures: {self.__assigned_enclosures}")


    def accept_assignment (self, enclosure: Enclosure):
        self.__assigned_enclosures.append(enclosure)

    def get_assigned_enclosure(self, enclosure_id: str):
        if self.__assigned_enclosures == []:
            raise NoAssignedEnclosuresError

        for enclosure in self.__assigned_enclosures:
            if enclosure_id == enclosure.id:
                return enclosure

        return None

    def set_working_enclosure(self, enclosure_id: str):
        enclosure = self.get_assigned_enclosure(enclosure_id)
        if enclosure is None: raise EnclosureNotAvailableError
        self.__working_enclosure = enclosure

    def clean_enclosure(self):
        self.__working_enclosure.be_cleaned()

    def feed_animals(self):
        print(f"{self.name} is feeding animals in {self.__working_enclosure}")
        for animal in self.__working_enclosure.contains:
            animal.eat()



