'''
File: zoo_data.py
Description: This module stores predefined animal data used by the zoo system. It contains dictionaries
             describing species information for mammals, birds, and reptiles, including dietary needs,
             environmental requirements, and characteristic sounds. These data structures act as reference
             tables for creating animal objects and validating species attributes throughout the zoo system.

Author: Borys Pierzchala
ID: 110457330
Username: PIEBY002
This is my own work as defined by the University's Academic Integrity Policy.
'''

MAMMAL_DATA = {
    "Lion": {"class": "mammal", "diet": "carnivore", "enclosure": "Savannah", "sound": "roar"},
    "Black Bear": {"class": "mammal", "diet": "carnivore", "enclosure": "Forest", "sound": "growl"},
    "Brown Bear": {"class": "mammal", "diet": "carnivore", "enclosure": "Forest", "sound": "growl"},
    "Polar Bear": {"class": "mammal", "diet": "carnivore", "enclosure": "Arctic", "sound": "huff"},
    "Grizzly Bear": {"class": "mammal", "diet": "carnivore", "enclosure": "Forest", "sound": "roar"},
    "Giraffe": {"class": "mammal", "diet": "herbivore", "enclosure": "Savannah", "sound": "hum"},
    "Zebra": {"class": "mammal", "diet": "herbivore", "enclosure": "Savannah", "sound": "whinny"},
    "Puma": {"class": "mammal", "diet": "herbivore", "enclosure": "Mountain", "sound": "growl"},
    "Meerkat": {"class": "mammal", "diet": "herbivore", "enclosure": "Desert", "sound": "chirp"},
    "Hippopotamus": {"class": "mammal", "diet": "herbivore", "enclosure": "Wetlands", "sound": "grunt"},
    "Rhinoceros": {"class": "mammal", "diet": "herbivore", "enclosure": "Savannah", "sound": "snort"},
    "Cheetah": {"class": "mammal", "diet": "carnivore", "enclosure": "Savannah", "sound": "chirp"},
    "Leopard": {"class": "mammal", "diet": "carnivore", "enclosure": "Forest", "sound": "growl"},
    "Tiger": {"class": "mammal", "diet": "carnivore", "enclosure": "Rainforest", "sound": "roar"},
    "Gorilla": {"class": "mammal", "diet": "herbivore", "enclosure": "Rainforest", "sound": "hoot"},
    "Chimpanzee": {"class": "mammal", "diet": "omnivore", "enclosure": "Rainforest", "sound": "screech"},
    "Orangutan": {"class": "mammal", "diet": "herbivore", "enclosure": "Rainforest", "sound": "long call"},
    "Kangaroo": {"class": "mammal", "diet": "herbivore", "enclosure": "Grassland", "sound": "thump"},
    "Koala": {"class": "mammal", "diet": "herbivore", "enclosure": "Eucalyptus Forest", "sound": "bellow"},
    "Red Panda": {"class": "mammal", "diet": "herbivore", "enclosure": "Mountain Forest", "sound": "chirp"},
    "Wolf": {"class": "mammal", "diet": "carnivore", "enclosure": "Forest", "sound": "howl"},
    "Hyena": {"class": "mammal", "diet": "carnivore", "enclosure": "Savannah", "sound": "cackle"},
    "Bison": {"class": "mammal", "diet": "herbivore", "enclosure": "Grassland", "sound": "bellow"},
    "Camel": {"class": "mammal", "diet": "herbivore", "enclosure": "Desert", "sound": "grunt"},
    "Llama": {"class": "mammal", "diet": "herbivore", "enclosure": "Mountain", "sound": "hum"},
    "Capybara": {"class": "mammal", "diet": "herbivore", "enclosure": "Wetlands", "sound": "whistle"},
    "Otter": {"class": "mammal", "diet": "carnivore", "enclosure": "Riverbank", "sound": "chirp"},
    "Seal": {"class": "mammal", "diet": "carnivore", "enclosure": "Arctic Pool", "sound": "bark"},
    "Sea Lion": {"class": "mammal", "diet": "carnivore", "enclosure": "Coastal Pool", "sound": "bark"},
    "Dolphin": {"class": "mammal", "diet": "carnivore", "enclosure": "Aquarium", "sound": "click"}
}

MAMMAL_ENCLOSURES = list(set(info["enclosure"] for info in MAMMAL_DATA.values()))

