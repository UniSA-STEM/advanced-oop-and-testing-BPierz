from domain.enclosures.enclosure import Enclosure
from domain.animals.animal import Animal
from domain.animals.animal_mammal import Mammal
from domain.animals.animal_bird import Bird
from domain.animals.animal_reptile import Reptile
from domain.records.health_entry import Entry
from domain.staff.staff import Staff
from domain.staff.staff_keeper import Keeper
from domain.staff.staff_veterinarian import Veterinarian
from interface.interface import Interface
from collections import defaultdict
from exceptions import *

class ZooSystem:
    ANIMAL_TYPES = ['Mammal', 'Bird', 'Reptile']

    def __init__(self, zoo_name: str):
        self.__zoo_name = zoo_name
        self.__enclosures = []
        self.__animals = []
        self.__staff = []
        self.__health_log = defaultdict(dict)

    @property
    def log(self):
        return self.__health_log

    @property
    def animals(self):
        return self.__animals

    @property
    def staff(self):
        return self.__staff

    @property
    def enclosures(self):
        return self.__enclosures

# Method creates enclosure code for identification based on enclosure type and order in enclosure log
    def create_enclosure_code(self, type: str, size: int) -> str:
        index = type.find(' ')
        id_code = str(size)
        id_code += type[:3]

        if index != -1:
            id_code += type[index + 1: index + 4]

        count = 1
        for enclosure in self.__enclosures:
            if enclosure.type == type:
                count += 1
        id_code += str(count)

        return id_code

# Creates unique ID code for staff members based on name, surname and birthday
    def create_staff_id(self, staff_name: str, staff_birthday: str):
        index = staff_name.find(' ')
        staff_id = staff_name[:3]
        staff_id += staff_name[index + 1:index + 4]
        staff_id += staff_birthday[-2:]
        return staff_id

# Searches for animals in system based on animal name string and returns Animal object
    def get_animal(self, animal_name: str):

        for i in self.__animals:
            if i.name == animal_name:
                return i
        return None

# Searches for enclosures owned by self based on id and returns an Enclosure object
    def get_enclosure(self, enclosure_id: str):
        for i in self.__enclosures:
            if i.id == enclosure_id:
                return i
# Searches for staff owned by self based on id and returns Staff object
    def get_staff(self, staff_id: str):
        for i in self.__staff:
            if i.id == staff_id:
                return i

# Adds new enclosure object to own storage
    def add_enclosure(self, size: int, type: str):
        id_code = self.create_enclosure_code(type, size)
        new_enclosure = Enclosure(size, type, id_code)
        self.__enclosures.append(new_enclosure)

# Adds new Animal of subclass based on type parameter
    def add_animal(self, type, name, species, age):

        if type not in self.ANIMAL_TYPES:
            raise ValueError('Invalid animal type')

        if type == 'Mammal':
            new_animal = Mammal(name, species, age)
        if type == 'Bird':
            new_animal = Bird(name, species, age)
        if type == 'Reptile':
            new_animal = Reptile(name, species, age)

        self.__animals.append(new_animal)

# Adds new Staff object of subclass based on role attribute passed in
    def add_staff(self, name:str, age: int, gender:str, birthday:str, role = None):

        staff_id = self.create_staff_id(name, birthday)

        if gender not in ['Male', 'Female']:
            raise ValueError('Invalid staff gender')

        if role != None:

            if role not in ['Keeper', 'Administrator', 'Veterinarian']:
                raise ValueError('Invalid staff role')

            if role == 'Keeper':
                new_staff = Keeper(name, age, gender, birthday, staff_id)
            if role == 'Veterinarian':
                new_staff = Veterinarian(name, age, gender, birthday, staff_id)

        else:
            new_staff = Staff(name, age, gender, birthday, staff_id)

        self.__staff.append(new_staff)

# removes enclosure from own enclosures
    def remove_enclosure(self, enclosure: Enclosure):
        self.__enclosures.remove(enclosure)

# Removes animal from own animals and deletes health information
    def remove_animal(self, animal_name: str):
        animal = self.get_animal(animal_name)

        if animal_name in self.__health_log:
            del self.__health_log[animal_name]

        self.__animals.remove(animal)

# Assigns animals to enclosures
    def assign_animal_to_enclosure(self, animal_name: str, enclosure_id: str):
        animal = self.get_animal(animal_name)
        enclosure = self.get_enclosure(enclosure_id)

        if enclosure.can_store(animal):
            enclosure.store(animal)

# Assigns animals to veterinarians
    def assign_animal_to_vet(self, animal_name:str, staff_id: str):
        animal = self.get_animal(animal_name)
        vet = self.get_staff(staff_id)

        if vet.role != "Veterinarian":
            raise InvalidStaffRoleError('Can only assign Veterinarians to animals')
        vet.accept_assignment(animal)

# Assigns enclosures to keepers
    def assign_enclosure_to_keeper(self, enclosure_id: str, staff_id: str):
        enclosure = self.get_enclosure(enclosure_id)
        keeper = self.get_staff(staff_id)

        if keeper.role != "Keeper":
            raise InvalidStaffRoleError('Can only assign Keepers to Enclosures')

        keeper.accept_assignment(enclosure)

    # Reports health issues
    def report_issue(self, animal_name: str, date: str, issue: str, details: str, severity: int, treatment: str):
        animal = self.get_animal(animal_name)

        if animal not in self.__animals:
            print(f"Animal is not in the zoo system")

        log_entry = Entry(date, issue, details, severity, treatment)
        animal.add_log_entry(log_entry)
        self.__health_log[animal.name][date] = log_entry

    # Displays health log of health records.
    def display_log(self, animal_name: str):

        print(f"---- {animal_name} Health Records ----")
        for date, entry in self.__health_log[animal_name].items():
            print(entry)
        print(f"---- End of Health Records ----")

    # Schedule feeding for staff
    def to_feed(self):
        need_feeding = [animal for animal in self.__animals if animal.hungry]
        return need_feeding

    # Schedule cleaning for staff
    def to_clean(self):
        need_cleaning = [enclosure for enclosure in self.__enclosures if enclosure.cleanliness < 3]
        return need_cleaning
