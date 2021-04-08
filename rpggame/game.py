#!/usr/bin/env python3

''' RPG Game '''

from locations import rooms
from verbs import travel_verbs,get_verbs,use_verbs,look_verbs
from clearScreen import clear
from items import items_list

def showInstructions():
    ''' Display instructions '''
    print ('''
How to Play
===========
Movement: Type a move verb like "go" followed by a direction.
- go east
Collecting Items: Type a get verb like "get" followed by the item name.
- get key
Examining Items: Tytpe a look verb followed by the item name.
-  look key
Using Items: Typ:e a use verb followed by by the item name.
- use key
''')
    input("Press 'Enter' to continue")

def showStatus(msg):  
    ''' print the player's current status '''
    print('---------------------------')
    print(rooms[currentRoom]['description'])
    print(rooms[currentRoom]['description'])
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
    if msg is not None:
        print(msg)

def processTurn(inventory,display_message,currentRoom):
    ''' Process player turn '''
    move = ''
    while move == '':
        move = input('>')
    # parse player input into verb and noun
    move = move.lower().split(" ", 1)
    if move[0] in travel_verbs:
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            display_message = 'You can\'t go that way!'
    if move[0] in get_verbs:
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            display_message = move[1] + ' got!'
            del rooms[currentRoom]['item']
        else:
            display_message = 'Can\'t get ' + move[1] + '!'
    if move[0] in look_verbs:
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            display_message = items_list[move[1]]['room_description']
        elif move[1] in inventory:
            display_message = items_list[move[1]]['inventory_description']
    if move[0] in use_verbs:
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            display_message = items_list[move[1]]['room_function'](inventory,currentRoom)
        elif move[1] in inventory:
            display_message = items_list[move[1]]['inventory_function'](inventory,currentRoom)
    if move[0] == "help":
        showInstructions()

    #Determine win/loose conditions
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        return True,inventory,display_message,currentRoom
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        return True,inventory,display_message,currentRoom
    return False,inventory,display_message,currentRoom

#Player inventory
inventory = []
#Turn message
display_message = "Type 'help' to see instructions."
#Player's room. 
currentRoom = 'Hall'

game_over = False

while not game_over:
    clear()
    showStatus(display_message)
    display_message = ""
    game_over,inventory,display_message,currentRoom = processTurn(inventory,display_message,currentRoom)

