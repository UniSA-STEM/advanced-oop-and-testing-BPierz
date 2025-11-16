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
mammal_data = {
    "Lion": {"diet": ["meat", "organs", "bones"], "enclosure": "Savannah", "sound": "roar", "max_age": 25},
    "Black Bear": {"diet": ["fish", "berries", "insects", "meat", "plants"], "enclosure": "Forest", "sound": "growl", "max_age": 30},
    "Brown Bear": {"diet": ["fish", "berries", "roots", "insects", "meat"], "enclosure": "Forest", "sound": "growl", "max_age": 35},
    "Polar Bear": {"diet": ["fish", "seal meat", "whale blubber"], "enclosure": "Arctic", "sound": "huff", "max_age": 30},
    "Grizzly Bear": {"diet": ["fish", "berries", "insects", "meat"], "enclosure": "Forest", "sound": "roar", "max_age": 30},
    "Giraffe": {"diet": ["acacia leaves", "twigs", "fruits"], "enclosure": "Savannah", "sound": "hum", "max_age": 28},
    "Zebra": {"diet": ["grass", "hay"], "enclosure": "Savannah", "sound": "whinny", "max_age": 25},
    "Puma": {"diet": ["meat", "organs"], "enclosure": "Mountain", "sound": "growl", "max_age": 20},
    "Meerkat": {"diet": ["insects", "small reptiles", "eggs"], "enclosure": "Desert", "sound": "chirp", "max_age": 12},
    "Hippopotamus": {"diet": ["grass", "water plants"], "enclosure": "Wetlands", "sound": "grunt", "max_age": 50},
    "Rhinoceros": {"diet": ["grass", "leaves", "shoots"], "enclosure": "Savannah", "sound": "snort", "max_age": 50},
    "Cheetah": {"diet": ["meat", "organs"], "enclosure": "Savannah", "sound": "chirp", "max_age": 17},
    "Leopard": {"diet": ["meat", "organs"], "enclosure": "Forest", "sound": "growl", "max_age": 23},
    "Tiger": {"diet": ["meat", "organs"], "enclosure": "Rainforest", "sound": "roar", "max_age": 26},
    "Gorilla": {"diet": ["fruit", "leaves", "shoots"], "enclosure": "Rainforest", "sound": "hoot", "max_age": 55},
    "Chimpanzee": {"diet": ["fruit", "insects", "leaves", "nuts"], "enclosure": "Rainforest", "sound": "screech", "max_age": 55},
    "Orangutan": {"diet": ["fruit", "leaves", "bark"], "enclosure": "Rainforest", "sound": "long call", "max_age": 55},
    "Kangaroo": {"diet": ["grass", "shoots"], "enclosure": "Grassland", "sound": "thump", "max_age": 20},
    "Koala": {"diet": ["eucalyptus leaves"], "enclosure": "Eucalyptus Forest", "sound": "bellow", "max_age": 18},
    "Red Panda": {"diet": ["bamboo", "fruit", "insects"], "enclosure": "Mountain Forest", "sound": "chirp", "max_age": 15},
    "Wolf": {"diet": ["meat", "organs", "bones"], "enclosure": "Forest", "sound": "howl", "max_age": 16},
    "Hyena": {"diet": ["meat", "bones", "carrion"], "enclosure": "Savannah", "sound": "cackle", "max_age": 25},
    "Bison": {"diet": ["grass", "hay"], "enclosure": "Grassland", "sound": "bellow", "max_age": 25},
    "Camel": {"diet": ["grass", "dry shrubs"], "enclosure": "Desert", "sound": "grunt", "max_age": 40},
    "Llama": {"diet": ["grass", "hay"], "enclosure": "Mountain", "sound": "hum", "max_age": 25},
    "Capybara": {"diet": ["grass", "water plants"], "enclosure": "Wetlands", "sound": "whistle", "max_age": 12},
    "Otter": {"diet": ["fish", "crustaceans"], "enclosure": "Riverbank", "sound": "chirp", "max_age": 20},
    "Seal": {"diet": ["fish", "squid"], "enclosure": "Arctic Pool", "sound": "bark", "max_age": 35},
    "Sea Lion": {"diet": ["fish", "squid"], "enclosure": "Coastal Pool", "sound": "bark", "max_age": 30},
    "Dolphin": {"diet": ["fish", "squid"], "enclosure": "Aquarium", "sound": "click", "max_age": 50}
}

mammal_enclosures = list(set(info["enclosure"] for info in mammal_data.values()))

