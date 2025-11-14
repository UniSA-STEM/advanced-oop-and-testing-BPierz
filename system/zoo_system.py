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
        self.__tasks_by_date = {}
        self.__reported_issues = defaultdict(list)
        self.__health_records = defaultdict(dict)


    @property
    def health_records(self):
        return self.__health_records

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
    def tasks_by_date(self):
        return self.__tasks_by_date

# Creates enclosure code for identification based on enclosure type and order in enclosure log
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

        raise NoSuchAnimalError('No such animal exists at the Zoo')

# Searches for enclosures owned by self based on id and returns an Enclosure object
    def get_enclosure(self, enclosure_id: str):
        lookup_id = str(enclosure_id).strip()
        for i in self.__enclosures:
            if i.id == lookup_id:
                return i
        raise NoSuchEnclosureError('No such enclosure exists at the Zoo')

# Searches for staff owned by self based on id and returns Staff object
    def get_staff(self, staff_id: str):
        lookup_id = str(staff_id).strip()
        for staff in self.__staff:
            if staff.id == lookup_id:
                return staff

        raise NoSuchStaffError('No such staff member exists at the Zoo')

    def get_staff_id(self, staff_name: str):

        for staff in self.__staff:
            if staff.name == staff_name:
                return staff.id

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

        if role != None:

            if role.lower() not in ['keeper', 'administrator', 'veterinarian']:
                raise ValueError('Invalid staff role (must be keeper, administrator, or veterinarian)')

            if role.lower() == 'keeper':
                new_staff = Keeper(name, age, gender, birthday, staff_id)
            if role.lower() == 'veterinarian':
                new_staff = Veterinarian(name, age, gender, birthday, staff_id)

        else:
            new_staff = Staff(name, age, gender, birthday, staff_id)

        self.__staff.append(new_staff)

    def remove_staff(self, staff_id: str):
        staff = self.get_staff(staff_id)  # will raise NoSuchStaffError if not found

        # Role-specific checks
        if staff.role == "Veterinarian" and staff.working_animal is not None:
            raise CannotRemoveStaffError("Can not remove staff while staff is working on animals")

        if staff.role == "Keeper" and staff.working_enclosure is not None:
            raise CannotRemoveStaffError("Can not remove staff while staff is working on enclosure")

        # Unassign all their tasks
        for task in staff.tasks:
            task.assigned = False
            task.assigned_to = None
        staff.tasks.clear()

        # Finally remove staff from system
        self.__staff.remove(staff)



# removes enclosure from own enclosures
    def remove_enclosure(self, enclosure_id: str):

        enclosure = self.get_enclosure(enclosure_id)
        animals = enclosure.contains

        if animals:
            raise CannotRemoveEnclosureError('Can only remove Enclosures without animals currently stored')

        keepers_id = enclosure.keepers
        for id in keepers_id:
            keeper = self.get_staff(id)
            keeper.assigned_enclosures.remove(enclosure)
            if keeper.working_enclosure == enclosure:
                keeper.working_enclosure = None

        self.__enclosures.remove(enclosure)

# Removes animal from own animals and deletes health information
    def remove_animal(self, animal_name: str):
        animal = self.get_animal(animal_name)

        enclosure = animal.in_enclosure
        vets = [staff for staff in self.__staff if staff.type == "Veterinarian"]

        if animal.treatment == True:
            raise CannotRemoveAnimalError('Can not remove animals in treatment')
        if enclosure:
            enclosure.contains.remove(animal)
        if animal_name in self.__health_records:
            del self.__health_records[animal_name]

        for vet in vets:
            if animal in vet.assigned_animals:
                vet.assigned_animals.remove(animal)
            if animal in vet.working_animal:
                vet.working_animal = None

        self.__animals.remove(animal)

