## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'description' : 'This is the hall',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'description' : 'This is the kitchen',
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'description' : 'This is the dinning room',
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
               },
            'Garden' : {
                  'description' : 'This is the garden',
                  'north' : 'Dining Room'
            }
         }
