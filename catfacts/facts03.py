#!/usr/bin/env python3

import requests
import random

def main():
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    for catfact in r.json():
        print(catfact.get("text"))

    print("\nlab 38 challange 1\n")
    print(r.status_code)

    print("\nlab 38 challange 2\n")
    print(random.choice(r.json()).get("text"))

main()
