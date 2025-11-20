import pytest
from domain.staff.staff import Staff
from domain.staff.staff_veterinarian import Veterinarian
from domain.staff.staff_keeper import Keeper
from domain.enclosures.enclosure import Enclosure
from domain.animals.animal_mammal import Mammal
from domain.animals.animal_bird import Bird

@pytest.fixture
def staff():
    staff = Staff("Peter Parker", 18, "Male", "15/06/2001", "PetPar01")
def vet():
    return Veterinarian("Naruto Uzumaki", 20, "Male", "15/06/1998", "NarUzu98")
@pytest.fixture
def keeper():
    return Keeper("Mary Jane", 25, "Female", "15/06/1994", "MarJan94")

@pytest.fixture
def savannah_enclosure():
    return Enclosure(100, "Savannah", "100Sav1")

@pytest.fixture
def lion():
    return Mammal("Mufasa", "Lion", 8)

@pytest.fixture
def macaw():
    return Bird("Blue", "Macaw", 4)

@pytest.fixture
def keeper_with_enclosure(keeper, savannah_enclosure):
    keeper.accept_assignment(savannah_enclosure)
    return keeper

@pytest.fixture
def vet_with_lion(vet, lion):
    vet.accept_assignment(lion)
    return vet

