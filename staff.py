'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Staff:

    def __init__(self, name, age, gender, birthday):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__birthday = birthday

    def feed(self, animal):
        pass

    def read_log(self, animal: Animal):
        log = animal.log
        print(f"{animal.name}'s log:")

        for entry in log:
            print(f"Date: {entry.date} | Issue: {entry.issue} | Severity: {entry.str_severity()}")




