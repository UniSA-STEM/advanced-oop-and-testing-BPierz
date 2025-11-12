from domain.staff.staff import Staff
from domain.animals.animal import Animal
from domain.records.health_entry import Entry
from exceptions import *

class Veterinarian(Staff):

    def __init__(self, name, age, gender, birthday, id):
        super().__init__(name, age, gender, birthday, id)
        self.role = "Veterinarian"
        self.__assigned_animals = []
        self.__working_animal = None

    def __repr__(self):
        super().__repr__()
        return (f"Currently Treating: {self.__working_animal}"
                f"Assigned Animals: {self.__assigned_animals}")

    def accept_assignment(self, animal: Animal):
        self.__assigned_animals.append(animal)

    def get_assigned_animal(self, animal_name: str):
        if self.__assigned_animals == []:
            raise NoAssignedAnimalsError

        for element in self.__assigned_animals:
            if animal_name == element.name:
                return element
        return None

    def stop_working_animal(self, animal: Animal):
        animal.treatment = False

    def set_working_animal(self, animal_name: str):
        previous_animal = self.__working_animal
        if previous_animal != None:
            self.stop_working_animal(previous_animal)

        new_animal = self.get_assigned_animal(animal_name)

        if new_animal is None: raise AnimalNotAvailableError

        self.__working_animal = new_animal
        new_animal.treatment = True

    def report_issue(self, animal: Animal,  date: str, issue: str, details: str, severity: int, treatment: str):
        log_entry = Entry(date, issue, details, severity, treatment)
        animal.add_log_entry(log_entry)

