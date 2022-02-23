import random


def surnames_generator():
    random.seed(version=2)
    f = open("names.txt")
    list_names = f.readlines()
    random_name = list_names[random.randint(0, len(list_names))]
    random_surname = list_names[random.randint(0, len(list_names))]
    return random_name[:len(random_name) - 1] + " " +\
          random_surname[:len(random_surname) - 1] + "ович"


print(surnames_generator())