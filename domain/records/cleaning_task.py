'''
File: cleaning_task.py
Description: This module defines the CleaningTask subclass used by the zoo system. The CleaningTask class
             extends the abstract Task class and represents enclosure-cleaning operations scheduled within
             the zoo. It provides behaviour for generating task identifiers and formatting task details
             specific to enclosure cleaning work.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''

from exceptions import IncompleteTaskError
from domain.records.task import Task


class CleaningTask(Task):

    def __init__(self, enclosure_id: str, date: str):
        if not enclosure_id:
            raise IncompleteTaskError("No Enclosure provided for cleaning task")
        super().__init__(task_type="Cleaning", enclosure_id=enclosure_id, date=date)

    def generate_id(self):
        if self.date is None:
            date = "UNS"
            return f"Cln-{self.enclosure_id}-{date}"
        return f"Cln-{self.enclosure_id}-{self.date[:5]}"
