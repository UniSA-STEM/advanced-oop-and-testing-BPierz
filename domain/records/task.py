
from abc import ABC, abstractmethod
from exceptions import IncompleteTaskError

class Task(ABC):

    def __init__(self, task_type: str, enclosure_id: str = None, animal_id: str = None, date: str = None):
        self.__type = task_type
        self.__enclosure_id = enclosure_id
        self.__animal_id = animal_id
        self.__date = date
        self.__assigned = False
        self.__assigned_to = None
        self.__complete = False

        self.__id = self._generate_id()

    @abstractmethod
    def _generate_id(self) -> str:
        pass

    @abstractmethod
    def _details_str(self) -> str:
        pass

    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        return self.__type

    @property
    def enclosure_id(self):
        return self.__enclosure_id

    @property
    def animal_id(self):
        return self.__animal_id

    @property
    def assigned(self):
        return self.__assigned

    @assigned.setter
    def assigned(self, value: bool):
        self.__assigned = bool(value)

    @property
    def assigned_to(self):
        return self.__assigned_to

    @assigned_to.setter
    def assigned_to(self, value):
        self.__assigned_to = value

    @property
    def complete(self):
        return self.__complete

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, value):
        self.__date = value

    def mark_complete(self):
        self.__complete = True

    def __str__(self):
        enc_line = f"Enclosure: {self.__enclosure_id}\n" if self.__enclosure_id else ""
        ani_line = f"Animal: {self.__animal_id}\n" if self.__animal_id else ""

        return (
            "---- TASK ----\n"
            f"Scheduled for: {self.__date}\n"
            f"ID: {self.__id}\n"
            f"Type: {self.__type}\n"
            f"{enc_line}{ani_line}"
            f"{self._details_str()}"
            "--------------\n"
        )
