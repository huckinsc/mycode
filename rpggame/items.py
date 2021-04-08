def use_key_room(inv,room): 
    return "This item cannot be used from here."   

def use_key_inv(inv,room):
    return "There is no lock to use the key on." 


items_list = {
            'key' : {
                'room_description' : 'The key is on the table.',
                'inventory_description' : 'The key is gold in color',
                'room_function' : use_key_room,
                'inventory_function' : use_key_inv
                }
            }
