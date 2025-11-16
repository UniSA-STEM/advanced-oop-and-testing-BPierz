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
ui.add_enclosure(75, "Riverbank")
ui.add_enclosure(80, "Rainforest")
ui.add_enclosure(100, "HumptyDumpty")

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
ui.assign_animal_to_enclosure("MotoMoto", "75Riv1")
ui.assign_animal_to_enclosure("Mufasa", "100Sav1")

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