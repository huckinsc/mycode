def use_key_room(inv,room,locations): 
    return "This item cannot be used from here."   

def use_key_inv(inv,room,locations):
    if room == 'Hall':
        locations['Hall']['description'] = 'HAll\nNot much to say here.\nThe door to the north is unlocked.\nYou hear sounds from the south.\nThere is a door to the east.'
        locations['Hall']['north'] = 'Porch'
        inv.remove('key')
        return "The door to the north has been unlocked."
    else:
        return "There is no lock to use the key on." 

def use_jello_room(inv,room,locations):
    return "This is to slippery to manipulate from here."

def use_jello_inv(inv,room,locations):
    inv.remove('jello mold')
    inv.append('key')
    return "You dig your hands deep in the the slimy mess and find a key."

items_list = {
            'key' : {
                'room_description' : 'The key is on the table.',
                'inventory_description' : 'The key is gold in color',
                'room_function' : use_key_room,
                'inventory_function' : use_key_inv
                },
            'jello mold' : {
                'room_description' : 'An old slimy, molding jello mold sits in the middle of the table.',
                'inventory_description' : 'There seems to be a shiny object in the middle of the mold.',
                'room_function' : use_jello_room,
                'inventory_function' : use_jello_inv
                }
            }
