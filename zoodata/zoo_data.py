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
    "Lion": {"class": "mammal", "diet": ["meat", "organs", "bones"], "enclosure": "Savannah", "sound": "roar"},
    "Black Bear": {"class": "mammal", "diet": ["fish", "berries", "insects", "meat", "plants"], "enclosure": "Forest", "sound": "growl"},
    "Brown Bear": {"class": "mammal", "diet": ["fish", "berries", "roots", "insects", "meat"], "enclosure": "Forest", "sound": "growl"},
    "Polar Bear": {"class": "mammal", "diet": ["fish", "seal meat", "whale blubber"], "enclosure": "Arctic", "sound": "huff"},
    "Grizzly Bear": {"class": "mammal", "diet": ["fish", "berries", "insects", "meat"], "enclosure": "Forest", "sound": "roar"},
    "Giraffe": {"class": "mammal", "diet": ["acacia leaves", "twigs", "fruits"], "enclosure": "Savannah", "sound": "hum"},
    "Zebra": {"class": "mammal", "diet": ["grass", "hay"], "enclosure": "Savannah", "sound": "whinny"},
    "Puma": {"class": "mammal", "diet": ["meat", "organs"], "enclosure": "Mountain", "sound": "growl"},
    "Meerkat": {"class": "mammal", "diet": ["insects", "small reptiles", "eggs"], "enclosure": "Desert", "sound": "chirp"},
    "Hippopotamus": {"class": "mammal", "diet": ["grass", "water plants"], "enclosure": "Wetlands", "sound": "grunt"},
    "Rhinoceros": {"class": "mammal", "diet": ["grass", "leaves", "shoots"], "enclosure": "Savannah", "sound": "snort"},
    "Cheetah": {"class": "mammal", "diet": ["meat", "organs"], "enclosure": "Savannah", "sound": "chirp"},
    "Leopard": {"class": "mammal", "diet": ["meat", "organs"], "enclosure": "Forest", "sound": "growl"},
    "Tiger": {"class": "mammal", "diet": ["meat", "organs"], "enclosure": "Rainforest", "sound": "roar"},
    "Gorilla": {"class": "mammal", "diet": ["fruit", "leaves", "shoots"], "enclosure": "Rainforest", "sound": "hoot"},
    "Chimpanzee": {"class": "mammal", "diet": ["fruit", "insects", "leaves", "nuts"], "enclosure": "Rainforest", "sound": "screech"},
    "Orangutan": {"class": "mammal", "diet": ["fruit", "leaves", "bark"], "enclosure": "Rainforest", "sound": "long call"},
    "Kangaroo": {"class": "mammal", "diet": ["grass", "shoots"], "enclosure": "Grassland", "sound": "thump"},
    "Koala": {"class": "mammal", "diet": ["eucalyptus leaves"], "enclosure": "Eucalyptus Forest", "sound": "bellow"},
    "Red Panda": {"class": "mammal", "diet": ["bamboo", "fruit", "insects"], "enclosure": "Mountain Forest", "sound": "chirp"},
    "Wolf": {"class": "mammal", "diet": ["meat", "organs", "bones"], "enclosure": "Forest", "sound": "howl"},
    "Hyena": {"class": "mammal", "diet": ["meat", "bones", "carrion"], "enclosure": "Savannah", "sound": "cackle"},
    "Bison": {"class": "mammal", "diet": ["grass", "hay"], "enclosure": "Grassland", "sound": "bellow"},
    "Camel": {"class": "mammal", "diet": ["grass", "dry shrubs"], "enclosure": "Desert", "sound": "grunt"},
    "Llama": {"class": "mammal", "diet": ["grass", "hay"], "enclosure": "Mountain", "sound": "hum"},
    "Capybara": {"class": "mammal", "diet": ["grass", "water plants"], "enclosure": "Wetlands", "sound": "whistle"},
    "Otter": {"class": "mammal", "diet": ["fish", "crustaceans"], "enclosure": "Riverbank", "sound": "chirp"},
    "Seal": {"class": "mammal", "diet": ["fish", "squid"], "enclosure": "Arctic Pool", "sound": "bark"},
    "Sea Lion": {"class": "mammal", "diet": ["fish", "squid"], "enclosure": "Coastal Pool", "sound": "bark"},
    "Dolphin": {"class": "mammal", "diet": ["fish", "squid"], "enclosure": "Aquarium", "sound": "click"}
}

mammal_enclosures = list(set(info["enclosure"] for info in mammal_data.values()))

