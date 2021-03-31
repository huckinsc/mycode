#!/usr/bin/env python3

import requests

def main():
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    print( dir(r) )

main()
