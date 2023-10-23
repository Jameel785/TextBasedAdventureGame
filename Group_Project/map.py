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

#1
Lecture_room = {
    "name":"Lecture Room",

    "description":"""You are in the lecture room for computer science.
    The odour of sweaty armpits and stale deodorant is rampant.
    Alongside is empty bottles of energy drinks on the floor.
    There are rows of seats lined across the hall with a large whiteboard stacked at the end of the lecture hall.""",

    "exits":{"north":"Computer Lab","east":"Seminar Room","south":"The Great Hall"}
}
#2
Computer_lab = {
    "name":"Computer Lab",

    "description":"""You are now in the computer suite.
    There are rows upon rows of personal computers hooked up to cheap monitors on the desks.
    On the desks are empty plug sockets and turned off switches.
    The keyboards are full of breadcrumbs and surrounded by empty crisp packets.""",

    "exits":{"south: Lecture Room"}
} 
#3
Seminar_room = {
    "name":"Seminar Room",

    "description":"""You are now in the seminar room.
    There are desks upon desks littered across the room.
    On top of the desks are piles of scribbled paper sheets and empty pencil cases.""",

    "exits":{"west":"Lecture Room"}
}
#4
The_Great_hall = {
    "name":"The Great Hall",

    "description":"""You are now in the great hall of the student union.
    Surrounding you is vast plains of empty space, with left over cardboard cutouts from the previous freshers fair.
    With a capacity of over 1,600 people, there is no shortage of empty space here.""",

    "exits":{"north":"Lecture Room","east":"Seminar Room","south":"The Taff","west":"The Lounge"}
}
#5
The_Taff = {
    "name":"The Taff",

    "description":"""You are now in the taff.
    The taff is the local pub built into the student union.
    The stench of cheap beer and stale lager is rampant.
    The floor is littered with empty beer bottles and tissues.""",

    "exits":{"north":"The Great Hall","east":"Love Cardiff Shop"}
}
#6
The_Lounge = {
    "name":"The Lounge",

    "description":"""You are now in the lounge.
    Around you are study spaces where students could sit and chat.
    There are also play areas filled with table tennis tables and pool tables.""",

    "exits":{"north":"Lecture Room","east":"The Great Hall"}
}
#7
Love_Cardiff_shop = {
    "name":"Love Cardiff Shop",

    "description":"""You are now in the Love Cardiff Shop.
    Inside the store are rows upon rows of stacked clothing.
    T-shirts and crew neck jumpers marked at half price.
    There are receipt papers and coat hangers littered across the floor.
    """,

    "exits":{"east":"Ferris Wheel"}
}
#8
Ferris_wheel = {
    "name":"Ferris Wheel",

    "description":"""You are now at the giant Ferris wheel in the Cardiff Bay.
    The Cardiff bay has endless seagulls and birds scattered across its coats.
    The sea is deep blue and its sand is bright white.
    The Ferris wheel itself stand large and tall.
    It is easily the largest structure in Cardiff bay.""",

    "exits":{"north":"Queens Arcade","south":"Cardiff Docks","west":"Millenium Centre"}
}
#9
Cardiff_docks = {
    "name":"Cardiff Docks",

    "description":"""You are now at the Cardiff bay and docks.
    There are boats surrounding the entire area.
    Seagulls are squeaking as they are flying through the air and the sky has a bright blue hue to it.""",

    "exits":{"north":"Ferris Wheel","south":"Roald Dahl Plass"}
}
#10
Roald_Dahl_plass = {
    "name":"Roald Dahl Plass",

    "description":"""You are now at the roald dahl plass.
    This is a plaza with plenty of places to eat and drink and it is surrounded by illuminated pillars.
    The smell of burnt popcorn and cotton candy has filled the air and there is magical atmosphere which fills your mood.""",

    "exits":{"north":"Cardiff Docks","east":"Seminar Room","west":"The Senedd ROOM 1"}
}
#11
Millenium_centre = {
    "name":"Millenium Centre",

    "exits":{"east":"Ferris Wheel","south":"Cardiff Docks","west":"The Senedd ROOM 1"}
}
#12
The_Senedd_1 = {
    "name":"The Senedd ROOM 1",

    "exits":{"north":"The Senedd ROOM 2","east":"Millenium Centre","south":"Roald Dahl Pass"}
}
#13
The_Senedd_2 = {
    "name":"The Senedd ROOM 2",

    "exits":{"east":"Millenium Centre","south":"The Sendd ROOM 2"}
}
#14
Queens_arcade = {
    "name":"Queens Arcade",

    "exits":{"north":"Cardiff Museum"}
}
#15
Cardiff_museum = {
    "name":"Cardiff Museum",

    "exits":{"north":"Cardiff Castle","east":"Principality Stadium","west":"NQ64"}
}
#16
NQ64 = {
    "name":"NQ64",

    "exits":{"north":"The Earnest Willows","east":"Cardiff Museum"}
}
#17
The_Earnest_willows = {
    "name":"The Earnest Willows",

    "exits":{"north":"The Prince of Wales"}
}
#18
The_Prince_of_Wales = {
    "name":"The Prince of Wales",

    "exits":{"west":"NQ64"}
}
#19
Principality_stadium = {
    "name":"Principality Stadium",

    "exits":{"west":"Cardiff Museum"}
}
#20
Cardiff_castle = {
    "name":"Cardiff Castle",

    "exits":{"north":"END"}
}

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
    "The_Senedd_ROOM_1":The_Senedd_1,
    "Millennium_centre":Millenium_centre,
    "The_Senedd_ROOM_2":The_Senedd_2,
    "Queens_arcade":Queens_arcade,
    "Cardiff_museum":Cardiff_museum,
    "NQ64":NQ64,
    "The_Earnest_willows":The_Earnest_willows,
    "The_Prince_of_Wales":The_Prince_of_Wales,
    "Principality_stadium":Principality_stadium,
    "Cardiff_castle":Cardiff_castle
}


#Oli