reptile_data = {
    "Cobra": {"diet": ["mice", "rats", "frogs", "small birds"], "enclosure": "tropical terrarium", "sound": "hiss", "max_age": 20},
    "King Cobra": {"diet": ["snakes", "lizards", "small mammals"], "enclosure": "tropical terrarium", "sound": "hiss", "max_age": 25},
    "Python": {"diet": ["rats", "rabbits", "birds"], "enclosure": "tropical terrarium", "sound": "hiss", "max_age": 30},
    "Boa Constrictor": {"diet": ["rats", "rabbits", "birds"], "enclosure": "tropical terrarium", "sound": "hiss", "max_age": 30},
    "Anaconda": {"diet": ["fish", "birds", "small mammals"], "enclosure": "aquatic reptile", "sound": "hiss", "max_age": 30},
    "Komodo Dragon": {"diet": ["meat", "carrion", "eggs"], "enclosure": "tropical terrarium", "sound": "growl", "max_age": 30},
    "Monitor Lizard": {"diet": ["insects", "meat", "eggs"], "enclosure": "tropical terrarium", "sound": "hiss", "max_age": 20},
    "Bearded Dragon": {"diet": ["insects", "greens", "vegetables"], "enclosure": "desert terrarium", "sound": "chirp", "max_age": 15},
    "Iguana": {"diet": ["leafy greens", "fruit", "flowers"], "enclosure": "tropical terrarium", "sound": "rustle", "max_age": 20},
    "Chameleon": {"diet": ["insects", "worms"], "enclosure": "tropical terrarium", "sound": "click", "max_age": 7},
    "Gecko": {"diet": ["insects", "worms"], "enclosure": "desert terrarium", "sound": "chirp", "max_age": 15},
    "Horned Viper": {"diet": ["mice", "lizards", "small birds"], "enclosure": "desert terrarium", "sound": "hiss", "max_age": 15},
    "Desert Tortoise": {"diet": ["grass", "leafy greens", "flowers"], "enclosure": "desert terrarium", "sound": "rustle", "max_age": 60},
    "Giant Tortoise": {"diet": ["leaves", "fruit", "vegetables"], "enclosure": "tropical terrarium", "sound": "grunt", "max_age": 120},
    "Crocodile": {"diet": ["fish", "meat", "birds"], "enclosure": "aquatic reptile", "sound": "bellow", "max_age": 70},
    "Alligator": {"diet": ["fish", "small mammals", "birds"], "enclosure": "aquatic reptile", "sound": "bellow", "max_age": 60},
    "Sea Turtle": {"diet": ["sea grass", "algae"], "enclosure": "aquatic reptile", "sound": "splash", "max_age": 80}
}

reptile_enclosures = list(set(info["enclosure"] for info in reptile_data.values()))

bird_data = {
    "Eagle": {"diet": ["fish", "rodents", "small birds"], "enclosure": "aviary", "sound": "screech", "max_age": 30},
    "Hawk": {"diet": ["rodents", "small birds", "insects"], "enclosure": "aviary", "sound": "kree", "max_age": 25},
    "Owl": {"diet": ["rodents", "insects", "small birds"], "enclosure": "aviary", "sound": "hoot", "max_age": 25},
    "Falcon": {"diet": ["small birds", "insects", "rodents"], "enclosure": "aviary", "sound": "kek-kek", "max_age": 25},
    "Vulture": {"diet": ["carrion", "meat"], "enclosure": "aviary", "sound": "hiss", "max_age": 40},
    "Macaw": {"diet": ["nuts", "fruit", "seeds"], "enclosure": "tropical aviary", "sound": "squawk", "max_age": 60},
    "Cockatoo": {"diet": ["seeds", "fruit", "nuts"], "enclosure": "tropical aviary", "sound": "screech", "max_age": 60},
    "Toucan": {"diet": ["fruit", "insects"], "enclosure": "tropical aviary", "sound": "croak", "max_age": 20},
    "Flamingo": {"diet": ["shrimp", "algae", "insects"], "enclosure": "waterfowl aviary", "sound": "honk", "max_age": 40},
    "Pelican": {"diet": ["fish"], "enclosure": "waterfowl aviary", "sound": "grunt", "max_age": 30},
    "Duck": {"diet": ["insects", "water plants", "seeds"], "enclosure": "waterfowl aviary", "sound": "quack", "max_age": 15},
    "Swan": {"diet": ["water plants", "grass"], "enclosure": "waterfowl aviary", "sound": "honk", "max_age": 30},
    "Penguin": {"diet": ["fish", "krill"], "enclosure": "waterfowl aviary", "sound": "bray", "max_age": 25},
    "Peacock": {"diet": ["seeds", "insects"], "enclosure": "aviary", "sound": "mee-ow", "max_age": 20},
    "Cane": {"diet": ["insects", "small fish", "plants"], "enclosure": "waterfowl aviary", "sound": "trumpet", "max_age": 30},
    "Stork": {"diet": ["fish", "insects", "amphibians"], "enclosure": "waterfowl aviary", "sound": "clatter", "max_age": 30},
    "Canary": {"diet": ["seeds", "fruit"], "enclosure": "aviary", "sound": "tweet", "max_age": 10},
    "Finch": {"diet": ["seeds", "small insects"], "enclosure": "aviary", "sound": "cheep", "max_age": 10}
}

bird_enclosures = list(set(info["enclosure"] for info in bird_data.values()))
all_enclosures = list(mammal_enclosures+reptile_enclosures+bird_enclosures)

animal_data = [mammal_data, bird_data, reptile_data]

all_food_items = set()
for groups in animal_data:
    for info in groups.values():
        for food in info["diet"]:
            all_food_items.add(food)

animals = []
for groups in animal_data:
    for species in groups.keys():
        animals.append(species)


