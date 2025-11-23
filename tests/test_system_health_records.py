import pytest
from system.zoo_system import ZooSystem
from exceptions import *

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


def test_create_health_entry(system_with_lions):
    system = system_with_lions

    entry = system.create_health_entry(
        "Nala",
        "05/06/2020",
        "Injury",
        "Scratched leg",
        3,
        "Bandaging"
    )

    assert "Nala" in system.health_records
    assert len(system.health_records["Nala"]) == 1
    assert entry in system.health_records["Nala"]
    assert entry.date == "05/06/2020"
    assert entry.issue == "Injury"
    assert entry.details == "Scratched leg"
    assert entry.severity == 3
    assert entry.treatment == "Bandaging"

def test_create_health_entry_raises(system_with_lions):
    system = system_with_lions

    with pytest.raises(NoSuchAnimalError):
        system.create_health_entry(
            "Simba",
            "05/06/2020",
            "Injury",
            "Leg",
            2,
            "Medicine"
        )
    with pytest.raises(TypeError):
        system.create_health_entry(
            3,
            "05/06/2020",
            "Injury",
            "Leg",
            2,
            "Medicine"
        )
    with pytest.raises(TypeError):
        system.create_health_entry(
            "Nala",
            8,
            "Injury",
            "Leg",
            2,
            "Medicine"
        )
    with pytest.raises(ValueError):
        system.create_health_entry(
            "Nala",
            "05/06/2020",
            "Injury",
            "Leg",
            10,
            "Medicine"
        )

def test_create_health_entry_today(system_with_lions):
    system = system_with_lions

    entry = system.create_health_entry(
        "Nala",
        "today",
        "Cold",
        "Sneezing",
        1,
        "Rest"
    )

    today = system.validate_date("today")
    assert entry.date == today

def test_get_animal_health_record(system_with_lions):
    system = system_with_lions

    e1 = system.create_health_entry("Nala", "01/01/2020", "Injury", "Leg", 2, "Bandage")
    e2 = system.create_health_entry("Nala", "02/01/2020", "Fever", "Hot", 3, "Medicine")

    record = system.get_animal_health_record("Nala")

    assert len(record) == 2
    assert e1 in record
    assert e2 in record

    with pytest.raises(NoSuchAnimalError):
        system.get_animal_health_record("Simba")

