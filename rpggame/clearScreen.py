#!/usr/bin/env python3

from os import system,name

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


if __name__ == "__main__":
    print("Hello World")
    clear()
