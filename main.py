from interface.interface import Interface
from system.zoo_system import ZooSystem

# Creating the ZooSystem and Interface objects
system = ZooSystem("Sue's Zoo")
ui = Interface(system)

# Adding Animals to the Zoo System
ui.add_animal("Mammal", "MotoMoto", "Hippopotamus", 5)
ui.add_animal("Bird", "Blue", "Macaw", 10)
ui.add_animal("Mammal", "Mufasa", "Lion", 13)
ui.add_animal("Mammal", "Melman", "Giraffe", 20)
ui.add_animal("Reptile", "Sneaky", "Snake", 25)
ui.add_animal("Mammal", "Gloria", "Hippopotamus", 14)
ui.add_animal("Bird", "Mikey", "Macaw", 15)
ui.add_animal("Mammal", "Simba", "Lion", 13)
ui.add_animal("Mammal", "Nala", "Lion", 20)
ui.add_animal("Reptile", "Sassy", "Snake", 25)

# Removing Animals
ui.remove_animal("Giraffe")
ui.remove_animal("Melman")

# Adding Staff Members
ui.add_staff("Peter Parker", 24, "Male", "12/01/2001", "Keeper")
ui.add_staff("Peter Griffin", 65, "Male", "05/03/1965", "Veterinarian")
ui.add_staff("Mary Jane", 24, "Female", "10/12/2001", "Keeper")
ui.add_staff("Naruto Uzumaki", 18, "Male", "15/9/2006", "veterinarian")
ui.add_staff("Jonah Jameson", 70, "Male", "17/8/1960")

# Displaying Staff Objects
print(system.staff)
for i in system.staff:
    print(i.id)

# Removing a Staff Member
ui.remove_staff("PetGri65")
print(system.staff)

# Adding Enclosures
ui.add_enclosure(100, "Savannah")
ui.add_enclosure(50, "Forest")
ui.add_enclosure(80, "Mountain")
ui.add_enclosure(90, "Desert")
ui.add_enclosure(75, "Wetlands")
ui.add_enclosure(80, "Rainforest")
ui.add_enclosure(100, "HumptyDumpty")
ui.add_enclosure(20, "tropical aviary")

# Removing Enclosures
ui.remove_enclosure("80Rai1")
ui.remove_enclosure("Riverbank")
ui.remove_enclosure("80Mou1")

# Displaying Enclosures
print(system.enclosures)

# Showing All Items
ui.show_all_animals()
ui.show_all_staff()
ui.show_all_enclosures()

# Assigning Animals to Enclosures
ui.assign_animal_to_enclosure("MotoMoto", "75Wet1")
ui.assign_animal_to_enclosure("Mufasa", "100Sav1")
ui.assign_animal_to_enclosure("Nala", "100Sav1")
ui.assign_animal_to_enclosure("Simba", "100Sav1")
ui.assign_animal_to_enclosure("Gloria", "75Wet1")
ui.assign_animal_to_enclosure("Mikey", "20TroAvi1")
ui.assign_animal_to_enclosure("Blue", "20TroAvi1")



# Checking Enclosure Contents
print(system.enclosures[0].contains)
ui.show_all_enclosures()

# Assigning Enclosures to Keepers
ui.assign_enclosure_to_keeper("100Sav1", "PetPar01")
ui.show_enclosure("100Sav1")

# Showing Single Animal / Staff Records
ui.show_animal("Mufasa")
ui.show_staff("NarUzu06")

# Assigning Animal to Veterinarian
ui.assign_animal_to_vet("Mufasa", "NarUzu06")
ui.show_staff("NarUzu06")

# Scheduling Tasks Automatically
for enclosure in system.enclosures:
    enclosure.cleanliness = 1  # Forcing low cleanliness for testing

ui.schedule_cleaning_auto("13/06/2025")
ui.schedule_feeding_auto("15/06/2025")

# Creating Manual Tasks
ui.add_enclosure(50, "Savannah")
ui.create_task_manually("Cleaning", "50Sav2")



# Check internal schedule populated with appropriate tasks objects
print(system.tasks_by_date)