REPTILE_DATA = {
    "Cobra": {"class": "reptile", "diet": "carnivore", "enclosure": "tropical terrarium", "sound": "hiss"},
    "King Cobra": {"class": "reptile", "diet": "carnivore", "enclosure": "tropical terrarium", "sound": "hiss"},
    "Python": {"class": "reptile", "diet": "carnivore", "enclosure": "tropical terrarium", "sound": "hiss"},
    "Boa Constrictor": {"class": "reptile", "diet": "carnivore", "enclosure": "tropical terrarium", "sound": "hiss"},
    "Anaconda": {"class": "reptile", "diet": "carnivore", "enclosure": "aquatic reptile", "sound": "hiss"},
    "Komodo Dragon": {"class": "reptile", "diet": "carnivore", "enclosure": "tropical terrarium", "sound": "growl"},
    "Monitor Lizard": {"class": "reptile", "diet": "carnivore", "enclosure": "tropical terrarium", "sound": "hiss"},
    "Bearded Dragon": {"class": "reptile", "diet": "omnivore", "enclosure": "desert terrarium", "sound": "chirp"},
    "Iguana": {"class": "reptile", "diet": "herbivore", "enclosure": "tropical terrarium", "sound": "rustle"},
    "Chameleon": {"class": "reptile", "diet": "carnivore", "enclosure": "tropical terrarium", "sound": "click"},
    "Gecko": {"class": "reptile", "diet": "carnivore", "enclosure": "desert terrarium", "sound": "chirp"},
    "Horned Viper": {"class": "reptile", "diet": "carnivore", "enclosure": "desert terrarium", "sound": "hiss"},
    "Desert Tortoise": {"class": "reptile", "diet": "herbivore", "enclosure": "desert terrarium", "sound": "rustle"},
    "Giant Tortoise": {"class": "reptile", "diet": "herbivore", "enclosure": "tropical terrarium", "sound": "grunt"},
    "Crocodile": {"class": "reptile", "diet": "carnivore", "enclosure": "aquatic reptile", "sound": "bellow"},
    "Alligator": {"class": "reptile", "diet": "carnivore", "enclosure": "aquatic reptile", "sound": "bellow"},
    "Sea Turtle": {"class": "reptile", "diet": "herbivore", "enclosure": "aquatic reptile", "sound": "splash"}
}



REPTILE_ENCLOSURES = list(set(info["enclosure"] for info in REPTILE_DATA.values()))


BIRD_DATA = {
    "Eagle": {"class": "bird", "diet": "carnivore", "enclosure": "aviary", "sound": "screech"},
    "Hawk": {"class": "bird", "diet": "carnivore", "enclosure": "aviary", "sound": "screech"},
    "Owl": {"class": "bird", "diet": "carnivore", "enclosure": "aviary", "sound": "hoot"},
    "Falcon": {"class": "bird", "diet": "carnivore", "enclosure": "aviary", "sound": "screech"},
    "Vulture": {"class": "bird", "diet": "carnivore", "enclosure": "aviary", "sound": "hiss"},
    "Macaw": {"class": "bird", "diet": "herbivore", "enclosure": "tropical aviary", "sound": "squawk"},
    "Cockatoo": {"class": "bird", "diet": "herbivore", "enclosure": "tropical aviary", "sound": "screech"},
    "Toucan": {"class": "bird", "diet": "herbivore", "enclosure": "tropical aviary", "sound": "croak"},
    "Flamingo": {"class": "bird", "diet": "omnivore", "enclosure": "waterfowl aviary", "sound": "honk"},
    "Pelican": {"class": "bird", "diet": "carnivore", "enclosure": "waterfowl aviary", "sound": "squawk"},
    "Duck": {"class": "bird", "diet": "omnivore", "enclosure": "waterfowl aviary", "sound": "quack"},
    "Swan": {"class": "bird", "diet": "herbivore", "enclosure": "waterfowl aviary", "sound": "honk"},
    "Penguin": {"class": "bird", "diet": "carnivore", "enclosure": "waterfowl aviary", "sound": "honk"},
    "Peacock": {"class": "bird", "diet": "herbivore", "enclosure": "aviary", "sound": "call"},
    "Crane": {"class": "bird", "diet": "omnivore", "enclosure": "waterfowl aviary", "sound": "trumpet"},
    "Stork": {"class": "bird", "diet": "carnivore", "enclosure": "waterfowl aviary", "sound": "clatter"},
    "Canary": {"class": "bird", "diet": "herbivore", "enclosure": "aviary", "sound": "tweet"},
    "Finch": {"class": "bird", "diet": "herbivore", "enclosure": "aviary", "sound": "chirp"}
}

BIRD_ENCLOSURES = list(set(info["enclosure"] for info in BIRD_DATA.values()))

ENCLOSURES = list(MAMMAL_ENCLOSURES+REPTILE_ENCLOSURES+BIRD_ENCLOSURES)
