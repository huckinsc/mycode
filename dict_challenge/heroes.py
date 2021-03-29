#!/usr/bin/env python3

heroes = {
        "wolverine":{
            "real name":"James Howlett",
            "powers":"regeneration",
            "archenemy":"Sabertooth"
            },
        "harry potter":{
            "real name":"Harry Potter",
            "powers":"He's a wizard",
            "archenemy":"Voldemort"
            },
        "agent fitz":{
            "real name":"Leopold Fitz",
            "powers":"intellegence",
            "archenemy":"Hydra"
            }
        }

done = False
while done == False:
    valid_data = True
    character_request = input("Who would you like to get information about?")
    character = heroes.get(character_request.lower())
    if character is not None:
        attr_request = input("What information would you like?")
        attr = character.get(attr_request.lower())
        if attr is not None:
            print(f"{character_request.title()}'s {attr_request.lower()} is: {attr}")
        else:
            print(f"{attr_request} is not a valid character attribute.")
    else:
        print(f"There is no data for {character_request}.")
    


    done_response = input("Would you like to get more information?(y/Y will continue and all other input will exit)")
    if done_response.upper()  != "Y":
        done = True
    


