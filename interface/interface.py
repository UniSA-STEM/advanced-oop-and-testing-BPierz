from system.zoo_system import ZooSystem

# This is the class made to output readable messages to console
class Interface:
    def __init__(self, zoo_system: ZooSystem):
        self.__system = zoo_system

    def display_staff(self, staff_role:str = None):
        pass

    def schedule_feeding_auto(self):
        pass

    def add_animal(self):
        pass

    def remove_animal(self):
        pass

    def add_staff(self):
        pass

    def remove_staff(self):
        pass

    def add_enclosure(self):
        pass

    def remove_enclosure(self):
        pass


    def display_feeding_schedule(self):
        tasks = self.__system.uncompleted_tasks["Feeding"]
        tasks_str = "\n".join(tasks)
        print(f"Here is the feeding schedule:\n{tasks_str}")

    def display_cleaning_schedule(self):
        tasks = self.__system.uncompleted_tasks["Cleaning"]
        tasks_str = "\n".join(tasks)
        print(f"Here is the cleaning schedule:\n{tasks_str}")

    def display_health_record(self, animal_name: str):
        print(f"---- {animal_name} Health Records ----")
        print(f"{self.__system.get_health_record(animal_name)}")
        print(f"---- End of Health Records ----")

