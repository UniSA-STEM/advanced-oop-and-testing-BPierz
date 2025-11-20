from .task import Task
from exceptions import IncompleteTaskError

class TreatmentTask(Task):

    def __init__(self, animal_id: str, date: str):
        if not animal_id:
            raise IncompleteTaskError("No Animal provided for treatment task")

        super().__init__(task_type="Treatment", animal_id=animal_id, date=date)

    def generate_id(self):
        return f"Tr-{self.animal_id}-{self.date[:5]}"
