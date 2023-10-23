from items import *

class Room():
    def __init__(self, name, description, exits, items, enemies):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items
        self.enemies = enemies
    
    def print_all_exits_name(self):
        directions = ["north", "east", "south", "west"]
        for direction in directions:
            if self.exits[direction] is not None:
                print("GO " + direction.upper() + " to " + self.exits[direction] + ".")


    def print_room(self):
        """This function takes a room as an input and nicely displays its name,
        description and items within it."""
        
        print("\n" + self.name.upper())
        print("\n" + self.description + "\n")
        self.print_room_items()


    def print_room_items(self):
        """This function takes a room as an input and nicely displays a list of items
        found in this room (followed by a blank line). If there are no items in
        the room, nothing is printed."""
        
        if len(self.items) > 0:
            print("There is", self.list_of_items(), "here. \n")

    
    def is_valid_exit(self, direction):
        return direction in self.exits


    def list_of_items(self):
        """This methods takes all the items in the players 
        inventory and places them in a formatted list"""

        item_string = ""
        for item in self.items:
            item_string += (item.name + ", ")
        item_string = item_string[:-2]
        return item_string


    def exit_leads_to(self, direction):
        """This function takes a dictionary of exits and a direction (a particular
        exit taken from this dictionary). It returns the name of the room into which
        this exit leads."""
        
        return rooms[self.exits[direction]].name

"""Add all the room classes in the format of:"""

# room_name_here = Room(room_name, room_description, room_exit_dictionary*, room_items_dictionary**, room_enemies_list)

"""*formatted like:"""

#{"direction": "room_name_here", "direction": "room_name_here"}

"""**formatted like:"""
#{"item_name": item_}


Lecture_room = ()

Computer_lab = () 

Seminar_room = ()

The_Great_hall = ()

The_Taff = ()

The_Lounge = ()

Love_Cardiff_shop = ()

Ferris_wheel = ()

Cardiff_docks = ()

Roald_Dahl_plass = ()

The_Senedd = ()

Millennium_centre = ()

Welsh_parliament = ()

Queens_arcade = ()

Cardiff_museum = ()

NQ64 = ()

The_Earnest_willows = ()

The_Prince_of_Wales = ()

Principality_stadium = ()

Cardiff_castle = ()


rooms = {
    "Lecture_room":Lecture_room,
    "Computer_lab":Computer_lab,
    "Seminar_room":Seminar_room,
    "The_Great_hall":The_Great_hall,
    "The_Taff":The_Taff,
    "The_Lounge":The_Lounge,
    "Love_Cardiff_shop":Love_Cardiff_shop,
    "Ferris_wheel":Ferris_wheel,
    "Cardiff_docks":Cardiff_docks,
    "Roald_Dahl_plass":Roald_Dahl_plass,
    "The_Senedd":The_Senedd,
    "Millennium_centre":Millennium_centre,
    "Welsh_parliament":Welsh_parliament,
    "Queens_arcade":Queens_arcade,
    "Cardiff_museum":Cardiff_museum,
    "NQ64":NQ64,
    "The_Earnest_willows":The_Earnest_willows,
    "The_Prince_of_Wales":The_Prince_of_Wales,
    "Principality_stadium":Principality_stadium,
    "Cardiff_castle":Cardiff_castle
}


#Oli