# Display schedule to inspect printing of whole schedule
ui.display_schedule()
ui.display_schedule("15/06/2025")
ui.display_schedule("13/06/2025")


# Demonstrate system workflow of assigning animals, enclosures and completing tasks

# Cannot assign task where enclosure not assigned first
ui.assign_task("PetPar01", "Cln-50Sav2-UNSCH")

# Assigning enclosure and task
PetPar = system.get_staff("PetPar01")
ui.assign_enclosure_to_keeper("50Sav2", "PetPar01")
ui.assign_task("PetPar01", "Cln-50Sav2-UNSCH")

# Display Schedule for PetPar01
ui.display_schedule(staff_id="PetPar01")
# Verify enclosure assignment
ui.show_enclosure("50Sav2")

# PetPar01 is working on enclosure currently, performs cleaning on enclosure.
PetPar.set_working_enclosure("50Sav2")
PetPar.clean_enclosure()
# Can complete task when enclosure is clean.
ui.complete_task("PetPar01", "Cln-50Sav2-UNSCH")
# Completed task is now stored under complete in data
ui.display_schedule(status="completed")

# See treatment tasks
for animals in system.animals[::2]:
    animals.ailment = True
# Create task manually, not using auto creation method.
ui.create_task_manually("Treatment", animal_names = "MotoMoto" )
# Use automatic schedulling
system.schedule_treatment_auto("today")

# Display schedule for today
ui.display_schedule(date="today")
# Assign tasks to appropriate staff members, does not work if animal not assigned first.
ui.assign_task("PetPar01", "Tr-Mikey-20/11")
ui.assign_task("NarUzu06", "Tr-Mikey-19/11")
# Animal assigned, task assigned
ui.assign_animal_to_vet("Mikey", "NarUzu06")
ui.assign_task("NarUzu06", "Tr-Mikey-20/11")

# Task objects completes whole treatment and healing procedure.
NarUzu = system.get_staff("NarUzu06")
NarUzu.treat_animal("Mikey")
ui.complete_task("NarUzu06", "Tr-Mikey-20/11")
NarUzu.heal_animal()
# Call ui to mark as complete
ui.complete_task("NarUzu06", "Tr-Mikey-20/11")




# Veterinarians and Keepers are able to perform health checks on animals and across animals in enclosures to which they
# are assigned. These print to output as these model physical actions taken by real workers.
# Without arguments, staff members check across animals assigned or animals stored in assigned enclosures.

NarUzu.health_check("Mufasa")
NarUzu.health_check()
PetPar.health_check()


# Through ui, health entries can be created and stored in the system. Health entries are independent of actions taken by staff
# and animal states and are used for reporting, not automatic information generation.
ui.create_health_entry("Mufasa",
                       "today",
                       "Mufasa is not eating",
                       "Mufasa has lost his appetite and has not touched his food in a long time",
                       3,
                       "Give appetite medication")

ui.create_health_entry("Blue",
                       "14/11/2025",
                       "Blue is plucking",
                       "Blue is likely bored and has started plucking",
                       2,
                       "Give new toys")

ui.create_health_entry("Blue",
                       "20/11/2025",
                       "Blue has stopped plucking",
                       "Plucking is no longer an issue",
                       0,
                       "Replace toys more often.")

ui.create_health_entry("Mufasa",
                       "21/11/2025",
                       "Mufasa is eating again but now overweight",
                       "Mufasa has been eating everything in sight",
                       3,
                       "Take off appetite medication immediately")

ui.create_health_entry("Nala",
                       "20/11/2025",
                       "Nala is acting strange",
                       "Nala has been circuling her enclosure all day",
                       1,
                       "Provide with entertainment, maybe move enclosure")

# Health records can be displayed across the whole zoo (no parameters) or for a specific animal by calling ui method.
ui.display_health_record()
ui.display_health_record("Mufasa")
ui.display_health_record("Nala")


# Animal behaviours working
animal1 = system.animals[0]
animal2 = system.animals[1]
animal3 = system.animals[2]

# Animals make distinct sounds
animal1.make_sound()
animal2.make_sound()
animal3.make_sound()


