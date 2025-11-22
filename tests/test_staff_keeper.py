import pytest
from domain.staff.staff_keeper import Keeper
from exceptions import *

class FakeAnimal:
    def __init__(self, name, ailment=False, can_eat=True):
        self.name = name
        self.ailment = ailment
        self.eaten = False
        self.can_eat = can_eat

    def eat(self, food):
        if not self.can_eat:
            raise WrongFoodError("Cannot eat this")
        self.eaten = True


class FakeEnclosure:
    def __init__(self, id):
        self.id = id
        self.contains = []
        self.cleaned = False

    def be_cleaned(self):
        self.cleaned = True


@pytest.fixture
def keeper():
    return Keeper("John Doe", 30, "Male", "10/10/1990", "JohDoe90")

@pytest.fixture
def enclosure1():
    return FakeEnclosure("50Sav1")

@pytest.fixture
def enclosure2():
    return FakeEnclosure("80For2")

@pytest.fixture
def healthy_animal():
    return FakeAnimal("Mufasa", ailment=False)

@pytest.fixture
def sick_animal():
    return FakeAnimal("Nala", ailment=True)

@pytest.fixture
def refusing_food_animal():
    return FakeAnimal("Zazu", ailment=False, can_eat=False)


def test_init_sets_role_and_defaults(keeper):
    assert keeper.role == "Keeper"
    assert keeper.assigned_enclosures == []
    assert keeper.working_enclosure is None


def test_str_without_working_enclosure(keeper):
    expected = "ID: JohDoe90 | Role: Keeper | Assigned Enclosures: 0 | Currently Working: Nothing"
    assert str(keeper) == expected


def test_str_with_working_enclosure(keeper, enclosure1):
    keeper.accept_assignment(enclosure1)
    keeper.working_enclosure = enclosure1
    expected = "ID: JohDoe90 | Role: Keeper | Assigned Enclosures: 1 | Currently Working: 50Sav1"
    assert str(keeper) == expected


def test_accept_assignment(keeper, enclosure1):
    keeper.accept_assignment(enclosure1)
    assert keeper.assigned_enclosures == [enclosure1]

    with pytest.raises(DuplicateError):
        keeper.accept_assignment(enclosure1)


def test_get_assigned_enclosure(keeper, enclosure1, enclosure2):
    with pytest.raises(NoAssignedEnclosuresError):
        keeper.get_assigned_enclosure("50Sav1")

    keeper.accept_assignment(enclosure1)
    keeper.accept_assignment(enclosure2)

    assert keeper.get_assigned_enclosure("80For2") is enclosure2
    assert keeper.get_assigned_enclosure("999XXX") is None


def test_set_working_enclosure(keeper, enclosure1):
    keeper.accept_assignment(enclosure1)
    keeper.set_working_enclosure("50Sav1")
    assert keeper.working_enclosure is enclosure1

    with pytest.raises(EnclosureNotAvailableError):
        keeper.set_working_enclosure("999XXX")


def test_clean_enclosure(keeper, enclosure1):
    keeper.accept_assignment(enclosure1)
    keeper.working_enclosure = enclosure1
    keeper.clean_enclosure()
    assert enclosure1.cleaned is True


def test_feed_animals_success(keeper, enclosure1, healthy_animal, capsys):
    enclosure1.contains.append(healthy_animal)
    keeper.accept_assignment(enclosure1)
    keeper.working_enclosure = enclosure1

    keeper.feed_animals("meat")
    out = capsys.readouterr().out

    assert "John Doe fed all animals in enclosure 50Sav1 with meat" in out
    assert healthy_animal.eaten is True


def test_feed_animals_rejecting_food(keeper, enclosure1, refusing_food_animal, capsys):
    enclosure1.contains.append(refusing_food_animal)
    keeper.accept_assignment(enclosure1)
    keeper.working_enclosure = enclosure1

    keeper.feed_animals("meat")
    out = capsys.readouterr().out

    assert "Could not feed Zazu: Cannot eat this" in out


def test_feed_animals_no_working_enclosure(keeper):
    with pytest.raises(EnclosureNotAvailableError):
        keeper.feed_animals("meat")


def test_feed_single_animal(keeper, healthy_animal, capsys):
    keeper.feed_animal(healthy_animal, "fruit")
    out = capsys.readouterr().out

    assert "John Doe fed Mufasa with fruit" in out
    assert healthy_animal.eaten is True


def test_health_check_all_assigned(keeper, enclosure1, healthy_animal, sick_animal, capsys):
    enclosure1.contains.extend([healthy_animal, sick_animal])
    keeper.accept_assignment(enclosure1)

    keeper.health_check()
    out = capsys.readouterr().out

    assert "JohDoe90: Nala is in need of medical attention!" in out
    assert "No animals need medical attention!" not in out


def test_health_check_none_need_attention(keeper, enclosure1, healthy_animal, capsys):
    enclosure1.contains.append(healthy_animal)
    keeper.accept_assignment(enclosure1)

    keeper.health_check()
    out = capsys.readouterr().out

    assert "No animals need medical attention!" in out


def test_health_check_specific_animal_found(keeper, enclosure1, sick_animal, capsys):
    enclosure1.contains.append(sick_animal)
    keeper.accept_assignment(enclosure1)

    keeper.health_check(animal_name="Nala")
    out = capsys.readouterr().out

    assert "JohDoe90: Nala is in need of medical attention!" in out


def test_health_check_specific_animal_not_found(keeper, enclosure1, healthy_animal, capsys):
    enclosure1.contains.append(healthy_animal)
    keeper.accept_assignment(enclosure1)

    keeper.health_check(animal_name="Simba")
    out = capsys.readouterr().out

    assert "Simba is not in keepers assigned enclosures." in out


def test_health_check_specific_enclosure_ok(keeper, enclosure1, sick_animal, capsys):
    enclosure1.contains.append(sick_animal)
    keeper.accept_assignment(enclosure1)

    keeper.health_check(enclosure_id="50Sav1")
    out = capsys.readouterr().out

    assert "JohDoe90: Nala is in need of medical attention!" in out


def test_health_check_specific_enclosure_not_assigned(keeper, capsys):
    keeper.health_check(enclosure_id="999XXX")
    out = capsys.readouterr().out

    assert "JohDoe90 is not assigned to enclosure 999XXX." in out