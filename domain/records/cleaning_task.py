from exceptions import IncompleteTaskError
from task import Task


class CleaningTask(Task):

    def __init__(self, enclosure_id: str):
        if not enclosure_id:
            raise IncompleteTaskError("No Enclosure provided for cleaning task")
        super().__init__(task_type="Cleaning", enclosure_id=enclosure_id)

    def _generate_id(self):
        return f"Cln-{self.enclosure_id}"

    def _details_str(self):
        return "Cleaning required\n"