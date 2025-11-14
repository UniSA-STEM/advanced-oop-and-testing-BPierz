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

    def __str__(self):
        if self.__working_enclosure is None:
            working = "Nothing"
        else:
            working = self.__working_enclosure.name
        base = super().__str__()
        return f"{base} | Assigned Enclosures: {len(self.__assigned_enclosures)} | Currently Working: {working}"

    @property
    def assigned_enclosures(self):
        return self.__assigned_enclosures

    @assigned_enclosures.setter
    def assigned_enclosures(self, assigned_enclosures):
        self.__assigned_enclosures = assigned_enclosures

    @property
    def working_enclosure(self):
        return self.__working_enclosure
    @working_enclosure.setter
    def working_enclosure(self, working_enclosure):
        self.__working_enclosure = working_enclosure

    def accept_assignment (self, enclosure: Enclosure):
        if enclosure in self.__assigned_enclosures:
            raise DuplicateError (f"Enclosure {enclosure} already assigned to this Keeper")

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



