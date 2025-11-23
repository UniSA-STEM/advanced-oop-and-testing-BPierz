'''
File: test_enclosure.py
Description: This module contains unit tests for enclosure objects.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''


from domain.enclosures.enclosure import Enclosure
from domain.animals.animal_mammal import Mammal
import pytest

@pytest.fixture
def enclosure():
    return Enclosure(50, "Savannah", "50Sav1")
@pytest.fixture
def lion():
    return Mammal("Simba", "Lion", 12, "savannah", ["meat", "bones", "organs"], "Raur")
@pytest.fixture
def macaw():
    return Mammal("Blue", "Macaw", 14, "tropical aviary", ["fruit", "nuts", "seeds"], "Squawk")
class TestEnclosure:

    def test_attributes(self, enclosure):
        assert enclosure.id == "50Sav1"
        assert enclosure.type == "Savannah"
        assert enclosure.size == 50

    def test_str(self, enclosure):
        assert str(enclosure) == (f"-----------------------\n"
                f"Enclosure ID: 50Sav1\n"
                f"Type: Savannah\n"
                f"Contains: Nothing\n"
                f"Keepers Assigned: None\n"
                f"Cleanliness: 5/5\n"
                f"-----------------------\n")

    def test_keepers_assigned(self, enclosure):
        enclosure.keepers = ["PetPar01", "MarJan02"]
        assert enclosure.keepers == ["PetPar01", "MarJan02"]
        assert str(enclosure) == (f"-----------------------\n"
                f"Enclosure ID: 50Sav1\n"
                f"Type: Savannah\n"
                f"Contains: Nothing\n"
                f"Keepers Assigned: PetPar01, MarJan02\n"
                f"Cleanliness: 5/5\n"
                f"-----------------------\n")

    def test_cleanliness(self, enclosure):
        enclosure.cleanliness = 2
        assert enclosure.cleanliness == 2
        enclosure.cleanliness = -5
        assert enclosure.cleanliness == 0
        enclosure.cleanliness = 10
        assert enclosure.cleanliness == 5

    def test_be_cleaned(self, enclosure):
        original = enclosure.cleanliness
        enclosure.be_cleaned()
        assert enclosure.cleanliness == original + 1

    def test_store_adds_animal(self, enclosure, lion):
        enclosure.store(lion)
        assert lion in enclosure.contains
        assert len(enclosure.contains) == 1

    def test_can_store_ok(self, enclosure, lion):
        assert enclosure.can_store(lion) is True

    def test_can_store_wrong_enclosure(self, enclosure, macaw):
        from exceptions import IncompatibleEnclosureError

        with pytest.raises(IncompatibleEnclosureError):
            enclosure.can_store(macaw)

    def test_can_store_different_species_when_occupied(self, enclosure, lion, macaw):
        from exceptions import IncompatibleEnclosureError

        enclosure.store(lion)

        with pytest.raises(IncompatibleEnclosureError):
            enclosure.can_store(macaw)

    def test_can_store_same_species(self, enclosure, lion):
        lion2 = lion
        enclosure.store(lion)
        assert enclosure.can_store(lion2) is True

    def test_report_prints_correctly(self, enclosure, lion, capsys):
        enclosure.store(lion)
        enclosure.report()
        out = capsys.readouterr().out

        assert "Cleanliness:" in out
        assert "Animals:" in out
        assert "Simba" in out

