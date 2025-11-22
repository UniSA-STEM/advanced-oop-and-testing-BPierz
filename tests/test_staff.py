import pytest
from domain.staff.staff import Staff


@pytest.fixture
def staff():
    return Staff("Peter Parker", 18, "Male", "15/06/2001", "PetPar01")

def test_creation(staff):
    assert isinstance(staff, Staff)
    assert staff.name == "Peter Parker"
    assert staff.age == 18
    assert staff.gender == "Male"
    assert staff.birthday == "15/06/2001"
    assert staff.id == "PetPar01"
    assert staff.role is None
    assert staff.tasks == []

def test_age_low():
    with pytest.raises(ValueError):
        Staff("John Doe", 10, "male", "01/01/2000", "J01")

def test_age_high():
    with pytest.raises(ValueError):
        Staff("John", 150, "male", "01/01/2000", "J01")


def test_age_boundary_valid_low():
    staff = Staff("John", 15, "male", "01/01/2000", "J01")
    assert staff.age == 15


def test_age_boundary_valid_high():
    staff = Staff("John", 120, "male", "01/01/2000", "J01")
    assert staff.age == 120

def test_gender_invalid():
    with pytest.raises(ValueError):
        Staff("John", 30, "unknown", "01/01/2000", "J01")


def test_birthday_invalid():
    with pytest.raises(TypeError):
        staff = Staff("John", 30, "male", 20201010, "J01")

def test_repr_without_role(staff):
    assert repr(staff) == "ID: PetPar01 | Role: Staff Member"

def test_str_without_role(staff):
    assert str(staff) == "ID: PetPar01 | Role: None"

