## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'description' : 'HAll\nNot much to say here.\nThere is a locked door to the north.\nYou hear sounds from the south.\nThere is a door to the east.',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Bathroom', 
                },

            'Kitchen' : {
                  'description' : 'This is the kitchen',
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'description' : 'Dining Room\nA large table with several dirty plates of rotting food\nsits in the middleof the room.\nThere are doors to the west and south.',
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'key'
               },
            'Garden' : {
                  'description' : 'Garden\nThere are potted plants scattered around.',
                  'north' : 'Dining Room',
                  'item'  : 'potion'
            },
            'Bathroom' : {
                  'description' : 'Bathroom\nThere is a bathtub full of ice.\nYou notice that there is a fresh insision\nwhere your left kindney used to be\nThere is a door to the east',
                  'east'  : 'Hall' 
                }
         }
