from staff import Staff
from animal import Animal
from health_entry import Entry
from enclosure import Enclosure

class Keeper(Staff):

    def __init__(self, name, age, gender, birthday):
        super().__init__(name, age, gender, birthday)


    def report_issue(self, animal: Animal,  date: str, issue: str, details: str, severity: int, treatment: str):
        log_entry = Entry(date, issue, details, severity, treatment)
        animal.add_log_entry(log_entry)

    def feed(self, animal: Animal):
        pass

    def clean_enclosure(self, enclosure: Enclosure):
        pass

    def clean_animal(self, animal: Animal):
        pass


