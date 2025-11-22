'''
File: staff.py
Description: This module defines the Staff class and the staff subclass hierarchy used by the zoo system.
             The Staff class is a parent non-abstract class and provides shared attributes and behaviours for all
             staff members. Subclasses extend this to represent specific roles including Keeper,
             Veterinarian, and Administrator. These classes model real staff members and hold data for staff members
             in the zoo system.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''



class Staff:
    class Staff:
        """ A parent class representing a generic staff member within the zoo system.
            This class provides shared attributes and behaviours for all staff roles.
            Subclasses extend this to model specific staff roles such as Keeper and Veterinarian"""

    def __init__(self, name: str, age: int, gender: str, birthday: str, id: str):
        """ Creates a Staff object and initialises shared staff attributes.
            Parameters:
                - name: string
                    The full name of the staff member.
                - age: integer
                    The age of the staff member in years.
                - gender: string
                    The gender of the staff member.
                - birthday: string
                    The date of birth of the staff member.
                - id: string
                    The unique identification code of the staff member."""
        self.__name = name

        if age < 15 or age > 120:
            raise ValueError("Age must be between 15 and 120")
        self.__age = age

        if gender.lower().strip() not in ["male", "female"]:
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
        """ Returns the unique staff id for this staff member. """
        return self.__id
    @property
    def name(self):
        """ Returns the name of this staff member. """
        return self.__name
    @property
    def age(self):
        """ Returns the age of this staff member. """
        return self.__age
    @property
    def role(self):
        """ Returns the role assigned to this staff member. """
        return self.__role
    @role.setter
    def role(self, role):
        """ Sets the role assigned to this staff member. """
        self.__role = role
        return
    @property
    def tasks(self):
        """ Returns the tasks assigned to this staff member. """
        return self.__tasks
    @tasks.setter
    def tasks(self, tasks):
        """ Sets the tasks assigned to this staff member. """
        self.__tasks = tasks
    @property
    def gender(self):
        """ Returns the gender of this staff member. """
        return self.__gender
    @property
    def birthday(self):
        """ Returns the date of birth of this staff member. """
        return self.__birthday



    def __repr__(self):
        """ Returns a concise string representation used for debugging and internal display. """
        role = "Staff Member" if self.__role is None else self.__role
        return f"ID: {self.__id} | Role: {role}"

    def __str__(self):
        """ Returns a formatted string representation of this staff member, subclasses extend this __str__ method. """
        return f"ID: {self.__id} | Role: {self.__role}"
