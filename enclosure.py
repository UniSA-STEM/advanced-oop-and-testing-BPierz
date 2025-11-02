'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:

    def __init__(self, size: int, env_type: str, cleanliness: int):
        self.__contains = []
        self.__size = size
        self.__env_type = env_type
        self.__cleanliness = cleanliness

    def report(self):
        print(f"Cleanliness: /5\n"
              f"Animals: {self.__contains}\n")


