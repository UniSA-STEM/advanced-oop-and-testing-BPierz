from domain.animals.animal import Animal
from domain.enclosures.enclosure import Enclosure
from domain.animals.animal_mammal import Mammal
from domain.animals.animal_bird import Bird
from domain.animals.animal_reptile import Reptile
from domain.records.cleaning_task import CleaningTask
from domain.records.health_entry import Entry
from domain.staff.staff import Staff
from domain.staff.staff_keeper import Keeper
from domain.staff.staff_veterinarian import Veterinarian
from zoodata.zoo_data import *
from collections import defaultdict
from exceptions import *
from domain.records.feeding_task import FeedingTask
from domain.records.treatment_task import TreatmentTask
from datetime import datetime


class ZooSystem:
    ANIMAL_TYPES = ['Mammal', 'Bird', 'Reptile']
    ANIMAL_DATA = animal_data
    FOOD_ITEMS = all_food_items
    ANIMALS = animals
    ENCLOSURES = all_enclosures

    def __init__(self, zoo_name: str):
        """ Creates a ZooSystem object and initialises internal storage for all zoo data structures.
            Parameters:
                - zoo_name: string
                    The name of the zoo that this system represents."""

        self.__zoo_name = zoo_name
        self.__enclosures = []
        self.__animals = []
        self.__staff = []
        self.__tasks_by_date = {}
        self.__reported_issues = defaultdict(list)
        self.__health_records = defaultdict(list)

    @property
    def health_records(self):
        """ Returns the dictionary storing health records for all animals. """
        return self.__health_records

    @property
    def animals(self):
        """ Returns the list of all animal objects stored in the zoo system. """
        return self.__animals

    @property
    def staff(self):
        """ Returns the list of all staff member objects in the zoo system. """
        return self.__staff

    @property
    def enclosures(self):
        """ Returns the list of all enclosure objects stored in the zoo system. """
        return self.__enclosures

    @property
    def tasks_by_date(self):
        """ Returns the dictionary storing all scheduled task objects grouped by date. """
        return self.__tasks_by_date


    def create_enclosure_code(self, type: str, size: int) -> str:
        """ A helper method used to generate a unique enclosure identification code for enclosures.
            Enclosure objects are identified internally by their enclosure id.
            Parameters:
                - type: string
                    The environmental type of enclosure object.
                - size: integer
                    The size of enclosure object in square meters.
            Returns:
                - enclosure_id: string
                    The unique enclosure id for enclosure object. """

        words = type.split()

        code = words[0][:3].title()

        if len(words) > 1:
            code += words[1][:3].title()

        if len(words) > 2:
            code += words[2][:3].title()

        id_code = f"{size}{code}"

        count = 1
        for enclosure in self.__enclosures:
            if enclosure.type.lower() == type.lower():
                count += 1

        return f"{id_code}{count}"


    def create_staff_id(self, staff_name: str, staff_birthday: str):
        """ A helper method used to generate a unique staff identification code for staff members.
            Staff objects are identified internally by their staff id.
            Parameters:
                - staff_name: string
                    The full name of staff member object.
                - staff_birthday: string
                    The birthday date of staff member object in string format.
            Returns:
                - staff_id: string
                    The unique staff id for staff member object. """
        words = staff_name.split()
        if len(words) <= 1:
            raise ValueError ("Full name of staff member is required")

        first  = words[0]
        if len(words) == 2:
            last = words[1]
            code = first[:3]+last[:3]
        else:
            middle = words[1]
            last = words[-1]
            code = first[:3]+middle[:1]+last[:2]

        staff_id = f"{code}{staff_birthday[-2:]}"

        return staff_id


    def get_animal(self, animal_name: str):
        """ A helper method used to retrieve an Animal object from system storage based on animal.name string.
            Parameters:
                - animal_name: string
                    The name of animal object to be retrieved.
            Returns:
                - animal: Animal
                    The Animal object matching the provided animal name. """
        if not isinstance(animal_name, str):
            raise TypeError("Animal name must be a string")

        for i in self.__animals:
            if i.name == animal_name:
                return i

        raise NoSuchAnimalError('No such animal exists at the Zoo')


    def get_enclosure(self, enclosure_id: str):
        """ A helper method used to retrieve an Enclosure object from system storage based on enclosure.id string.
            Parameters:
                - enclosure_id: string
                    The unique enclosure id of enclosure object to be retrieved.
            Returns:
                - enclosure: Enclosure
                    The Enclosure object matching the provided enclosure id. """
        if not isinstance(enclosure_id, str):
            raise TypeError("Enclosure ID must be a string")

        lookup_id = str(enclosure_id).strip()
        for i in self.__enclosures:
            if i.id == lookup_id:
                return i
        raise NoSuchEnclosureError('No such enclosure exists at the Zoo')


    def get_staff(self, staff_id: str):
        """ A helper method used to retrieve a Staff object from system storage based on staff.id string.
            Parameters:
                - staff_id: string
                    The unique staff id of staff member object to be retrieved.
            Returns:
                - staff: Staff
                    The Staff object matching the provided staff id. """
        if not isinstance(staff_id, str):
            raise TypeError("Staff ID must be a string")

        lookup_id = str(staff_id).strip()
        for staff in self.__staff:
            if staff.id == lookup_id:
                return staff

        raise NoSuchStaffError('No such staff member exists at the Zoo')

    def add_enclosure(self, size: int, type: str):
        """ A helper method used to create and store a new Enclosure object in system storage.
            Parameters:
                - size: integer
                    The size of enclosure object in square meters.
                - type: string
                    The environmental type of enclosure object."""

        if not isinstance(size, int) or not isinstance(type, str):
            raise TypeError("Enclosure size must be a integer and type a string")
        norm_type = type.strip().title()

        if norm_type not in self.ENCLOSURES:
            raise NotInDatabaseError('No such enclosure exists at the Zoo')


        id_code = self.create_enclosure_code(type, size)
        new_enclosure = Enclosure(size, type, id_code)
        self.__enclosures.append(new_enclosure)


    def add_animal(self, type: str, name: str, species: str, age: int):
        """ A helper method used to create and store a new Animal object of appropriate subclass.
            Parameters:
                - type: string
                    The animal type indicating subclass (e.g. 'Mammal', 'Bird', 'Reptile').
                - name: string
                    The name of animal object.
                - species: string
                    The species of animal object.
                - age: integer
                    The age of animal object in years """

        if not isinstance(type, str) or not isinstance(species, str) or not isinstance(name, str):
            raise TypeError("Species, name and type must be a string")

        norm_type = " ".join(type.strip().split()).title()
        norm_species = " ".join(species.strip().split()).title()

        if norm_type not in self.ANIMAL_TYPES:
            raise NotInDatabaseError(f'Animal {type} not in database. Try Mammal, Reptile or Bird')
        if norm_species not in self.ANIMALS:
            raise NotInDatabaseError(f'Animal {species} not in database. Add {species} to database manually or try again')
        if not isinstance(age, int):
            raise TypeError(f'Age must be a number')
        if age < 0:
            raise ValueError(f'Age must be a positive number or 0 if newborn')
        if not isinstance(species, str) or not isinstance(name, str) or not isinstance(type, str):
            raise TypeError("Species, name and type must be a string")

        found = False
        for group in self.ANIMAL_DATA:
            if norm_species in group:
                info = group[norm_species]
                found = True
                break

        if not found:
            raise NotInDatabaseError(f'Animal {species} not in database. Add {species} to database manually or try again')
        if age > info["max_age"]:
            raise ValueError(f'{age} years of age for this species exceeds reasonable age of maximum {info["max_age"]} for this species.')

        for animal in self.__animals:
            if animal.name == name:
                raise DuplicateError(f"An Animal with this name already exists at the zoo, please choose another name.")

        if norm_type == 'Mammal':
            enclosure = info["enclosure"]
            diet = info["diet"]
            sound = info["sound"]
            new_animal = Mammal(name, species, age, enclosure, diet, sound)

        if norm_type == 'Bird':
            enclosure = info["enclosure"]
            diet = info["diet"]
            sound = info["sound"]
            new_animal = Bird(name, species, age, enclosure, diet, sound)

        if norm_type == 'Reptile':
            enclosure = info["enclosure"]
            diet = info["diet"]
            sound = info["sound"]
            new_animal = Reptile(name, species, age, enclosure, diet, sound)


        self.__animals.append(new_animal)


    def add_staff(self, name: str, age: int, gender: str, birthday: str, role=None):
        """ Used to create and store a new Staff object or Staff subclass object.
            Parameters:
                - name: string
                    The full name of staff member object.
                - age: integer
                    The age of staff member object in years.
                - gender: string
                    The gender of staff member object.
                - birthday: string
                    The birthday date of staff member object in string format.
                - role: string (optional)
                    The staff role indicating subclass ('keeper', 'veterinarian')."""

        if not isinstance(name, str) or not isinstance(gender, str) or not isinstance(birthday, str):
            raise TypeError("Name, gender and birthday must be a string")
        if not isinstance (age, int):
            raise TypeError("Age must be a number")

        name = name.strip()
        if " " not in name:
            raise ValueError(f"Staff name and surname (full name), separated by a space are required")

        date = self.validate_date(birthday)
        staff_id = self.create_staff_id(name, birthday)


        for staff in self.__staff:

            if staff.id == staff_id:
                if staff.name == name and staff.birthday == birthday:
                    raise DuplicateError(f"Staff {name} with birthday {birthday} already in the system")
                else:
                    staff_id = "2" + staff.id

        if role != None:

            if role.lower().strip() not in ['keeper', 'veterinarian']:
                raise InvalidStaffRoleError('Invalid staff role (must be keeper or veterinarian)')

            if role.lower().strip() == 'keeper':
                new_staff = Keeper(name, age, gender, date, staff_id)
            if role.lower().strip() == 'veterinarian':
                new_staff = Veterinarian(name, age, gender, date, staff_id)

        else:
            new_staff = Staff(name, age, gender, date, staff_id)

        self.__staff.append(new_staff)

    def remove_staff(self, staff_id: str):
        """ Used to remove a Staff object from system storage based on staff id string.
            Parameters:
                - staff_id: string
                    The unique staff id of staff member object to be removed."""

        if not isinstance(staff_id, str):
            raise TypeError("Staff Id must be a string")

        staff = self.get_staff(staff_id)

        if staff.role == "Veterinarian" and staff.working_animal is not None:
            raise CannotRemoveStaffError("Can not remove staff while staff is working on an animal")

        if staff.role == "Keeper" and staff.working_enclosure is not None:
            raise CannotRemoveStaffError("Can not remove staff while staff is working in enclosure")

        for enclosure in self.__enclosures:
            if staff_id in enclosure.keepers:
                enclosure.keepers.remove(staff_id)

        for date, buckets in self.__tasks_by_date.items():
            for status, groups in buckets.items():

                if staff_id in groups:

                    unassigned = groups.setdefault("UNASSIGNED", [])

                    for task in groups[staff_id]:
                        task.assigned = False
                        task.assigned_to = None
                        unassigned.append(task)

                    del groups[staff_id]

                    break
        self.__staff.remove(staff)


    def remove_enclosure(self, enclosure_id: str):
        """Used to remove an Enclosure object from system storage based on enclosure id string.
               Parameters:
                   - enclosure_id: string
                       The unique enclosure id of enclosure object to be removed."""

        if not isinstance(enclosure_id, str):
            raise TypeError("Enclosure ID must be a string")

        enclosure = self.get_enclosure(enclosure_id)
        animals = enclosure.contains

        if animals:
            raise CannotRemoveEnclosureError('Can only remove Enclosures without animals currently stored')

        keepers_id = enclosure.keepers
        for id in keepers_id:
            keeper = self.get_staff(id)
            if enclosure in keeper.assigned_enclosures:
                keeper.assigned_enclosures.remove(enclosure)
            if keeper.working_enclosure == enclosure:
                keeper.working_enclosure = None

        for animal in self.__animals:
            if animal.in_enclosure == enclosure_id:
                animal.in_enclosure = None

        for date, bucket in self.__tasks_by_date.items():
            for state in ("uncompleted", "completed"):
                groups = bucket[state]
                for staff_id, tasks in list(groups.items()):
                    groups[staff_id] = [t for t in tasks if not getattr(t, "enclosure_id", None) == enclosure_id]

        self.__enclosures.remove(enclosure)


    def remove_animal(self, animal_name: str):
        """ Used to remove an Animal object from system storage based on animal name string.
            Parameters:
                - animal_name: string
                    The name of animal object to be removed."""

        animal = self.get_animal(animal_name)

        if not isinstance(animal_name, str):
            raise TypeError("Animal name must be a string")

        if animal.treatment == True:
            raise CannotRemoveAnimalError('Can not remove animals in treatment')

        for date_key, buckets in self.__tasks_by_date.items():
            for status in ("uncompleted", "completed"):
                groups = buckets[status]
                for owner_id, tasks in list(groups.items()):
                    new_tasks = []
                    for task in tasks:
                        if isinstance(task, TreatmentTask) and task.animal_id == animal_name:
                            continue

                        if isinstance(task, FeedingTask) and isinstance(task.animals, list):
                            if animal_name in task.animals:
                                task.animals = [n for n in task.animals if n != animal_name]
                                if not task.animals:
                                    continue
                        new_tasks.append(task)

                    if new_tasks:
                        groups[owner_id] = new_tasks
                    else:
                        del groups[owner_id]

        if animal.in_enclosure:
            enclosure = self.get_enclosure(animal.in_enclosure)
            if animal in enclosure.contains:
                enclosure.contains.remove(animal)


        for staff in self.__staff:
            if isinstance(staff, Veterinarian):

                if staff.working_animal is animal:
                    raise CannotRemoveAnimalError("Can not remove animals in treatment")

                if animal in staff.assigned_animals:
                    staff.assigned_animals.remove(animal)


        self.__health_records.pop(animal_name, None)

        self.__animals.remove(animal)

    def assign_animal_to_enclosure(self, animal_name: str, enclosure_id: str):
        """ Assigns an animal object to an enclosure object based on provided identifiers.
            Enclosure objects store real animal objects.
            Parameters:
                - animal_name: string
                    The name of animal object to be assigned.
                - enclosure_id: string
                    The enclosure id of enclosure object receiving the animal."""

        if not isinstance(animal_name, str) or not isinstance(enclosure_id, str):
            raise TypeError("Animal name and enclosure id must be of type string")

        animal = self.get_animal(animal_name)
        enclosure = self.get_enclosure(enclosure_id)

        if animal.treatment == True:
            raise AnimalUnderTreatmentError('Can not move animals in treatment')

        if animal.in_enclosure == enclosure_id:
            raise ValueError("Animal is already in this enclosure")

        if animal.in_enclosure is not None:
            old = self.get_enclosure(animal.in_enclosure)
            if enclosure.can_store(animal):
                if animal in old.contains:
                    old.contains.remove(animal)
                    enclosure.store(animal)
                    animal.in_enclosure = enclosure.id
                    return

        if enclosure.can_store(animal):
            enclosure.store(animal)
            animal.in_enclosure = enclosure.id

    def get_enclosure_animals(self, enclosure_id: str):
        """ Retrieves all animal objects currently stored within a specific enclosure.
            Parameters:
                - enclosure_id: string
                    The enclosure id of enclosure object whose animals are requested.
            Returns:
                - animals: list
                    A list of Animal objects stored in the specified enclosure. """

        enclosure = self.get_enclosure(enclosure_id)
        animals = enclosure.contains
        return animals


    def assign_animal_to_vet(self, animal_name: str, staff_id: str):
        """ Assigns an animal object to a veterinarian staff member for monitoring or treatment.
            Veterinarians are assigned real animal objects.
              Parameters:
                  - animal_name: string
                      The name of animal object to be assigned.
                  - staff_id: string
                      The staff id of veterinarian receiving the assignment."""
        if not isinstance(animal_name, str) or not isinstance(staff_id, str):
            raise TypeError("Animal name and staff id must be of type string")

        animal = self.get_animal(animal_name)
        vet = self.get_staff(staff_id)

        if vet.role != "Veterinarian":
            raise InvalidStaffRoleError('Can only assign Veterinarians to animals')

        for staff_member in self.__staff:
            if isinstance(staff_member, Veterinarian):
                if animal in staff_member.assigned_animals:
                    if staff_member.id == vet.id:

                        raise DuplicateError(f"{animal.name} already assigned to {vet.id}")
                    else:

                        raise DuplicateError(f"{animal.name} is already assigned to veterinarian {staff_member.id}")

        vet.accept_assignment(animal)


    def assign_enclosure_to_keeper(self, enclosure_id: str, staff_id: str):
        """ Assigns an enclosure object to a keeper staff member for management and care duties.
            Keepers are assigned real enclosure objects.
            Parameters:
                - enclosure_id: string
                    The enclosure id of enclosure object to be assigned.
                - staff_id: string
                    The staff id of keeper receiving the assignment."""

        if not isinstance(enclosure_id, str) or not isinstance(staff_id, str):
            raise TypeError("Enclosure id and staff id must be of type string")

        enclosure = self.get_enclosure(enclosure_id)
        keeper = self.get_staff(staff_id)

        if keeper.role != "Keeper":
            raise InvalidStaffRoleError('Can only assign Keepers to Enclosures')

        keeper.accept_assignment(enclosure)
        if keeper.id not in enclosure.keepers:
            enclosure.keepers.append(keeper.id)

    def validate_date(self, date: str):
        """ A helper method that validates a date string and ensures it follows the required DD/MM/YYYY format.
            Parameters:
                - date: string
                    The date string provided for validation.
            Returns:
                - date: string
                    A validated date string formatted as DD/MM/YYYY. """
        if not isinstance(date, str):
            raise TypeError("Date must be a string")

        date_lower = date.strip().lower()
        today = datetime.today().strftime("%d/%m/%Y")

        if date_lower in ("today", "now"):
            return today

        try:
            dt = datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            raise InvalidDateError(f"Invalid date: '{date}'. Please use DD/MM/YYYY, e.g. 05/12/2025.")

        return dt.strftime("%d/%m/%Y")

    def get_date_key(self, date: str = None):
        """ A helper method that produces a standardised date key for scheduling purposes.
            Parameters:
                - date: string (optional)
                    The date string to be converted into a date key.
            Returns:
                - date_key: string
                    A validated date key or 'UNSCHEDULED' if no date is provided. """

        if date is None:
            return "UNSCHEDULED"

        return self.validate_date(date)

    def get_or_create_date_slot(self, date: str = None):
        """ Retrieves or creates a task storage slot associated with a specific date.
                    Parameters:
                        - date: string (optional)
                            The date string used to locate or create a task slot.
                    Returns:
                        - slot: dict
                            A dictionary containing task buckets for 'uncompleted' and 'completed' tasks. """

        date_key = self.get_date_key(date)

        if date_key not in self.__tasks_by_date:
            self.__tasks_by_date[date_key] = {
                "uncompleted": {},
                "completed": {}
            }
        return self.__tasks_by_date[date_key]

    def add_task(self, task, date: str = None, staff_id: str = None):
        """ Adds a task object to the scheduling system under the specified date and staff assignment.
            Parameters:
                - task: Task
                    The task object to be added into the schedule.
                - date: string (optional)
                    The scheduled date for the task.
                - staff_id: string (optional)
                    The staff id for task assignment, or 'UNASSIGNED' if none is provided."""

        slot = self.get_or_create_date_slot(date)
        bucket = slot["uncompleted"]
        key = staff_id if staff_id is not None else "UNASSIGNED"
        if key not in bucket:
            bucket[key] = []
        bucket[key].append(task)
        task.assigned_to = staff_id
        task.assigned = staff_id is not None

    def schedule_feeding_auto(self, date: str = None):
        """ Automatically creates feeding tasks for enclosures containing hungry animals.
             Parameters:
                 - date: string (optional)
                     The date for which feeding tasks are to be scheduled."""

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
            task = FeedingTask(enclosure_id, animals, date_key)
            if task.id not in existing_ids:
                self.add_task(task, date=date_key)


    def schedule_cleaning_auto(self, date: str = None):
        """ Automatically creates cleaning tasks for enclosures requiring cleaning attention.
            Parameters:
                - date: string (optional)
                    The date for which cleaning tasks are to be scheduled."""
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
            task = CleaningTask(enclosure.id, date_key)
            if task.id not in existing_ids:
                self.add_task(task, date=date)

    def schedule_treatment_auto(self, date: str = None):
        """ Automatically creates treatment tasks for animals requiring medical attention.
            Parameters:
                - date: string (optional)
                    The date for which cleaning tasks are to be scheduled."""
        need_treatment = [animal for animal in self.__animals if animal.ailment]

        date_key = self.get_date_key(date)
        existing_ids = set()
        if date_key in self.__tasks_by_date:
            for bucket in self.__tasks_by_date[date_key]["uncompleted"].values():
                for t in bucket:
                    existing_ids.add(t.id)
            for bucket in self.__tasks_by_date[date_key]["completed"].values():
                for t in bucket:
                    existing_ids.add(t.id)

        for animal in need_treatment:
            task = TreatmentTask(animal.name, date_key)
            if task.id not in existing_ids:
                self.add_task(task, date=date)

    def assign_task_to_staff(self, staff_id: str, task_id: str):
        staff = self.get_staff(staff_id)

        date_key, status, owner_id, task = self.find_task_in_schedule(task_id)

        if status != "uncompleted":
            raise InvalidTaskAssignmentError ("Cannot assign a completed task")
        if task.type in ("Feeding", "Cleaning") and staff.role != "Keeper":
            raise InvalidStaffRoleError("Can only assign Keepers to feeding and cleaning tasks")
        if task.type == "Treatment" and staff.role != "Veterinarian":
            raise InvalidStaffRoleError("Can only assign Veterinarians to Treatments")

        if task.type in ("Feeding", "Cleaning"):
            enclosure = self.get_enclosure(task.enclosure_id)
            if enclosure not in staff.assigned_enclosures:
                raise InvalidTaskAssignmentError (f"Keeper {staff.id} is not assigned to enclosure {enclosure.id}")
        if task.type == "Treatment":
            animal = self.get_animal(task.animal_id)
            if animal not in staff.assigned_animals:
                raise InvalidTaskAssignmentError (f"Veterinarian {staff.id} is not assigned to animal {animal.name}")

        slot = self.__tasks_by_date[date_key]
        uncompleted = slot["uncompleted"]

        uncompleted[owner_id].remove(task)
        if not uncompleted[owner_id]:
            del uncompleted[owner_id]

        uncompleted.setdefault(staff_id, []).append(task)

        task.assigned = True
        task.assigned_to = staff_id

        if task not in staff.tasks:
            staff.tasks.append(task)


    def iter_tasks(self, date: str = None, status: str = None, assigned: bool = None, staff_id: str = None):
        """ Iterates through all task objects in the scheduling system with optional filtering.
            Parameters:
                - date: string (optional)
                    The date key for filtering tasks.
                - status: string (optional)
                    The task status for filtering ('uncompleted' or 'completed').
                - assigned: bool (optional)
                    Whether to filter tasks by assignment state.
                - staff_id: string (optional)
                    The staff id to filter tasks by assigned staff member.
            Returns:
                - generator: yields tuples containing date key, status, assignment group, and task object. """

        date_keys = [self.get_date_key(date)] if date else self.__tasks_by_date.keys()

        for date in date_keys:
            if date not in self.__tasks_by_date:
                continue
            buckets = self.__tasks_by_date[date]

            status_keys = [status] if status else buckets.keys()

            for st in status_keys:
                if st not in buckets:
                    continue

                for group, tasks in buckets[st].items():
                    for task in tasks:
                        if assigned is not None:
                            is_assigned = task.assigned_to is not None
                            if is_assigned != assigned:
                                continue
                        if staff_id is not None:
                            if task.assigned_to != staff_id:
                                continue
                        yield date, st, group, task


    def task_exists(self, check_task, date: str = None):
        """ A helper method that checks whether a task object already exists within the scheduling system.
            Parameters:
                - check_task: Task
                    The task object being checked for existence.
                - date: string (optional)
                    The date key used to limit the search.
            Returns:
                - exists: bool
                    True if the task exists, otherwise False. """
        for _, _, _, task in self.iter_tasks(date=date, status=None):
            if task.id == check_task.id:
                return True
            return False

    def get_task_by_id(self, task_id: str):
        """ Retrieves a task object from the scheduling system based on its unique task id.
            Parameters:
                - task_id: string
                    The unique task id of task object to be retrieved.
            Returns:
                - task: Task
                    The task object matching the provided task id. """

        for _, _, _, task in self.iter_tasks():
            if task.id == task_id:
                return task
        raise NoSuchTaskError(f"No task found with ID: {task_id}")

    def find_task_in_schedule(self, task_id: str):
        """Locate a task by id in the schedule.

        Returns:
            (date_key, state, owner_id, task)
        Raises:
            NoSuchTaskError if the task cannot be found.
        """
        for date_key, slot in self.__tasks_by_date.items():
            for state in ("uncompleted", "completed"):
                if state not in slot:
                    continue
                for owner_id, tasks in slot[state].items():
                    for task in tasks:
                        if task.id == task_id:
                            return date_key, state, owner_id, task

        raise NoSuchTaskError(f"No task found with ID: {task_id}")


    def create_task_manual(self, task_type: str, enclosure_id: str = None, animal_names=None, date: str = None):
            """
            Creates and adds a new task object manually to the schedule.
            Supports Feeding, Cleaning, and Treatment tasks.
            - Feeding requires enclosure_id + list of animal names
            - Cleaning requires enclosure_id only
            - Treatment requires a single animal name (string)
            """

            normalised_type = task_type.strip().capitalize()
            date_key = self.get_date_key(date)


            if normalised_type == "Feeding":
                if enclosure_id is None or not animal_names:
                    raise IncompleteTaskError("Feeding requires enclosure ID and a list of animal names.")
                if not isinstance(animal_names, list):
                    raise TypeError("animal_names must be a list for Feeding tasks.")
                new_task = FeedingTask(enclosure_id, animal_names, date_key)

            elif normalised_type == "Cleaning":
                if enclosure_id is None:
                    raise IncompleteTaskError("Cleaning requires enclosure ID.")
                new_task = CleaningTask(enclosure_id, date_key)

            elif normalised_type == "Treatment":
                if not isinstance(animal_names, str):
                    raise TypeError("Treatment requires a single animal name (string).")
                new_task = TreatmentTask(animal_names, date_key)

            else:
                raise IncompleteTaskError(f"Invalid task type: {task_type}")

            if self.task_exists(new_task, date):
                raise IncompleteTaskError("Task already exists.")

            self.add_task(new_task, date=date)
            return new_task


    def complete_task(self, task_id: str):
        date_key, state, owner_id, task = self.find_task_in_schedule(task_id)

        if state != "uncompleted":
            raise InvalidTaskAssignmentError("Task is already completed.")
        if owner_id == "UNASSIGNED":
            raise InvalidTaskAssignmentError("Cannot complete an unassigned task.")

        self.get_staff(owner_id)


        if task.type == "Cleaning":
            enclosure = self.get_enclosure(task.enclosure_id)
            if enclosure.cleanliness < 4:
                raise IncompleteTaskError("Enclosure is not clean enough to complete this task.")

        if task.type == "Feeding":
            enclosure = self.get_enclosure(task.enclosure_id)

            if getattr(task, "animals", None) == ["All Animals"]:
                target_animals = enclosure.contains
            else:
                target_animals = [self.get_animal(name) for name in getattr(task, "animals", [])]

            for animal in target_animals:
                if animal.hungry:
                    raise IncompleteTaskError(f"{animal.name} is still hungry.")

        if task.type == "Treatment":
            animal = self.get_animal(task.animal_id)
            if animal.ailment:
                raise IncompleteTaskError(f"{animal.name}'s treatment is not finished.")

        slot = self.__tasks_by_date[date_key]
        uncompleted = slot["uncompleted"]
        completed = slot["completed"]

        uncompleted[owner_id].remove(task)
        if not uncompleted[owner_id]:
            del uncompleted[owner_id]

        completed.setdefault(owner_id, []).append(task)
        task.mark_complete()

    def create_health_entry(self, animal_name: str, date: str, issue: str, details: str, severity: int, treatment: str):
        if not isinstance(animal_name, str):
            raise TypeError("Animal name must be a string")

        for field_name, field in [("issue", issue), ("details", details), ("treatment", treatment)]:
            if not isinstance(field, str):
                raise TypeError(f"{field_name.capitalize()} must be a string")
            if not field.strip():
                raise ValueError(f"{field_name.capitalize()} cannot be empty")
        if not isinstance(severity, int):
            raise TypeError("Severity must be an integer")
        if not (0 <= severity <= 3):
            raise ValueError("Severity must be between 0 and 3")

        animal = self.get_animal(animal_name)
        date_key = self.validate_date(date)


        log_entry = Entry(date_key, issue, details, severity, treatment)
        self.__health_records[animal_name].append(log_entry)
        return log_entry


    def get_animal_health_record(self, animal_name: str):
        if not isinstance(animal_name, str):
            raise TypeError("Animal name must be a string")

        if animal_name not in self.__health_records:
            raise NoSuchAnimalError(f"No health records exist for {animal_name}")

        return self.__health_records[animal_name]





