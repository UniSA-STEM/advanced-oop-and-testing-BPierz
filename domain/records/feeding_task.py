from exceptions import IncompleteTaskError
from task import Task


class FeedingTask(Task):

    def __init__(self, enclosure_id: str, animal_names: list):
        if animal_names is None and enclosure_id is None:
            raise IncompleteTaskError(
                "No Animal or Enclosure Indicated for Feeding Task"
            )

        self.__animals = animal_names
        super().__init__(task_type="Feeding", enclosure_id=enclosure_id)

    def _generate_id(self):
        count = len(self.__animals) if self.__animals is not None else 0
        return f"Fd-{self.enclosure_id}-{count}"


    @property
    def animals(self):
        return list(self.__animals) if self.__animals is not None else []


    def _details_str(self) -> str:
        if self.__animals is None or len(self.__animals) == 0:
            return "Feed: (no animals listed)\n"

        if self.__animals[0] == "All Animals":
            return "Feed: All Animals\n"

        animals_str = "\n ".join(self.__animals) + "\n"
        return f"Feed:\n {animals_str}"