reptile_data = {
    "Cobra": {"class": "reptile", "diet": ["mice", "rats", "frogs", "small birds"], "enclosure": "tropical terrarium", "sound": "hiss"},
    "King Cobra": {"class": "reptile", "diet": ["snakes", "lizards", "small mammals"], "enclosure": "tropical terrarium", "sound": "hiss"},
    "Python": {"class": "reptile", "diet": ["rats", "rabbits", "birds"], "enclosure": "tropical terrarium", "sound": "hiss"},
    "Boa Constrictor": {"class": "reptile", "diet": ["rats", "rabbits", "birds"], "enclosure": "tropical terrarium", "sound": "hiss"},
    "Anaconda": {"class": "reptile", "diet": ["fish", "birds", "small mammals"], "enclosure": "aquatic reptile", "sound": "hiss"},
    "Komodo Dragon": {"class": "reptile", "diet": ["meat", "carrion", "eggs"], "enclosure": "tropical terrarium", "sound": "growl"},
    "Monitor Lizard": {"class": "reptile", "diet": ["insects", "meat", "eggs"], "enclosure": "tropical terrarium", "sound": "hiss"},
    "Bearded Dragon": {"class": "reptile", "diet": ["insects", "greens", "vegetables"], "enclosure": "desert terrarium", "sound": "chirp"},
    "Iguana": {"class": "reptile", "diet": ["leafy greens", "fruit", "flowers"], "enclosure": "tropical terrarium", "sound": "rustle"},
    "Chameleon": {"class": "reptile", "diet": ["insects", "worms"], "enclosure": "tropical terrarium", "sound": "click"},
    "Gecko": {"class": "reptile", "diet": ["insects", "worms"], "enclosure": "desert terrarium", "sound": "chirp"},
    "Horned Viper": {"class": "reptile", "diet": ["mice", "lizards", "small birds"], "enclosure": "desert terrarium", "sound": "hiss"},
    "Desert Tortoise": {"class": "reptile", "diet": ["grass", "leafy greens", "flowers"], "enclosure": "desert terrarium", "sound": "rustle"},
    "Giant Tortoise": {"class": "reptile", "diet": ["leaves", "fruit", "vegetables"], "enclosure": "tropical terrarium", "sound": "grunt"},
    "Crocodile": {"class": "reptile", "diet": ["fish", "meat", "birds"], "enclosure": "aquatic reptile", "sound": "bellow"},
    "Alligator": {"class": "reptile", "diet": ["fish", "small mammals", "birds"], "enclosure": "aquatic reptile", "sound": "bellow"},
    "Sea Turtle": {"class": "reptile", "diet": ["sea grass", "algae"], "enclosure": "aquatic reptile", "sound": "splash"}
}


reptile_enclosures = list(set(info["enclosure"] for info in reptile_data.values()))


bird_data = {
    "Eagle": {"class": "bird", "diet": ["fish", "rodents", "small birds"], "enclosure": "aviary", "sound": "screech"},
    "Hawk": {"class": "bird", "diet": ["rodents", "small birds", "insects"], "enclosure": "aviary", "sound": "kree"},
    "Owl": {"class": "bird", "diet": ["rodents", "insects", "small birds"], "enclosure": "aviary", "sound": "hoot"},
    "Falcon": {"class": "bird", "diet": ["small birds", "insects", "rodents"], "enclosure": "aviary", "sound": "kek-kek"},
    "Vulture": {"class": "bird", "diet": ["carrion", "meat"], "enclosure": "aviary", "sound": "hiss"},
    "Macaw": {"class": "bird", "diet": ["nuts", "fruit", "seeds"], "enclosure": "tropical aviary", "sound": "squawk"},
    "Cockatoo": {"class": "bird", "diet": ["seeds", "fruit", "nuts"], "enclosure": "tropical aviary", "sound": "screech"},
    "Toucan": {"class": "bird", "diet": ["fruit", "insects"], "enclosure": "tropical aviary", "sound": "croak"},
    "Flamingo": {"class": "bird", "diet": ["shrimp", "algae", "insects"], "enclosure": "waterfowl aviary", "sound": "honk"},
    "Pelican": {"class": "bird", "diet": ["fish"], "enclosure": "waterfowl aviary", "sound": "grunt"},
    "Duck": {"class": "bird", "diet": ["insects", "water plants", "seeds"], "enclosure": "waterfowl aviary", "sound": "quack"},
    "Swan": {"class": "bird", "diet": ["water plants", "grass"], "enclosure": "waterfowl aviary", "sound": "honk"},
    "Penguin": {"class": "bird", "diet": ["fish", "krill"], "enclosure": "waterfowl aviary", "sound": "bray"},
    "Peacock": {"class": "bird", "diet": ["seeds", "insects"], "enclosure": "aviary", "sound": "mee-ow"},
    "Crane": {"class": "bird", "diet": ["insects", "small fish", "plants"], "enclosure": "waterfowl aviary", "sound": "trumpet"},
    "Stork": {"class": "bird", "diet": ["fish", "insects", "amphibians"], "enclosure": "waterfowl aviary", "sound": "clatter"},
    "Canary": {"class": "bird", "diet": ["seeds", "fruit"], "enclosure": "aviary", "sound": "tweet"},
    "Finch": {"class": "bird", "diet": ["seeds", "small insects"], "enclosure": "aviary", "sound": "cheep"}
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


