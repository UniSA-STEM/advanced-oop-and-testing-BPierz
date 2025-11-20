
'''
File: interface.py
Description: This module represents a user interface and holds the class Interface. The Interface class handles exceptions
            raised by the classes below and outputs user-friendly information and messages on operations performed by
            the zoo system internally. Users use Interface methods to trigger system actions and receive reports and outputs
            from the zoo system in a readable format.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.'''
from domain.staff.staff import Staff
from exceptions import *
from system.zoo_system import ZooSystem


class Interface:
    def __init__(self, zoo_system: ZooSystem):
        """ Creates an Interface object used to interact with the zoo system.
            Parameters:
                - zoo_system: ZooSystem
                    The ZooSystem object that this interface communicates with."""
        self.__system = zoo_system

    def add_animal(self, type, name, species, age):
        """ Adds a new animal object to the zoo system and displays confirmation to the user.
            Parameters:
                - type: string
                    The animal type indicating subclass (e.g. 'Mammal', 'Bird', 'Reptile').
                - name: string
                    The name of animal object.
                - species: string
                    The species of animal object.
                - age: integer
                    The age of animal object in years."""
        try:
            self.__system.add_animal(type, name, species, age)
            print (f"Animal added!\n{self.__system.animals[-1]}")
        except ValueError as e:
            print (f"Animal cannot be added: {e}\n")

    def remove_animal(self, animal_name: str):
        """ Removes an animal object from the zoo system and displays confirmation to the user.
            Parameters:
                - animal_name: string
                    The name of animal object to be removed."""
        try:
            animal = self.__system.get_animal(animal_name)
            self.__system.remove_animal(animal_name)
            print (f"Animal removed:\n{animal}\n")
        except NoSuchAnimalError as e:
            print (f"Cannot remove animal: {e}\n")

    def add_staff(self, name:str, age: int, gender:str, birthday:str, role = None):
        """ Adds a new staff member to the zoo system and displays confirmation to the user.
            Parameters:
                - name: string
                    The full name of staff member object.
                - age: integer
                    The age of staff member object in years.
                - gender: string
                    The gender of staff member object.
                - birthday: string
                    The birthday date of staff member object.
                - role: string (optional)
                    The staff role indicating subclass (e.g. 'Keeper', 'Veterinarian')."""
        try:
            self.__system.add_staff(name, age, gender, birthday, role)
            print (f"Staff Member added {self.__system.staff[-1]}")
        except ValueError as e:
            print (f"Staff Member cannot be added: {e}\n")
        except TypeError as e:
            print (f"Staff Member cannot be added: {e}\n")
        except InvalidDateError as e:
            print (f"Staff Member cannot be added: {e}\n")


    def remove_staff(self, staff_id: str):
        """ Removes a staff member from the zoo system and displays confirmation to the user.
            Parameters:
                - staff_id: string
                    The unique staff id of staff member object to be removed. """

        if staff_id is None:
            print("Cannot remove staff: provide staff id.")
            return

        try:
            staff = self.__system.get_staff(staff_id)
            self.__system.remove_staff(staff_id)
            print(f"Staff Member removed: {staff.name} : {staff.id}")
        except NoSuchStaffError as e:
            print(f"Cannot remove staff: {e}\n")


    def add_enclosure(self, size: int, type: str):
        """ Adds a new enclosure object to the zoo system and displays confirmation to the user.
            Parameters:
                - size: integer
                    The size of enclosure object in square meters.
                - type: string
                    The environmental type of enclosure object."""

        try:
            self.__system.add_enclosure(size, type)
            print (f"Enclosure added!\n"
                   f"{self.__system.enclosures[-1]}")
        except ValueError as e:
            print (f"Enclosure cannot be added: {e}\n")
        except TypeError as e:
            print (f"Enclosure cannot be added: {e}\n")


    def remove_enclosure(self, enclosure_id: str):
        """ Removes an enclosure object from the zoo system and displays confirmation to the user.
            Parameters:
                - enclosure_id: string
                    The unique enclosure id of enclosure object to be removed."""
        try:
            enclosure = self.__system.get_enclosure(enclosure_id)
            self.__system.remove_enclosure(enclosure_id)
            print(f"Enclosure removed: {enclosure.id}")

        except NoSuchEnclosureError as e:
            print(f"Cannot remove enclosure: {e}\n")
        except CannotRemoveEnclosureError as e:
            print(f"Cannot remove enclosure: {e}\n")


    def show_all_animals(self):
        """ Displays all animal objects currently stored within the zoo system."""

        animals = self.__system.animals
        animals_str = [str(animal) for animal in animals]
        animals_display = "\n".join(animals_str)
        print (f"All animals: \n"
               f"{animals_display}\n")

    def show_animal(self, animal_name: str):
        """ Displays a single animal object based on the provided animal name.
            Parameters:
                - animal_name: string
                    The name of animal object to be displayed."""

        try:
            animal = self.__system.get_animal(animal_name)
            print(animal)
        except NoSuchAnimalError as e:
            print(f"Cannot show animal: {e}\n")

    def show_animals_in_enclosure(self, enclosure_id: str):
        animals = self.__system.get_enclosure_animals(enclosure_id)
        animals_str = "\n".join(animals)

        print(f"All Animals in {enclosure_id}:{animals_str}")


    def show_all_enclosures(self):
        """ Displays all animal objects currently stored within a specific enclosure.
            Parameters:
                - enclosure_id: string
                    The unique enclosure id of enclosure object."""

        enclosures = self.__system.enclosures
        enclosures_str = [enclosure.__str__() for enclosure in enclosures]
        enclosures_display = "\n".join(enclosures_str)
        print(f"All Enclosures:\n{enclosures_display}")

    def show_enclosure(self, enclosure_id: str):
        """ Displays a single enclosure object based on the provided enclosure id.
            Parameters:
                - enclosure_id: string
                    The unique enclosure id of enclosure object to be displayed."""
        try:
            enclosure = self.__system.get_enclosure(enclosure_id)
            print (enclosure)
        except NoSuchEnclosureError as e:
            print(f"Cannot show enclosure: {e}\n")

    def show_all_staff(self):
        """ Displays all staff objects currently stored within the zoo system, grouped by staff role."""
        staff = self.__system.staff
        keepers = [i.__str__() for i in staff if i.role == "Keeper"]
        vets = [i.__str__()  for i in staff if i.role == "Veterinarian"]
        misc = [i.__str__()  for i in staff if i.role == None]

        vets_str = "\n".join(vets)
        keepers_str = "\n".join(keepers)
        misc_str = "\n".join(misc)

        print(f"----- All Staff -----\n"
              f"Keepers:\n"
              f"{keepers_str}\n\n"
              f"Veterinarians:\n"
              f"{vets_str}\n\n"
              f"Other\n"
              f"{misc_str}\n"
              f"-----------------------\n")

    def show_staff(self, staff_id: str):
        """ Displays a single staff member object based on the provided staff id.
            Parameters:
                - staff_id: string
                    The unique staff id of staff member object to be displayed."""
        try:
            staff = self.__system.get_staff(staff_id)
            print(f"{staff}\n")
        except NoSuchStaffError as e:
            print(f"Cannot show staff: {e}\n")

    def assign_animal_to_enclosure(self, animal_name: str, enclosure_id: str):
        """ Assigns an animal object to an enclosure object and displays confirmation to the user.
            Parameters:
                - animal_name: string
                    The name of animal object to be assigned.
                - enclosure_id: string
                    The enclosure id of enclosure object receiving the animal."""
        try:

            self.__system.assign_animal_to_enclosure(animal_name, enclosure_id)
            enclosure = self.__system.get_enclosure(enclosure_id)
            animal = self.__system.get_animal(animal_name)
            if len(enclosure.contains) > 1:
                report = f"{len(enclosure.contains)} {animal.species}s\n"
            else:
                report = f"{len(enclosure.contains)} {animal.species}\n"

            print(f"Animal {animal.name} the {animal.species} now in Enclosure: {enclosure_id}\n"
                  f"Enclosure now contains: {report}")

        except NoSuchEnclosureError as e:
            print(f"Cannot assign animal to enclosure: {e}\n")
        except NoSuchAnimalError as e:
            print(f"Cannot assign animal to enclosure: {e}\n")
        except IncompatibleEnclosureError as e:
            print(f"Cannot assign animal to enclosure: {e}\n")

    def assign_enclosure_to_keeper(self, enclosure_id: str, keeper_id: str):
        """ Assigns an enclosure object to a keeper staff member and displays confirmation to the user.
            Parameters:
                - enclosure_id: string
                    The enclosure id of enclosure object to be assigned.
                - keeper_id: string
                    The staff id of keeper receiving the assignment."""
        try:
            self.__system.assign_enclosure_to_keeper(enclosure_id, keeper_id)
            keeper = self.__system.get_staff(keeper_id)
            enclosure = self.__system.get_enclosure(enclosure_id)

            print(f"Keeper {keeper.id} now responsible for Enclosure: {enclosure.id}\n")

        except NoSuchEnclosureError as e:
            print(f"Cannot assign keeper to enclosure: {e}\n")
        except NoSuchStaffError as e:
            print(f"Cannot assign keeper to enclosure: {e}\n")
        except InvalidStaffRoleError as e:
            print(f"Cannot assign keeper to enclosure: {e}\n")
        except DuplicateError as e:
            print(f"Cannot assign keeper to enclosure: {e}\n")

    def assign_animal_to_vet(self, animal_name: str, vet_id: str):
        """ Assigns an animal object to a veterinarian staff member and displays confirmation to the user.
            Parameters:
                - animal_name: string
                    The name of animal object to be assigned.
                - vet_id: string
                    The staff id of veterinarian receiving the assignment."""
        try:
            self.__system.assign_animal_to_vet(animal_name, vet_id)
            vet = self.__system.get_staff(vet_id)
            animal = self.__system.get_animal(animal_name)
            print(f"{animal.name} the {animal.species} now Assigned to Veterinarian: {vet.id}\n")

        except NoSuchAnimalError as e:
            print(f"Cannot assign animal to Veterinarian: {e}\n")
        except NoSuchStaffError as e:
            print(f"Cannot assign animal to Veterinarian: {e}\n")
        except InvalidStaffRoleError as e:
            print(f"Cannot assign animal to Veterinarian: {e}\n")
        except DuplicateError as e:
            print(f"Cannot assign animal to Veterinarian: {e}\n")


    def display_schedule(self, date: str = None, status: str = None, assigned:bool = None, staff_id:str = None):
        """ Displays scheduled task objects based on the provided filtering options.
            Parameters:
                - date: string (optional)
                    The date of tasks to be displayed.
                - status: string (optional)
                    The task status to filter by ('uncompleted' or 'completed').
                - assigned: boolean (optional)
                    Whether to filter by assignment state.
                - staff_id: string (optional)
                    The staff id used to filter tasks by assigned staff member."""

        tasks = list(self.__system.iter_tasks(date=date, status=status, assigned=assigned, staff_id=staff_id))
        if not tasks:
            print ("No tasks matching this selection can be found.\n")
            return

        if staff_id and not date and not status and assigned is None:
            print(f"\n=== TASKS FOR STAFF: {staff_id} ===")

        current_date = None
        current_status = None

        for task_date, task_status, group, task in tasks:

            if task_date != current_date:
                current_date = task_date

                if not (staff_id and not date and not status and assigned is None):
                    print(f"\n=== Schedule for: {task_date} ===")
                current_status = None

            if task_status != current_status:
                current_status = task_status
                print(f"\n--- [{task_status.upper()}] ---")

            print(f"\nAssigned to: {group}\n{task}")



    def schedule_cleaning_auto(self, date: str = None):
        """ Creates automatic cleaning tasks for enclosures and displays a report to the user.
            Parameters:
                - date: string (optional)
                    The date for which cleaning tasks are to be created."""
        try:
            self.__system.schedule_cleaning_auto(date)
            print(f"Created automatic cleaning schedule for {date} based on current Enclosure needs\n")
        except InvalidDateError as e:
            print(f"Cannot schedule tasks: {e}\n")

    def schedule_feeding_auto(self, date: str = None):
        """ Creates automatic feeding tasks for animals and displays a report to the user.
            Parameters:
                - date: string (optional)
                    The date for which feeding tasks are to be created."""
        try:
            self.__system.schedule_feeding_auto(date)
            print(f"Created automatic feeding schedule for {date} based on current Animal needs\n")

        except InvalidDateError as e:
            print(f"Cannot schedule tasks: {e}\n")


    def create_task_manually(self, task_type:str, enclosure_id = None, animal_names:list = None, date = None):
        """ Creates a new task object manually and displays a confirmation message to the user.
            Parameters:
                - task_type: string
                    The task type to be created ('Feeding' or 'Cleaning').
                - enclosure_id: string (optional)
                    The enclosure id associated with the task.
                - animal_names: list (optional)
                    The list of animal names for feeding tasks.
                - date: string (optional)
                    The scheduled date for the task."""
        try:
            new_task = self.__system.create_task_manual(task_type, enclosure_id, animal_names, date)
            print (f"Task Created Successfully!\n {new_task}\n")
        except IncompleteTaskError as e:
            print(f"Cannot create task: {e}\n")

    def assign_task (self, staff_id, task_id):
        """ Assigns task to staff
            Parameters:
                - staff_id: string (optional)
                The staff id of the staff member to assign task to.
                - task_id: string (optional)
                The task id of the task that is to be assigned to staff.
        """
        try:
            task = self.__system.get_task_by_id(task_id)
            self.__system.assign_task_to_staff(staff_id, task_id)
            print (f"Assigned task {task_id} to staff member {staff_id}\n")
            print(task)

        except InvalidTaskAssignmentError as e:
            print(f"Cannot assign task: {e}\n")
        except InvalidStaffRoleError as e:
            print(f"Cannot assign task: {e}\n")
        except NoSuchStaffError as e:
            print(f"Cannot assign task: {e}\n")
        except NoSuchTaskError as e:
            print(f"Cannot assign task: {e}\n")

    def complete_task(self, staff_id, task_id):
        """ Allows a task member to interact with the system and mark a task as complete."""

        try:
            self.__system.complete_task(task_id)
            print(f"Task {task_id} completed successfully by {staff_id}.\n")

        except IncompleteTaskError as e:
            print(f"Cannot complete task: {e}\n")
        except NoSuchTaskError as e:
            print(f"Cannot complete task: {e}\n")

    def create_health_entry(self, animal_name: str, date: str, issue: str, details: str, severity: int, treatment: str):

        new_entry = self.__system.create_health_entry(animal_name, date, issue, details, severity, treatment)
        print(f"\nHealth entry for {animal_name} created successfully!\n"
              f"{new_entry}\n")


    def display_health_record(self, animal_name: str = None, date: str = None):

        if animal_name is None:
            records = self.__system.health_records
            print (records)

            print(f"\n------ ZOO HEALTH RECORDS ------\n")
            for key in records:
                print(f"\n---- {key}'s Health Records ----\n")
                for entry in records[key]:
                    print (entry)

            print(f"------ END OF HEALTH RECORDS ------\n")
            return

        animal_record = self.__system.get_animal_health_record(animal_name)

        print(f"\n---- {animal_name}'s Health Records ----\n")
        for entry in animal_record:
            print(f"{entry}\n")

        print(f"---- End of Health Records ----\n")

