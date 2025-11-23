'''
File: test_system_basic.py
Description: This module contains unit tests for ZooSystem objects' basic functionalities.
Author: Borys Pierzchala.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''


import pytest
from domain.enclosures.enclosure import Enclosure
from exceptions import *
from system.zoo_system import ZooSystem
from zoodata.zoo_data import *


@pytest.fixture
def system():
    return ZooSystem("Sue's Zoo")


def test_init(system):
    assert system.enclosures == []
    assert system.animals == []
    assert system.staff == []
    assert system.tasks_by_date == {}
    assert system.health_records == {}

def test_animal_types(system):
    assert ZooSystem.ANIMAL_TYPES == ["Mammal", "Bird", "Reptile"]

def test_animal_data(system):
    assert ZooSystem.ANIMAL_DATA == animal_data
    assert ZooSystem.ANIMALS == animals
    assert ZooSystem.ENCLOSURES == all_enclosures
    assert ZooSystem.FOOD_ITEMS == all_food_items

def test_enclosure_code(system):
    code = system.create_enclosure_code("Savannah", 50)
    code2 = system.create_enclosure_code("Tropical Aviary", 20)
    code3 = system.create_enclosure_code("Very Hot Terrarium", 10)
    code4 = system.create_enclosure_code("tropical aviary", 20)
    assert code == "50Sav1"
    assert code2 == "20TroAvi1"
    assert code3 == "10VerHotTer1"
    assert code4 == "20TroAvi1"

def test_enclosure_code_same_type(system):
    e1 = Enclosure(50, "Savannah", "50Sav1")
    e2 = Enclosure(50, "Savannah", "50Sav2")
    system.enclosures.extend([e1,e2])
    code = system.create_enclosure_code("Savannah", 50)
    assert code == "50Sav3"

def test_create_staff_id(system):
    staff_id = system.create_staff_id("Naruto Uzumaki", "15/06/1998")
    staff_id2 = system.create_staff_id("naruto uzumaki", "15/06/1998")
    staff_id3 = system.create_staff_id("Monkey D Luffy", "05/05/2000")
    assert staff_id == "NarUzu98"
    assert staff_id2 == "naruzu98"
    assert staff_id3 == "MonDLu00"

def test_create_id_raises(system):
    with pytest.raises(ValueError):
        system.create_staff_id("Zendaya", "15/06/1998")


class FakeAnimal:
    def __init__(self, name):
        self.name = name
class FakeStaff:
    def __init__(self, id):
        self.id = id


def test_get_animal(system):
    a = FakeAnimal("Simba")
    system.animals.append(a)
    assert system.get_animal("Simba") == a
    with pytest.raises(NoSuchAnimalError):
        system.get_animal("Zendaya")
    with pytest.raises(TypeError):
        system.get_animal(50)

def test_get_staff(system):
    a = FakeStaff("NarUzu98")
    system.staff.append(a)
    assert system.get_staff("NarUzu98") == a
    with pytest.raises(NoSuchStaffError):
        system.get_staff("Zendaya")
    with pytest.raises(TypeError):
        system.get_staff(50)

def test_get_enclosure(system, enclosure):
    system.enclosures.append(enclosure)
    assert system.get_enclosure("50Sav1") is enclosure
    with pytest.raises(NoSuchEnclosureError):
        system.get_enclosure("Zendaya")
    with pytest.raises(TypeError):
        system.get_enclosure(50)

def test_add_enclosure(system):
    assert system.enclosures == []

    system.add_enclosure(50, "Savannah")

    assert len(system.enclosures) == 1
    enc = system.enclosures[0]
    assert enc.size == 50
    assert enc.type == "Savannah"
    assert enc.id == "50Sav1"

    system.add_enclosure(50, "Savannah")
    assert len(system.enclosures) == 2
    assert system.enclosures[1].size == 50
    assert system.enclosures[1].type == "Savannah"
    assert system.enclosures[1].id == "50Sav2"

    with pytest.raises(TypeError):
        system.add_enclosure(50, 50)
        system.add_enclosure("Savannah", "Savannah")
    with pytest.raises(NotInDatabaseError):
        system.add_enclosure(50, "Random Type Enclosure")


def test_add_animal(system):
    assert system.animals == []
    system.add_animal("Mammal", "Mufasa", "Lion", 5)
    assert len(system.animals) == 1
    system.add_animal("Mammal", "Nala", "Lion", 10)
    assert len(system.animals) == 2

    a = system.animals[0]
    assert a.name == "Mufasa"
    assert a.species == "Lion"
    assert a.age == 5
    assert a.enclosure == "Savannah"
    assert "meat" in  a.diet
    assert "berries" not in a.diet

    system.add_animal("Reptile", "Sneaky", "Chameleon", 5)
    a = system.animals[-1]
    assert a.name == "Sneaky"
    assert a.species == "Chameleon"
    assert a.age == 5
    assert "worms" in a.diet

    system.add_animal("Bird", "Blue", "Macaw", 5)
    a = system.animals[-1]
    assert a.name == "Blue"
    assert a.species == "Macaw"
    assert a.age == 5
    assert "nuts" in a.diet

def test_add_animal_raises(system):
    with pytest.raises(TypeError):
        system.add_animal("Mammal", "Nala", 10, 5)
        system.add_animal("Mammal", "Nala", "Lion", "5")
        system.add_animal("Mammal", 100, "Lion", 5)
        system.add_animal(200, "Nala", "Lion", "5")
    with pytest.raises(ValueError):
        system.add_animal("Mammal", "Nala", "Lion", -10)
    with pytest.raises(NotInDatabaseError):
        system.add_animal("Mammal", "Nala", "RandomSpecies", 5)
        system.add_animal("Amphibian", "Nala", "Lion", 10)

    system.add_animal("Mammal", "Nala", "Lion", 10)
    with pytest.raises(DuplicateError):
        system.add_animal("Mammal", "Nala", "Lion", 10)



def test_add_staff(system):
    assert system.staff == []
    system.add_staff("Peter Parker", 18, "Male", "01/12/2007")
    assert len(system.staff) == 1
    system.add_staff("Mary Jane", 19, "Female", "01/12/2006")
    assert len(system.staff) == 2

    a = system.staff[0]
    assert a.name == "Peter Parker"
    assert a.age == 18
    assert a.gender == "Male"
    assert a.birthday == "01/12/2007"
    assert a.role == None
    assert a.id == "PetPar07"

def test_add_staff_raises(system):
    with pytest.raises(TypeError):
        system.add_staff("Peter Parker", "15", "Male", "01/12/2006")
        system.add_staff("Peter Parker", 18, 123, "01/12/2006")
        system.add_staff("Peter Parker", 18, "Male", "01/12/2006")
        system.add_staff("Peter Parker", 18, "Male", 100)

    with pytest.raises(ValueError):
        system.add_staff("Zendaya", 18, "Female", "01/12/2006")

    with pytest.raises(InvalidStaffRoleError):
        system.add_staff("Peter Parker", 18, "Male", "01/12/2006", role = "rolenotinsystem")

    system.add_staff("Peter Parker", 18, "Male", "01/12/2006")

    with pytest.raises(DuplicateError):
        system.add_staff("Peter Parker", 18, "Male", "01/12/2006")

def test_assign_animal_to_enclosure(system):
    system.add_animal("Mammal", "Nala", "Lion", 10)
    system.add_animal("Mammal", "Mufasa", "Lion", 10)

    a1 = system.animals[0]
    a2 = system.animals[1]

    system.add_enclosure(50, "Savannah")
    system.add_enclosure(50, "Tropical Aviary")
    system.add_enclosure(100, "Savannah")
    system.add_enclosure(20, "Tropical Terrarium")

    e1 = system.enclosures[0]
    e3 = system.enclosures[2]

    system.assign_animal_to_enclosure("Nala", "50Sav1")
    system.assign_animal_to_enclosure("Mufasa", "50Sav1")

    assert a1 in e1.contains
    assert a2 in e1.contains

    system.assign_animal_to_enclosure("Nala", e3.id)

    assert a1 not in e1.contains
    assert a1 in e3.contains
    assert a2 in e1.contains


def test_assign_anim_to_enclosure_raises(system):
    system.add_animal("Mammal", "Nala", "Lion", 10)
    system.add_animal("Bird", "Blue", "Macaw", 20)
    system.add_animal("Bird", "Mikey", "Cockatoo", 20)

    a1 = system.animals[0]
    a3 = system.animals[2]
    a1.treatment = True

    system.add_enclosure(50, "Savannah")
    system.add_enclosure(50, "Tropical Aviary")
    system.add_enclosure(100, "Savannah")
    system.add_enclosure(20, "Tropical Terrarium")

    e1 = system.enclosures[0]
    e2 = system.enclosures[1]

    with pytest.raises(AnimalUnderTreatmentError):
        system.assign_animal_to_enclosure("Nala", "50Sav1")
    assert a1 not in e1.contains

    system.assign_animal_to_enclosure("Blue", "50TroAvi1")

    with pytest.raises(IncompatibleEnclosureError):
        system.assign_animal_to_enclosure("Blue", "50Sav1")

    with pytest.raises(IncompatibleEnclosureError):
        system.assign_animal_to_enclosure("Mikey", "50TroAvi1")

    assert a3 not in e2.contains


def test_assign_animal_to_vet(system):
    system.add_animal("Mammal", "Nala", "Lion", 10)
    system.add_animal("Mammal", "Mufasa", "Lion", 12)

    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Veterinarian")
    system.add_staff("Kakashi Hatake", 35, "Male", "07/09/1985", role="Veterinarian")

    a1 = system.animals[0]
    a2 = system.animals[1]
    vet1 = system.staff[0]
    vet2 = system.staff[1]

    system.assign_animal_to_vet("Nala", vet1.id)
    system.assign_animal_to_vet("Mufasa", vet1.id)

    assert a1 in vet1.assigned_animals
    assert a2 in vet1.assigned_animals

    with pytest.raises(DuplicateError):
        system.assign_animal_to_vet("Nala", vet1.id)

    with pytest.raises(DuplicateError):
        system.assign_animal_to_vet("Nala", vet2.id)

def test_assign_animal_to_vet_raises(system):
    system.add_animal("Mammal", "Nala", "Lion", 10)

    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Veterinarian")
    system.add_staff("Petar Parker", 30, "Male", "01/01/1995", role="Keeper")
    system.add_staff("Sakura Haruno", 22, "Female", "12/03/1999", role="Veterinarian")

    vet1 = system.staff[0]
    keeper = system.staff[1]
    vet2 = system.staff[2]

    with pytest.raises(NoSuchAnimalError):
        system.assign_animal_to_vet("Simba", vet1.id)

    with pytest.raises(NoSuchStaffError):
        system.assign_animal_to_vet("Nala", "FakeID123")

    with pytest.raises(InvalidStaffRoleError):
        system.assign_animal_to_vet("Nala", keeper.id)

    system.assign_animal_to_vet("Nala", vet1.id)

    with pytest.raises(DuplicateError):
        system.assign_animal_to_vet("Nala", vet2.id)


def test_assign_enclosure_to_keeper(system):
    system.add_enclosure(50, "Savannah")
    system.add_enclosure(100, "Savannah")

    system.add_staff("Petar Parker", 30, "Male", "01/01/1995", role="Keeper")

    e1 = system.enclosures[0]
    e2 = system.enclosures[1]
    keeper = system.staff[0]

    system.assign_enclosure_to_keeper(e1.id, keeper.id)
    system.assign_enclosure_to_keeper(e2.id, keeper.id)

    assert e1 in keeper.assigned_enclosures
    assert e2 in keeper.assigned_enclosures
    assert keeper.id in e1.keepers
    assert keeper.id in e2.keepers


def test_assign_enclosure_to_keeper_raises(system):
    system.add_enclosure(50, "Savannah")

    system.add_staff("Petar Parker", 30, "Male", "01/01/1995", role="Keeper")
    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Veterinarian")

    e1 = system.enclosures[0]
    keeper = system.staff[0]
    vet = system.staff[1]

    with pytest.raises(TypeError):
        system.assign_enclosure_to_keeper(123, keeper.id)

    with pytest.raises(TypeError):
        system.assign_enclosure_to_keeper(e1.id, 456)

    with pytest.raises(NoSuchEnclosureError):
        system.assign_enclosure_to_keeper("999Sav9", keeper.id)

    with pytest.raises(NoSuchStaffError):
        system.assign_enclosure_to_keeper(e1.id, "FakeID123")

    with pytest.raises(InvalidStaffRoleError):
        system.assign_enclosure_to_keeper(e1.id, vet.id)


def test_remove_animal(system):
    system.add_animal("Mammal", "Nala", "Lion", 10)
    system.add_animal("Mammal", "Mufasa", "Lion", 12)
    system.add_enclosure(50, "Savannah")

    a = system.animals[0]
    a2 = system.animals[1]
    system.remove_animal("Nala")


    assert len(system.animals) == 1
    assert a not in system.animals
    assert a2 in system.animals

    e = system.enclosures[0]
    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Veterinarian")
    vet = system.staff[0]
    system.assign_animal_to_vet("Mufasa", "NarUzu98")
    system.assign_animal_to_enclosure("Mufasa","50Sav1")
    a2.ailment = True
    system.create_health_entry("Mufasa", "05/06/2020", "Issue", "Details", 3, "Treatment")
    system.schedule_feeding_auto("05/06/2020")
    system.schedule_treatment_auto("05/06/2020")

    all_tasks = list(system.iter_tasks())
    all_tasks = list(system.iter_tasks())
    assert "Mufasa" in system.health_records

    system.remove_animal("Mufasa")

    remaining = list(system.iter_tasks())
    assert all(t.animal_id != "Mufasa" for _, _, _, t in remaining)

    assert "Mufasa" not in vet.assigned_animals
    assert a2 not in e.contains
    assert "Mufasa" not in system.health_records

def test_remove_animal_raises(system):
    system.add_animal("Mammal", "Nala", "Lion", 10)
    system.add_animal("Mammal", "Mufasa", "Lion", 12)
    a1 = system.animals[0]
    a2 = system.animals[1]
    a2.treatment = True

    with pytest.raises(CannotRemoveAnimalError):
        system.remove_animal("Mufasa")

    with pytest.raises(NoSuchAnimalError):
        system.remove_animal("Naruto Uzumaki")

    with pytest.raises(TypeError):
        system.remove_animal(9)

def test_remove_staff(system):

    system.add_enclosure(50, "Savannah")
    e = system.enclosures[0]
    e.cleanliness = 2

    system.add_staff("Petar Parkerh", 30, "Male", "01/01/1995", role="Keeper")
    keeper = system.staff[0]

    system.assign_enclosure_to_keeper(e.id, keeper.id)
    assert keeper.id in e.keepers

    system.schedule_cleaning_auto("05/06/2025")
    tasks = list(system.iter_tasks(date="05/06/2025"))
    assert len(tasks) > 0
    _, _, _, t = tasks[0]

    system.assign_task_to_staff(keeper.id, t.id)
    assert t.assigned is True
    assert t.assigned_to == keeper.id

    system.remove_staff(keeper.id)

    assert keeper not in system.staff
    assert keeper.id not in e.keepers

    assert t.assigned is False
    assert t.assigned_to is None

    for date, buckets in system.tasks_by_date.items():
        for status, groups in buckets.items():
            assert keeper.id not in groups


def test_remove_staff_raises(system):

    with pytest.raises(TypeError):
        system.remove_staff(123)

    with pytest.raises(NoSuchStaffError):
        system.remove_staff("FakeID123")

    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Veterinarian")
    system.add_animal("Mammal", "Mufasa", "Lion", 12)
    vet = system.staff[0]
    a = system.animals[0]
    vet.working_animal = a

    with pytest.raises(CannotRemoveStaffError):
        system.remove_staff(vet.id)

    system.add_enclosure(50, "Savannah")
    system.add_staff("Petar Parker", 30, "Male", "01/01/1995", role="Keeper")

    e = system.enclosures[0]
    keeper = system.staff[1]

    system.assign_enclosure_to_keeper(e.id, keeper.id)
    keeper.working_enclosure = e

    with pytest.raises(CannotRemoveStaffError):
        system.remove_staff(keeper.id)

def test_remove_enclosure(system):
    system.add_enclosure(50, "Savannah")
    system.add_staff("Petar Parker", 30, "Male", "01/01/1995", role="Keeper")

    e = system.enclosures[0]
    keeper = system.staff[0]

    system.assign_enclosure_to_keeper(e.id, keeper.id)
    assert keeper.id in e.keepers
    assert e in keeper.assigned_enclosures

    system.remove_enclosure(e.id)

    assert e not in system.enclosures
    assert e not in keeper.assigned_enclosures
    assert keeper.working_enclosure is None

    system.add_animal("Mammal", "Nala", "Lion", 10)
    system.add_enclosure(50, "Savannah")
    e= system.enclosures[0]
    a = system.animals[0]
    a.in_enclosure = e.id
    system.remove_enclosure(e.id)
    assert a.in_enclosure is None


def test_remove_enclosure_raises(system):

    with pytest.raises(TypeError):
        system.remove_enclosure(123)

    with pytest.raises(NoSuchEnclosureError):
        system.remove_enclosure("FakeID123")

    system.add_enclosure(50, "Savannah")
    system.add_animal("Mammal", "Nala", "Lion", 10)
    system.assign_animal_to_enclosure("Nala", "50Sav1")

    with pytest.raises(CannotRemoveEnclosureError):
        system.remove_enclosure("50Sav1")