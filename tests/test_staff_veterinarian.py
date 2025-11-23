'''
File: test_staff_veterinarian.py
Description: This module contains unit tests for Veterinarian objects.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from domain.staff.staff_veterinarian import Veterinarian
from exceptions import *


class FakeAnim:
    def __init__(self, name, ailment = False):
        self.name = name
        self.ailment = ailment
        self.treatment = False
        self.treated_by = None

@pytest.fixture
def vet():
    return Veterinarian("Naruto Uzumaki", 20, "Male", "15/06/1998", "NarUzu98")
@pytest.fixture
def sick_anim():
    return FakeAnim("Mufasa", ailment = True)
@pytest.fixture
def sick_anim2():
    return FakeAnim("Simba", ailment = True)

@pytest.fixture
def healthy_anim():
    return FakeAnim("Nala", ailment = False)

def test_init_sets_role_and_defaults(vet):
    assert vet.role == "Veterinarian"
    assert vet.assigned_animals == []
    assert vet.working_animal is None


def test_str_without_working_animal(vet):
    expected = "ID: NarUzu98 | Role: Veterinarian | Assigned Animals: 0 | Currently Treating: Nothing"
    assert str(vet) == expected


def test_str_with_working_animal(vet, sick_anim):
    vet.accept_assignment(sick_anim)
    vet.working_animal = sick_anim
    expected = "ID: NarUzu98 | Role: Veterinarian | Assigned Animals: 1 | Currently Treating: Mufasa"
    assert str(vet) == expected


def test_assigned_animals_property(vet, sick_anim, healthy_anim):
    vet.assigned_animals = [sick_anim, healthy_anim]
    assert vet.assigned_animals == [sick_anim, healthy_anim]
    assert sick_anim in vet.assigned_animals

def test_get_assigned_animal(vet, healthy_anim):
    with pytest.raises(NoAssignedAnimalsError):
        vet.get_assigned_animal("Yup")

    vet.accept_assignment(healthy_anim)
    assert vet.get_assigned_animal("Nala") == healthy_anim
    assert vet.get_assigned_animal("Mufasa") is None

def test_treat_animal_happy_path(vet, sick_anim, capsys):
    vet.accept_assignment(sick_anim)

    vet.treat_animal("Mufasa")

    assert vet.working_animal is sick_anim
    assert sick_anim.treatment is True
    assert sick_anim.treated_by == vet.id

    out = capsys.readouterr().out
    assert "NarUzu98 is treating Mufasa.\n" in out

def test_treat_animal_raises_not_assigned(vet):
    with pytest.raises(NoAssignedAnimalsError):
        vet.treat_animal("Nala")

def test_treat_animal_switching_animals(vet, sick_anim, sick_anim2, capsys):
    vet.accept_assignment(sick_anim)
    vet.treat_animal("Mufasa")

    vet.accept_assignment(sick_anim2)
    vet.treat_animal("Simba")

    out = capsys.readouterr().out

    assert "NarUzu98 has stopped treating Mufasa but animal still in need of medical attention." in out
    assert "NarUzu98 is treating Simba" in out

    assert vet.working_animal == sick_anim2
    assert vet.working_animal != sick_anim
    assert sick_anim in vet.assigned_animals

def test_stop_treating(vet, sick_anim, capsys):
    vet.accept_assignment(sick_anim)
    vet.treat_animal("Mufasa")
    vet.stop_treating_animal()
    out = capsys.readouterr().out

    assert vet.assigned_animals == [sick_anim]
    assert "NarUzu98 has stopped treating Mufasa but animal still in need of medical attention." in out
    assert vet.working_animal == None
    assert vet.working_animal != sick_anim

def test_heal_animal(vet, sick_anim, capsys):
    vet.accept_assignment(sick_anim)
    vet.treat_animal("Mufasa")
    vet.heal_animal()
    out = capsys.readouterr().out

    assert "NarUzu98 is treating Mufasa" in out
    assert "NarUzu98 has successfully treated Mufasa" in out
    assert "NarUzu98 has stopped treating Mufasa" in out
    assert sick_anim.ailment is False
    assert sick_anim in vet.assigned_animals


def test_health_check_all_assigned(vet, sick_anim, healthy_anim, capsys):
    vet.accept_assignment(sick_anim)
    vet.accept_assignment(healthy_anim)

    vet.health_check()
    out = capsys.readouterr().out

    assert "NarUzu98: Mufasa is in need of medical attention!" in out
    assert "NarUzu98: Nala is not in need of medical attention!" in out


def test_health_check_specific_sick(vet, sick_anim, capsys):
    vet.accept_assignment(sick_anim)

    vet.health_check("Mufasa")
    out = capsys.readouterr().out

    assert "NarUzu98: Mufasa is in need of medical attention!" in out


def test_health_check_specific_healthy(vet, healthy_anim, capsys):
    vet.accept_assignment(healthy_anim)

    vet.health_check("Nala")
    out = capsys.readouterr().out

    assert "NarUzu98: Nala is not in need of medical attention!" in out


def test_health_check_not_assigned(vet, sick_anim, capsys):
    vet.accept_assignment(sick_anim)

    vet.health_check("Scar")
    out = capsys.readouterr().out

    assert "Scar is not assigned to NarUzu98!" in out





