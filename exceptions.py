'''
File: exceptions.py
Description: This module defines the custom exception classes used by the zoo system. These exceptions
             provide clear and specific error types for handling invalid operations, missing data, and
             incorrect user input throughout the system. Each exception models a real operational error
             scenario, allowing the zoo system and the Interface module to respond with meaningful and
             user-friendly messages. This module supports robust error handling across all components of
             the zoo system.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''


class AnimalAsleepError(Exception):
    pass

class InvalidStaffRole(Exception):
    pass

class UnassignedAnimalError(Exception):
    pass

class NoAssignedEnclosuresError(Exception):
    pass

class EnclosureNotAvailableError(Exception):
    pass

class AnimalAssignedError(Exception):
    pass

class InvalidStaffRoleError(Exception):
    pass

class NoAssignedAnimalsError(Exception):
    pass

class AnimalNotAvailableError(Exception):
    pass

class AnimalNotExistError(Exception):
    pass

class AnimalUnderTreatmentError(Exception):
    pass

class NoSetAnimalError(Exception):
    pass

class IncompleteTaskError(Exception):
    pass

class CannotRemoveEnclosureError(Exception):
    pass

class CannotRemoveAnimalError(Exception):
    pass

class CannotRemoveStaffError(Exception):
    pass

class AnimalAlreadyAssignedError(Exception):
    pass

class NoSuchDateinScheduleError(Exception):
    pass

class InvalidTaskTypeError(Exception):
    pass

class TaskNotFoundError(Exception):
    pass

class NoSuchAnimalError(Exception):
    pass

class NoSuchEnclosureError(Exception):
    pass

class NoSuchStaffError(Exception):
    pass

class IncompatibleEnclosureError(Exception):
    pass

class DuplicateError(Exception):
    pass

class InvalidDateError(Exception):
    pass

class NoSuchTaskError(Exception):
    pass


