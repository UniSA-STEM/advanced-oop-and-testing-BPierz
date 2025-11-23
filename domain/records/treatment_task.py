'''
File: treatment_task.py
Description: This module defines the TreatmentTask class.The CleaningTask class
             extends the abstract Task class and represents animal-treatment operations scheduled within
             the zoo. It provides behaviour for generating task identifiers and formatting task details
             specific to animal treatment work.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''


from .task import Task
from exceptions import IncompleteTaskError

class TreatmentTask(Task):

    def __init__(self, animal_id: str, date: str):
        if not animal_id:
            raise IncompleteTaskError("No Animal provided for treatment task")

        super().__init__(task_type="Treatment", animal_id=animal_id, date=date)

    def generate_id(self):
        return f"Tr-{self.animal_id}-{self.date[:5]}"
