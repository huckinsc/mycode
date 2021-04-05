#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        print("Houses:")
        houses = got_dj['allegiances']
        print_houses(houses)
        print("Books:")
        books = got_dj['books']
        pov_books = got_dj['povBooks']
        print_books(books,pov_books)

def print_houses(houses):
    if len(houses) == 0:
        print("This chartacer did not belong to any house.")
    else:
        for house in houses:
            got_house =  requests.get(house)
            house_dj = got_house.json();
            print("\t",house_dj['name'])


def print_books(books,pov_books):
    if len(books) == 0 and len(pov_books) == 0:
        print("This character did not apper in any books.")


if __name__ == "__main__":
        main()

