from domain import animals
from exceptions import *
from system.zoo_system import ZooSystem

# This is the class made to output readable messages to console
class Interface:
    def __init__(self, zoo_system: ZooSystem):
        self.__system = zoo_system

    def add_animal(self, type, name, species, age):
        try:
            self.__system.add_animal(type, name, species, age)
            print (f"Animal added!\n{self.__system.animals[-1]}")
        except ValueError as e:
            print (f"Animal cannot be added: {e}\n")

    def remove_animal(self, animal_name: str):
        try:
            animal = self.__system.get_animal(animal_name)
            self.__system.remove_animal(animal_name)
            print (f"Animal removed:\n{animal}\n")
        except NoSuchAnimalError as e:
            print (f"Cannot remove animal: {e}\n")

    def add_staff(self, name:str, age: int, gender:str, birthday:str, role = None):
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
        # Must have at least one identifier
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
        try:
            self.__system.add_enclosure(size, type)
            print (f"Enclosure added!\n"
                   f"{self.__system.enclosures[-1]}")
        except ValueError as e:
            print (f"Enclosure cannot be added: {e}\n")
        except TypeError as e:
            print (f"Enclosure cannot be added: {e}\n")


    def remove_enclosure(self, enclosure_id: str):
        try:
            enclosure = self.__system.get_enclosure(enclosure_id)
            self.__system.remove_enclosure(enclosure_id)
            print(f"Enclosure removed: {enclosure.id}")

        except NoSuchEnclosureError as e:
            print(f"Cannot remove enclosure: {e}\n")
        except CannotRemoveEnclosureError as e:
            print(f"Cannot remove enclosure: {e}\n")



    def show_all_animals(self):
        animals = self.__system.animals
        animals_str = [str(animal) for animal in animals]
        animals_display = "\n".join(animals_str)
        print (f"All animals: \n"
               f"{animals_display}\n")

    def show_animal(self, animal_name: str):
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
        enclosures = self.__system.enclosures
        enclosures_str = [enclosure.__str__() for enclosure in enclosures]
        enclosures_display = "\n".join(enclosures_str)
        print(f"All Enclosures:\n{enclosures_display}")

    def show_enclosure(self, enclosure_id: str):
        try:
            enclosure = self.__system.get_enclosure(enclosure_id)
            print (enclosure)
        except NoSuchEnclosureError as e:
            print(f"Cannot show enclosure: {e}\n")

    def show_all_staff(self):
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
        try:
            staff = self.__system.get_staff(staff_id)
            print(f"{staff}\n")
        except NoSuchStaffError as e:
            print(f"Cannot show staff: {e}\n")

    def assign_animal_to_enclosure(self, animal_name: str, enclosure_id: str):
        try:

            self.__system.assign_animal_to_enclosure(animal_name, enclosure_id)
            enclosure = self.__system.get_enclosure(enclosure_id)
            animal = self.__system.get_animal(animal_name)
            if len(enclosure.contains) > 1:
                report = f"{len(enclosure.contains)} {animal.species}s\n"
            else:
                report = f"{len(enclosure.contains)} {animal.species}\n"

            print(f"Animal now in Enclosure: {enclosure_id}\n"
                  f"Enclosure now contains: {report}")

        except NoSuchEnclosureError as e:
            print(f"Cannot assign animal to enclosure: {e}\n")
        except NoSuchAnimalError as e:
            print(f"Cannot assign animal to enclosure: {e}\n")
        except IncompatibleEnclosureError as e:
            print(f"Cannot assign animal to enclosure: {e}\n")

    def assign_enclosure_to_keeper(self, enclosure_id: str, keeper_id: str):
        try:
            self.__system.assign_enclosure_to_keeper(enclosure_id, keeper_id)
            keeper = self.__system.get_staff(keeper_id)
            enclosure = self.__system.get_enclosure(enclosure_id)

            print(f"Keeper now responsible for Enclosure: {enclosure.id}\n")

        except NoSuchEnclosureError as e:
            print(f"Cannot assign keeper to enclosure: {e}\n")
        except NoSuchStaffError as e:
            print(f"Cannot assign keeper to enclosure: {e}\n")
        except InvalidStaffRoleError as e:
            print(f"Cannot assign keeper to enclosure: {e}\n")
        except DuplicateError as e:
            print(f"Cannot assign keeper to enclosure: {e}\n")

    def assign_animal_to_vet(self, animal_name: str, vet_id: str):
        try:
            self.__system.assign_animal_to_vet(animal_name, vet_id)
            vet = self.__system.get_staff(vet_id)
            animal = self.__system.get_animal(animal_name)
            print(f"Animal now Assigned to Veterinarian: {vet.id}\n")

        except NoSuchAnimalError as e:
            print(f"Cannot assign animal to Veterinarian: {e}\n")
        except NoSuchStaffError as e:
            print(f"Cannot assign animal to Veterinarian: {e}\n")
        except InvalidStaffRoleError as e:
            print(f"Cannot assign animal to Veterinarian: {e}\n")
        except DuplicateError as e:
            print(f"Cannot assign animal to Veterinarian: {e}\n")


    def display_schedule(self, date: str = None, status: str = None, assigned:bool = None, staff_id:str = None):
        tasks = list(self.__system.iter_tasks(date=date, status=status, assigned=assigned, staff_id=staff_id))
        if not tasks:
            print ("No tasks matching this selection can be found.\n")
            return

        current_date = None
        current_status = None

        for date, status, group, task in tasks:
            if date != current_date:
                current_date = date
                print(f"=== Schedule for: {date} ===")
            if status != current_status:
                current_status = status
                print(f"--- [{status.upper()}] ---\n")
            print(f"{group}\n"
                  f"{task}\n")



    def schedule_cleaning_auto(self, date: str = None):
        try:
            self.__system.schedule_cleaning_auto(date)
            print(f"Creating automatic cleaning schedule for {date} based on current Enclosure needs\n"
                  f"Current Schedule for {date}: \n")

            self.display_schedule(date=date, status=None, assigned=False)
        except InvalidDateError as e:
            print(f"Cannot schedule tasks: {e}\n")

    def schedule_feeding_auto(self, date: str = None):
        try:
            self.__system.schedule_feeding_auto(date)
            print(f"Creating automatic feeding schedule for {date} based on current Animal needs\n"
                  f"Current Schedule for {date}: \n")

            self.display_schedule(date=date, status=None, assigned=False)

        except InvalidDateError as e:
            print(f"Cannot schedule tasks: {e}\n")


    def create_task_manually(self, task_type:str, enclosure_id = None, animal_names:list = None, date = None):
        try:
            new_task = self.__system.create_task_manual(task_type, enclosure_id, animal_names, date)
            print (f"Task Created Successfully:\n {new_task}\n")
        except IncompleteTaskError as e:
            print(f"Cannot create task: {e}\n")


    def display_health_record(self, animal_name: str):
        print(f"---- {animal_name} Health Records ----")
        print(f"{self.__system.get_health_record(animal_name)}")
        print(f"---- End of Health Records ----")

