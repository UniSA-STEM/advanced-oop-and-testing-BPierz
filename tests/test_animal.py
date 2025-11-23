'''
File: test_animal.py
Description: This module contains unit tests for animal objects.
Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''



from domain.animals.animal_mammal import Mammal
from domain.animals.animal_bird import Bird
from domain.animals.animal_reptile import Reptile
from exceptions import *

@pytest.fixture
def bird():
    return Bird("Blue", "macaw", 15, "tropical aviary", ["seeds", "nuts", "fruit"], "squawk")
def mammal():
    return Mammal("Simba", "Lion", 45, "Savannah", ["meat", "organs", "bones"], "roar")
@pytest.fixture
def reptile():
    return Reptile("Coby", "Cobra", 17, "tropical terrarium", ["mice", "rats", "frogs", "small birds"], "hisss")


def test_make_sound(bird, capsys):
    bird.make_sound()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Blue: "squawk"'


def test_can_eat_when_food_in_diet(bird):
    assert bird.can_eat("seeds") is True
    assert bird.can_eat("nuts") is True
    assert bird.can_eat("fruits") is False
    assert bird.can_eat("fruit") is True

def test_can_eat_false_when_food_not_in_diet(bird):
    assert bird.can_eat("meat") is False
    assert bird.can_eat("organs") is False
    assert bird.can_eat("squawk") is False
    assert bird.can_eat("hisss") is False

def test_eat_sets_hungry_false_prints(bird, capsys):
    assert bird.hungry is True

    bird.eat("seeds")
    captured = capsys.readouterr()

    assert "Blue the Macaw eats seeds." in captured.out.strip()
    assert bird.hungry is False

def test_eat_error_when_cannot_eat(bird):
    with pytest.raises(WrongFoodError):
        bird.eat("meat")

def test_eat_error_if_asleep(bird):
    bird.sleep()
    with pytest.raises(AnimalAsleepError):
        bird.eat("seeds")

def test_drink_sets_thirsty_false_prints(bird, capsys):
    bird._Animal__thirsty = True
    bird.drink()
    captured = capsys.readouterr()
    assert "Blue drank and is no longer thirsty." == captured.out.strip()
    assert bird._Animal__thirsty is False

def test_drink_error_if_asleep(bird, capsys):
    bird.sleep()
    with pytest.raises(AnimalAsleepError):
        bird.drink()

def test_move_print(bird, capsys):
    bird.move()
    captured = capsys.readouterr()
    assert f"Blue flies through the air." == captured.out.strip()

def test_move_error_if_asleep(bird, capsys):
    bird.sleep()
    with pytest.raises(AnimalAsleepError):
        bird.move()