# Assigns animals to enclosures
    def assign_animal_to_enclosure(self, animal_name: str, enclosure_id: str):
        animal = self.get_animal(animal_name)
        enclosure = self.get_enclosure(enclosure_id)

        if enclosure.can_store(animal):
            enclosure.store(animal)
        animal.in_enclosure = enclosure.id

    def get_enclosure_animals (self, enclosure_id: str):
        enclosure = self.get_enclosure(enclosure_id)
        animals = enclosure.contains
        return animals

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
        enclosure.keepers.append(keeper.id)

    # Report health issues
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

    def get_date_key(self, date: str = None):
        return date if date is not None else "UNSCHEDULED"

    def get_or_create_date_slot(self, date: str = None):
        date_key = self.get_date_key(date)

        if date_key not in self.__tasks_by_date:
            self.__tasks_by_date[date_key] = {
                "uncompleted": {},
                "completed": {}
            }
        return self.__tasks_by_date[date_key]


    def add_task(self, task, date: str = None, staff_id: str = None):

        slot = self.get_or_create_date_slot(date)
        bucket = slot["uncompleted"]

        key = staff_id if staff_id is not None else "UNASSIGNED"

        if key not in bucket:
            bucket[key] = []

        bucket[key].append(task)

    def schedule_feeding_auto(self, date: str = None):

        feeding_schedule = {}
        for enclosure in self.__enclosures:
            hungry = [animal.name for animal in enclosure.contains if animal.hungry]
            if hungry:
                feeding_schedule[enclosure.id] = hungry
                if len(hungry) == len(enclosure.contains):
                    feeding_schedule[enclosure.id] = ["All Animals"]


        date_key = self.get_date_key(date)
        existing_ids = set()
        if date_key in self.__tasks_by_date:
            for bucket in self.__tasks_by_date[date_key]["uncompleted"].values():
                for t in bucket:
                    existing_ids.add(t.id)
            for bucket in self.__tasks_by_date[date_key]["completed"].values():
                for t in bucket:
                    existing_ids.add(t.id)

        for enclosure_id, animals in feeding_schedule.items():
            task = FeedingTask(enclosure_id, animals)
            if task.id not in existing_ids:
                self.add_task(task, date=date)


    # Schedule cleaning for staff

    def schedule_cleaning_auto(self, date: str = None):
        need_cleaning = [enclosure for enclosure in self.__enclosures if enclosure.cleanliness < 3]

        date_key = self.get_date_key(date)
        existing_ids = set()
        if date_key in self.__tasks_by_date:
            for bucket in self.__tasks_by_date[date_key]["uncompleted"].values():
                for t in bucket:
                    existing_ids.add(t.id)
            for bucket in self.__tasks_by_date[date_key]["completed"].values():
                for t in bucket:
                    existing_ids.add(t.id)

        for enclosure in need_cleaning:
            task = CleaningTask(enclosure.id)
            if task.id not in existing_ids:
                self.add_task(task, date=date)

    def assign_task_to_staff(self, staff_id: str, task_id: str):
        staff = self.get_staff(staff_id)

        date_key, state, owner_id, task = self._find_task_in_schedule(task_id)


        if state != "uncompleted":
            raise InvalidTaskAssignmentError("Cannot assign a completed task.")

        if task.type in ("Feeding", "Cleaning") and staff.role != "Keeper":
            raise InvalidStaffRoleError("Can only assign Keepers to Feedings and Cleanings")

        if task.type == "Treatment" and staff.role != "Veterinarian":
            raise InvalidStaffRoleError("Can only assign Veterinarians to Treatments")


        slot = self.__tasks_by_date[date_key]
        uncompleted = slot["uncompleted"]


        uncompleted[owner_id].remove(task)
        if not uncompleted[owner_id]:
            del uncompleted[owner_id]


        if staff_id not in uncompleted:
            uncompleted[staff_id] = []
        uncompleted[staff_id].append(task)


        task.assigned = True
        task.assigned_to = staff_id
        staff.tasks.append(task)

    def get_all_tasks(self):

        result = {
            "uncompleted": [],
            "completed": []
        }

        for date_key, slot in self.__tasks_by_date.items():
            for staff_id, tasks in slot.get("uncompleted", {}).items():
                result["uncompleted"].extend(tasks)

            for staff_id, tasks in slot.get("completed", {}).items():
                result["completed"].extend(tasks)

        return result

    def get_uncompleted_tasks(self):
        return self.get_all_tasks()["uncompleted"]
    def get_completed_tasks(self):
        return self.get_all_tasks()["completed"]


    def get_staff_tasks(self, staff_id: str):
        staff = self.get_staff(staff_id)

        result = {}

        for date_key, slot in self.__tasks_by_date.items():

            staff_tasks = {
                "uncompleted": slot.get("uncompleted", {}).get(staff_id, []),
                "completed": slot.get("completed", {}).get(staff_id, [])
            }

            if staff_tasks["uncompleted"] or staff_tasks["completed"]:
                result[date_key] = staff_tasks

        return result

    def get_date_tasks(self, date: str):

        date_key = date if date is not None else "UNSCHEDULED"

        slot = self.__tasks_by_date.get(date_key)
        if slot is None:
            raise NoSuchDateinScheduleError

        return {
            "uncompleted": dict(slot.get("uncompleted", {})),
            "completed": dict(slot.get("completed", {})),
        }

    def get_unscheduled_tasks(self):

        slot = self.__tasks_by_date.get("UNSCHEDULED")

        if slot is None:
            return {
                "uncompleted": {},
                "completed": {}
            }

        return {
            "uncompleted": dict(slot.get("uncompleted", {})),
            "completed": dict(slot.get("completed", {})),
        }

    def get_unassigned_tasks_for_date(self, date: str):

        date_key = date if date is not None else "UNSCHEDULED"

        slot = self.__tasks_by_date.get(date_key)
        if slot is None:
            return []

        uncompleted = slot.get("uncompleted", {})
        return uncompleted.get("UNASSIGNED", [])

    def create_task_manual(self, task_type: str, enclosure_id: str = None, animal_names: list[str] = None):
        normalised_type = task_type.capitalize()

        existing_ids = {t.id for t in self.get_uncompleted_tasks()} | {t.id for t in self.get_completed_tasks()}
        if normalised_type == "Feeding":
            if enclosure_id is None or not animal_names:
                raise IncompleteTaskError("Feeding task requires an enclosure ID and at least one animal name.")

            task = FeedingTask(enclosure_id, animal_names)

            if task.id not in existing_ids:
                self.add_task(task, date=None)
            return task

        if normalised_type == "Cleaning":
            if enclosure_id is None:
                raise IncompleteTaskError("Cleaning task requires an enclosure ID.")

            task = CleaningTask(enclosure_id)

            if task.id not in existing_ids:
                self.add_task(task, date=None)

            return task

        raise InvalidTaskTypeError(f"Unknown task type: {task_type}")

