#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    while True:
        user_input = input("What Pokemon would you like to know about:")
        pokeapiurl = "https://pokeapi.co/api/v2/pokemon/" + user_input.lower()
        pokeapi = requests.get(pokeapiurl)
        #print(pokeapi.status_code)
        if pokeapi.status_code == 200:
            pokeapijson = pokeapi.json()
            #print(pokeapi)
            print("ID:", pokeapijson["id"],"Name:",pokeapijson["name"])
        else:
            print("Not a valid a Pokemon.")

main()
