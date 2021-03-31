#!/usr/bin/env python3

FARMS = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

ANIMALS = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

def f1():
    for farm in FARMS:
        if farm["name"] == "NE Farm":
            for animal in farm["agriculture"]:
                print(animal)

def f2():
    user_input = input("What farm would you like to know about?")
    found = False
    for farm in FARMS:
        if farm["name"].lower() == user_input.lower():
            found = True
            for animal in farm["agriculture"]:
                print(animal)
    if not found:
        print("We don't have info for that farm.")


def f3():
    user_input = input("What farm would you like to know about?")
    found = False
    for farm in FARMS:
        if farm["name"].lower() == user_input.lower():
            found = True
            for animal in farm["agriculture"]:
                if animal in ANIMALS:
                    print(animal)
    if not found:
        print("We don't have info for that farm.")

f3()
