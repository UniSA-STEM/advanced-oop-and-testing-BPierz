from domain.enclosures.enclosure import Enclosure
from domain.animals.animal import Animal
from domain.animals.animal_mammal import Mammal
from domain.animals.animal_bird import Bird
from domain.animals.animal_reptile import Reptile
from domain.records.cleaning_task import CleaningTask
from domain.records.health_entry import Entry
from domain.staff.staff import Staff
from domain.staff.staff_keeper import Keeper
from domain.staff.staff_veterinarian import Veterinarian
from collections import defaultdict
from exceptions import *
from domain.records.feeding_task import FeedingTask

class ZooSystem:
    ANIMAL_TYPES = ['Mammal', 'Bird', 'Reptile']

    def __init__(self, zoo_name: str):
        self.__zoo_name = zoo_name
        self.__enclosures = []
        self.__animals = []
        self.__staff = []
        self.__uncompleted_tasks = defaultdict(list)
        self.__completed_tasks = defaultdict(dict)
        self.__health_records = defaultdict(dict)
        self.__feeding_schedule = defaultdict(dict)
        self.__cleaning_schedule = defaultdict(dict)


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
    @property
    def uncompleted_tasks(self):
        return self.__uncompleted_tasks


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

    def get_task(self, task_id: str):
        for category, task in self.__uncompleted_tasks:
            if task.id == task_id:
                return task

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

        animal.in_enclosure = enclosure.id

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
        self.__health_records[animal.name][date] = log_entry

    # Returns health record per animal
    def get_health_record(self, animal_name: str):
        animal_record = self.__health_records[animal_name]
        return animal_record


    # Schedule feeding across zoo for keeper staff
    def schedule_feeding_auto(self):
        feeding_schedule = {}
        for enclosure in self.__enclosures:
            hungry = [animal.name for animal in enclosure.contains if animal.hungry]
            if hungry:
                feeding_schedule[enclosure.id] = hungry
                if len(hungry) == len(enclosure.contains):
                    feeding_schedule[enclosure.id] = ["All Animals"]

        feeding_tasks = []
        for enclosure_id, animals in feeding_schedule.items():
            task = FeedingTask(enclosure_id, animals)
            feeding_tasks.append(task)

        self.__uncompleted_tasks["Feeding"].extend(feeding_tasks)


    # Schedule cleaning for staff
    def schedule_cleaning_auto(self):
        need_cleaning = [enclosure for enclosure in self.__enclosures if enclosure.cleanliness < 3]
        cleaning_tasks = []

        for enclosure in need_cleaning:
            cleaning_tasks.append(CleaningTask(enclosure.id))

        self.__uncompleted_tasks["Cleaning"].extend(cleaning_tasks)

    # Assign a task to staff member
    def assign_task_to_staff(self, staff_id: str, task_id:str = None):
        staff = self.get_staff(staff_id)
        task = self.get_task(task_id)

        if task.type == "Feeding" or "Cleaning" and staff.role != "Keeper":
            raise InvalidStaffRoleError('Can only assign Keepers to Feedings and Cleanings')

        staff.tasks.append(task)
        task.assigned = True
        task.assigned_to = staff_id

    def get_staff_tasks (self, staff_id: str):
        staff = self.get_staff(staff_id)
        assigned_tasks = staff.tasks
        return assigned_tasks

