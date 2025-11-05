from staff import Staff
from animal import Animal
from health_entry import Entry

class Veterinarian(Staff):

    def __init__(self, name, age, gender, birthday):
        super().__init__(name, age, gender, birthday)
        self.__assigned_animal = None

    def assign_animal(self, animal: Animal):
        self.__assigned_animal = animal

    def report_issue(self, animal: Animal,  date: str, issue: str, details: str, severity: int, treatment: str):
        log_entry = Entry(date, issue, details, severity, treatment)
        animal.add_log_entry(log_entry)

