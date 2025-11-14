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

    def __str__(self):
        if self.__working_animal is None:
            working = "Nothing"
        else:
            working = self.__working_animal.name
        base = super().__str__()
        return f"{base} | Assigned Animals: {len(self.__assigned_animals)} | Currently Treating: {working}"


    @property
    def assigned_animals(self):
        return self.__assigned_animals
    @assigned_animals.setter
    def assigned_animals(self, assigned_animals):
        self.__assigned_animals = assigned_animals

    @property
    def working_animal(self):
        return self.__working_animal
    @working_animal.setter
    def working_animal(self, working_animal):
        self.__working_animal = working_animal

    def accept_assignment(self, animal: Animal):
        self.__assigned_animals.append(animal)

    def get_assigned_animal(self, animal_name: str):
        if self.__assigned_animals == []:
            raise NoAssignedAnimalsError

        for element in self.__assigned_animals:
            if animal_name == element.name:
                return element
        return None

    def treat_animal(self, animal_name: str):
        previous_animal = self.__working_animal
        if previous_animal != None:
            self.stop_working_animal(previous_animal)

        new_animal = self.get_assigned_animal(animal_name)

        if new_animal is None: raise AnimalNotAvailableError(f"Animal is not in Vet Assigned Animals")

        self.__working_animal = new_animal

        new_animal.treatment = True
        self.__working_animal.treated_by = self.__id

        for task in self.tasks:
            if task.animal_id == new_animal.id:
                task.complete = True

    def stop_treating_animal(self):
        self.__working_animal.treatment = False
        self.__working_animal.treated_by = None
        self.__working_animal = None



    def report_issue(self, animal_name: str,  date: str, issue: str, details: str, severity: int, treatment: str):
        log_entry = Entry(date, issue, details, severity, treatment)
        animal = self.get_assigned_animal(animal_name)



