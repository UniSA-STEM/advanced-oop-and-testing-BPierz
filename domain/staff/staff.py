'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from domain.animals.animal import Animal


class Staff:

    def __init__(self, name: str, age: int, gender: str, birthday: str, id:str):
        self.__name = name

        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 100")
        self.__age = age

        if gender.lower() not in ["male", "female"]:
            raise ValueError("Gender must be 'male' or 'female'")
        self.__gender = gender

        if not isinstance(birthday, str):
            raise TypeError("Birthday must be a string")

        self.__birthday = birthday
        self.__id = id
        self.__role = None
        self.__tasks = []


    @property
    def id(self):
        return self.__id
    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role
        return

    def __repr__(self):
        role = "Staff Member" if self.__role is None else self.__role
        return f"ID: {self.__id} | Role: {role}"




    def feed_animal(self, animal: Animal):
        print(f"{self.__name} is feeding {animal.name}")
        animal.eat()



