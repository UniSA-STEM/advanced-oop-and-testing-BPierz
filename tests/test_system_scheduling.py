'''
File: test_system_schedulling.py
Description: This module contains unit tests for ZooSystem objects' schedulling functionalities.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''



import pytest
from exceptions import *
from system.zoo_system import ZooSystem
from datetime import datetime
from domain.records.cleaning_task import CleaningTask
from domain.records.feeding_task import FeedingTask
from domain.records.treatment_task import TreatmentTask


@pytest.fixture
def system():
    return ZooSystem("Sue's Zoo")

@pytest.fixture
def system_with_savannah(system):
    system = system
    system.add_enclosure(50, "Savannah")
    return system

@pytest.fixture
def system_with_lions(system_with_savannah):
    system = system_with_savannah
    system.add_animal("Mammal", "Nala", "Lion", 10)
    system.add_animal("Mammal", "Mufasa", "Lion", 12)
    return system

@pytest.fixture
def system_with_lions_assigned(system_with_lions):
    system = system_with_lions
    e = system.enclosures[0]
    system.assign_animal_to_enclosure("Nala", e.id)
    system.assign_animal_to_enclosure("Mufasa", e.id)
    return system

@pytest.fixture
def system_with_lions_and_vet(system_with_lions):
    system = system_with_lions
    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Veterinarian")
    vet = system.staff[0]
    system.assign_animal_to_vet("Nala", vet.id)
    return system

def test_validate_date(system):
    today = datetime.today().strftime("%d/%m/%Y")
    assert system.validate_date("today") == today
    assert system.validate_date("now") == today
    assert system.validate_date("  TODAY  ") == today

def test_validate_date_raises(system):
    with pytest.raises(InvalidDateError):
        system.validate_date("2025/12/05")
        system.validate_date("05-12-2025")
        system.validate_date("5/12/2025")
        system.validate_date("05/14/2025")
        system.validate_date("32/12/2025")
        system.validate_date("wrong")

    with pytest.raises(TypeError):
        system.validate_date(None)
        system.validate_date(10)

def test_get_date_key(system):
    today = datetime.today().strftime("%d/%m/%Y")
    assert system.get_date_key("today") == today
    assert system.get_date_key("today") == today
    assert system.get_date_key("now") == today
    assert system.get_date_key("  TODAY  ") == today
    assert system.get_date_key(None) == "UNSCHEDULED"

def test_get_or_create_date_slot(system):
    slot = system.get_or_create_date_slot("05/06/2020")
    slot2 = system.get_or_create_date_slot()
    slot3 = system.get_or_create_date_slot("06/06/2020")

    assert "05/06/2020" in system.tasks_by_date
    assert isinstance(slot, dict)
    assert "uncompleted" in slot
    assert "completed" in slot
    assert slot["uncompleted"] == {}
    assert slot["completed"] == {}

    assert "UNSCHEDULED" in system.tasks_by_date
    assert slot2 is system.tasks_by_date["UNSCHEDULED"]
    assert slot2["uncompleted"] == {}
    assert slot2["completed"] == {}

    assert "05/06/2020" in system.tasks_by_date
    assert "06/06/2020" in system.tasks_by_date
    assert slot is system.tasks_by_date["05/06/2020"]
    assert slot3 is system.tasks_by_date["06/06/2020"]
    assert slot is not slot3

def test_get_or_create_reuses_existing(system):
    first = system.get_or_create_date_slot("05/06/2020")
    first["uncompleted"]["NarUzu98"] = ["task1"]
    second = system.get_or_create_date_slot("05/06/2020")

    assert second is first
    assert "NarUzu98" in second["uncompleted"]
    assert second["uncompleted"]["NarUzu98"] == ["task1"]

def test_add_task(system):
    task = CleaningTask("50Sav1", "05/06/2020")
    system.add_task(task, date = "05/06/2020")
    slot = system.tasks_by_date["05/06/2020"]

    assert "UNASSIGNED" in slot["uncompleted"]
    assert task in slot["uncompleted"]["UNASSIGNED"]

    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Keeper")
    nar_id = system.staff[0].id

    task = FeedingTask("50Sav1", ["Nala"], "05/06/2020")
    system.add_task(task, date = "05/06/2020", staff_id = nar_id)
    slot = system.tasks_by_date["05/06/2020"]

    assert nar_id in slot["uncompleted"]
    assert task in slot["uncompleted"][nar_id]

def test_add_many_tasks(system):
    system.add_staff("Peter Parker", 22, "Male", "10/10/2002", role="Keeper")
    pet_id = system.staff[0].id

    t1 = CleaningTask("50Sav1", "06/06/2020")
    t2 = FeedingTask("50Sav1", ["Mufasa"], "06/06/2020")

    system.add_task(t1, date="06/06/2020", staff_id=pet_id)
    system.add_task(t2, date="06/06/2020", staff_id=pet_id)

    bucket = system.tasks_by_date["06/06/2020"]["uncompleted"]

    assert len(bucket[pet_id]) == 2
    assert t1 in bucket[pet_id]
    assert t2 in bucket[pet_id]

def test_add_multiple_unassigned_tasks(system):
    t1 = CleaningTask("50Sav1", "06/06/2020")
    t2 = CleaningTask("100Sav1", "06/06/2020")

    system.add_task(t1, date="06/06/2020")
    system.add_task(t2, date="06/06/2020")

    bucket = system.tasks_by_date["06/06/2020"]["uncompleted"]

    assert "UNASSIGNED" in bucket
    assert bucket["UNASSIGNED"] == [t1, t2]

def test_add_task_creates_new_date_slot(system):
    task = TreatmentTask("Mufasa", "05/06/2020")
    system.add_task(task, date="05/06/2020")

    slot = system.tasks_by_date["05/06/2020"]
    assert "uncompleted" in slot
    assert "UNASSIGNED" in slot["uncompleted"]
    assert task in slot["uncompleted"]["UNASSIGNED"]

def test_schedule_cleaning_auto(system):
    system.add_enclosure(50, "Savannah")
    system.add_enclosure(40, "Tropical Aviary")
    e1 = system.enclosures[0]
    e2 = system.enclosures[1]

    e1.cleanliness = 2
    e2.cleanliness = 5

    system.schedule_cleaning_auto("05/06/2020")

    slot = system.tasks_by_date["05/06/2020"]["uncompleted"]


    all_tasks = [t for tasks in slot.values() for t in tasks]
    assert len(all_tasks) == 1

    task = all_tasks[0]
    assert isinstance(task, CleaningTask)
    assert task.enclosure_id == e1.id
    assert task.date == "05/06/2020"
    assert task.id is not None

    system.schedule_cleaning_auto("05/06/2020")
    assert len(all_tasks) == 1

def test_schedule_cleaning_auto_unscheduled(system):
    system.add_enclosure(50, "Savannah")
    e = system.enclosures[0]
    e.cleanliness = 1
    system.schedule_cleaning_auto()
    assert "UNSCHEDULED" in system.tasks_by_date
    bucket = system.tasks_by_date["UNSCHEDULED"]["uncompleted"]

    all_tasks = [t for tasks in bucket.values() for t in tasks]
    assert len(all_tasks) == 1

    task = all_tasks[0]
    assert isinstance(task, CleaningTask)
    assert task.enclosure_id == e.id
    assert task.date == "UNSCHEDULED"

def test_schedule_cleaning_auto_not_need_cleaning(system):
    system.add_enclosure(50, "Savannah")
    system.add_enclosure(60, "Tropical Aviary")

    system.enclosures[0].cleanliness = 4
    system.enclosures[1].cleanliness = 5

    system.schedule_cleaning_auto("10/06/2020")

    assert "10/06/2020" not in system.tasks_by_date

def test_schedule_feeding_auto(system_with_lions_assigned):
    system = system_with_lions_assigned
    e = system.enclosures[0]

    for a in e.contains:
        a.hungry = True

    system.schedule_feeding_auto("05/06/2020")

    slot = system.tasks_by_date["05/06/2020"]["uncompleted"]
    all_tasks = [t for tasks in slot.values() for t in tasks]

    assert len(all_tasks) == 1

    task = all_tasks[0]
    assert isinstance(task, FeedingTask)
    assert task.enclosure_id == e.id
    assert task.animals == ["All Animals"]
    assert task.date == "05/06/2020"

def test_schedule_feeding_auto_some_hungry(system_with_lions_assigned):
    system = system_with_lions_assigned
    e = system.enclosures[0]

    for a in e.contains:
        a.hungry = False

    nala = system.get_animal("Nala")
    nala.hungry = True

    system.schedule_feeding_auto("06/06/2020")

    slot = system.tasks_by_date["06/06/2020"]["uncompleted"]
    all_tasks = [t for tasks in slot.values() for t in tasks]

    assert len(all_tasks) == 1

    task = all_tasks[0]
    assert isinstance(task, FeedingTask)
    assert task.enclosure_id == e.id
    assert task.animals == ["Nala"]

def test_schedule_feeding_auto_none_hungry(system_with_lions_assigned):
    system = system_with_lions_assigned
    e = system.enclosures[0]

    for a in e.contains:
        a.hungry = False

    system.schedule_feeding_auto("06/06/2020")

    assert "06/06/2020" not in system.tasks_by_date

def test_schedule_feeding_auto_no_duplicates(system_with_lions_assigned):
    system = system_with_lions_assigned
    e = system.enclosures[0]
    system.schedule_feeding_auto("06/06/2020")

    slot = system.tasks_by_date["06/06/2020"]["uncompleted"]
    first_tasks = [t for tasks in slot.values() for t in tasks]
    first_ids = [t.id for t in first_tasks]

    system.schedule_feeding_auto("06/06/2020")

    slot2 = system.tasks_by_date["06/06/2020"]["uncompleted"]
    second_tasks = [t for tasks in slot2.values() for t in tasks]
    second_ids = [t.id for t in second_tasks]

    assert len(second_tasks) == len(first_tasks)
    assert set(second_ids) == set(first_ids)


def test_schedule_treatment_and_assign_to_vet(system_with_lions_and_vet):
    system = system_with_lions_and_vet
    vet = system.staff[0]
    nala = system.get_animal("Nala")

    nala.ailment = True

    system.schedule_treatment_auto("06/06/2020")

    slot = system.tasks_by_date["06/06/2020"]["uncompleted"]
    all_tasks = [t for tasks in slot.values() for t in tasks]

    assert len(all_tasks) == 1

    task = all_tasks[0]
    assert isinstance(task, TreatmentTask)
    assert task.animal_id == "Nala"
    assert task.date == "06/06/2020"
    assert task.assigned is False
    assert task.assigned_to is None

    system.assign_task_to_staff(vet.id, task.id)

    slot_after = system.tasks_by_date["06/06/2020"]["uncompleted"]
    assert vet.id in slot_after
    assert task in slot_after[vet.id]
    assert task.assigned is True
    assert task.assigned_to == vet.id
    assert task in vet.tasks


def test_schedule_treatment_auto_no_ailments(system_with_lions):
    system = system_with_lions

    for a in system.animals:
        a.ailment = False

    system.schedule_treatment_auto("07/06/2020")

    assert "07/06/2020" not in system.tasks_by_date


def test_assign_treatment_task_wrong_role(system_with_lions):
    system = system_with_lions
    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Veterinarian")
    system.add_staff("Peter Parker", 22, "Male", "10/10/2002", role="Keeper")

    vet = system.staff[0]
    keeper = system.staff[1]

    nala = system.get_animal("Nala")
    nala.ailment = True

    system.schedule_treatment_auto("08/06/2020")

    slot = system.tasks_by_date["08/06/2020"]["uncompleted"]
    all_tasks = [t for tasks in slot.values() for t in tasks]
    task = all_tasks[0]

    with pytest.raises(InvalidStaffRoleError):
        system.assign_task_to_staff(keeper.id, task.id)

    system.assign_animal_to_vet("Nala", vet.id)
    system.assign_task_to_staff(vet.id, task.id)
    assert task in vet.tasks


def test_assign_treatment_task_vet_not_assigned_animal(system_with_lions):
    system = system_with_lions
    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Veterinarian")
    vet = system.staff[0]

    nala = system.get_animal("Nala")
    nala.ailment = True

    system.schedule_treatment_auto("09/06/2020")

    slot = system.tasks_by_date["09/06/2020"]["uncompleted"]
    all_tasks = [t for tasks in slot.values() for t in tasks]
    task = all_tasks[0]

    with pytest.raises(InvalidTaskAssignmentError):
        system.assign_task_to_staff(vet.id, task.id)

def test_iter_tasks_core(system):

    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Keeper")
    nar = system.staff[0]

    t1 = CleaningTask("50Sav1", "05/06/2020")
    t2 = FeedingTask("50Sav1", ["Nala"], "05/06/2020")
    t3 = TreatmentTask("Mufasa", "06/06/2020")

    system.add_task(t1, date="05/06/2020")
    system.add_task(t2, date="05/06/2020", staff_id=nar.id)
    system.add_task(t3, date="06/06/2020")

    all_tasks = list(system.iter_tasks())
    ids = {t.id for _,_,_,t in all_tasks}
    assert {t1.id, t2.id, t3.id} == ids

    tasks_05 = list(system.iter_tasks(date="05/06/2020"))
    ids_05 = {t.id for _,_,_,t in tasks_05}
    assert ids_05 == {t1.id, t2.id}

    tasks_06 = list(system.iter_tasks(date="06/06/2020"))
    ids_06 = {t.id for _,_,_,t in tasks_06}
    assert ids_06 == {t3.id}

    assigned = list(system.iter_tasks(assigned=True))
    unassigned = list(system.iter_tasks(assigned=False))

    assert {t.id for _,_,_,t in assigned} == {t2.id}
    assert {t.id for _,_,_,t in unassigned} == {t1.id, t3.id}

    nar_tasks = list(system.iter_tasks(staff_id=nar.id))
    assert len(nar_tasks) == 1
    assert nar_tasks[0][3] is t2

def test_complete_cleaning_tasks(system_with_savannah):
    system = system_with_savannah
    e = system.enclosures[0]

    e.cleanliness = 2
    system.add_staff("Bob Keeper", 30, "Male", "01/01/1995", role="Keeper")
    keeper = system.staff[0]

    t1 = CleaningTask(e.id, "05/06/2020")
    system.add_task(t1, date="05/06/2020", staff_id=keeper.id)

    with pytest.raises(IncompleteTaskError):
        system.complete_task(t1.id)

    slot = system.tasks_by_date["05/06/2020"]
    assert keeper.id in slot["uncompleted"]
    assert t1 in slot["uncompleted"][keeper.id]
    assert keeper.id not in slot["completed"]

    e.cleanliness = 4
    system.complete_task(t1.id)

    slot = system.tasks_by_date["05/06/2020"]
    assert keeper.id not in slot["uncompleted"]
    assert keeper.id in slot["completed"]
    assert t1 in slot["completed"][keeper.id]
    assert t1.complete is True

    with pytest.raises(InvalidTaskAssignmentError):
        system.complete_task(t1.id)

def test_complete_treatment_tasks(system_with_lions):
    system = system_with_lions
    mufasa = system.get_animal("Mufasa")

    system.add_staff("Naruto Uzumaki", 20, "Male", "15/06/1998", role="Veterinarian")
    vet = system.staff[0]
    system.assign_animal_to_vet("Mufasa", vet.id)

    mufasa.ailment = True
    t1 = TreatmentTask("Mufasa", "06/06/2020")
    system.add_task(t1, date="06/06/2020", staff_id=vet.id)

    with pytest.raises(IncompleteTaskError):
        system.complete_task(t1.id)

    slot = system.tasks_by_date["06/06/2020"]
    assert vet.id in slot["uncompleted"]
    assert t1 in slot["uncompleted"][vet.id]
    assert vet.id not in slot["completed"]

    mufasa.ailment = False
    system.complete_task(t1.id)

    slot = system.tasks_by_date["06/06/2020"]
    assert vet.id not in slot["uncompleted"]
    assert vet.id in slot["completed"]
    assert t1 in slot["completed"][vet.id]
    assert t1.complete is True

    with pytest.raises(InvalidTaskAssignmentError):
        system.complete_task(t1.id)

def test_complete_feeding_task_named_and_all(system_with_lions_assigned):
    system = system_with_lions_assigned
    e = system.enclosures[0]

    nala = system.get_animal("Nala")
    mufasa = system.get_animal("Mufasa")

    system.add_staff("Peter Parker", 22, "Male", "10/10/2002", role="Keeper")
    keeper = system.staff[0]

    nala.hungry = True
    mufasa.hungry = True

    task_named = FeedingTask(e.id, ["Nala", "Mufasa"], "06/06/2020")
    system.add_task(task_named, date="06/06/2020", staff_id=keeper.id)

    nala.hungry = False
    mufasa.hungry = True

    with pytest.raises(IncompleteTaskError):
        system.complete_task(task_named.id)

    mufasa.hungry = False
    system.complete_task(task_named.id)

    slot_named = system.tasks_by_date["06/06/2020"]
    assert keeper.id not in slot_named["uncompleted"]
    assert keeper.id in slot_named["completed"]
    assert task_named in slot_named["completed"][keeper.id]
    assert task_named.complete is True

    nala.hungry = True
    mufasa.hungry = True

    task_all = FeedingTask(e.id, ["All Animals"], "07/06/2020")
    system.add_task(task_all, date="07/06/2020", staff_id=keeper.id)

    nala.hungry = False
    with pytest.raises(IncompleteTaskError):
        system.complete_task(task_all.id)

    mufasa.hungry = False
    system.complete_task(task_all.id)

    slot_all = system.tasks_by_date["07/06/2020"]
    assert keeper.id not in slot_all["uncompleted"]
    assert keeper.id in slot_all["completed"]
    assert task_all in slot_all["completed"][keeper.id]
    assert task_all.complete is True