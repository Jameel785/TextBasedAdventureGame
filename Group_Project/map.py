from items import *

class Room():
    def __init__(self, name, description, exits, enemies=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.enemies = enemies
    
    def print_all_exits_name(self):
        directions = ["north", "east", "south", "west"]
        for direction in directions:
            if self.exits[direction] is not None:
                print("GO " + direction.upper() + " to " + self.exits[direction] + ".")


    def list_of_enemies(self):
        """This methods takes all the items in the players 
        inventory and places them in a formatted list"""

        enemies_string = ""
        for enemies in self.enemies:
            enemies_string += (enemies.items + ", ")
        enemies_string = enemies_string[:-2]
        return enemies_string
    

    def print_room(self):
        """This function takes a Room as an input and nicely displays its name,
        description and items within it."""
        
        print("\n" + self.name.upper())
        print("\n" + self.description + "\n")
        self.print_enemies()


    def print_enemies(self):
        """This function takes a Room as an input and nicely displays a list of items
        found in this Room (followed by a blank line). If there are no items in
        the Room, nothing is printed."""
        
        if len(self.enemies) > 0:
            print("There is", self.list_of_items(), "here. \n")

    
    def is_valid_exit(self, direction):
        return direction in self.exits


    def exit_leads_to(self, direction):
        """This function takes a dictionary of exits and a direction (a particular
        exit taken from this dictionary). It returns the name of the Room into which
        this exit leads."""
        
        return rooms[self.exits[direction]].name
    

#1
Lecture_Room = Room(
    "Lecture Room",

    """You are in the lecture Room for computer science.
    The odour of sweaty armpits and stale deodorant is rampant.
    Alongside is empty bottles of energy drinks on the floor.
    There are rows of seats lined across the hall with a large whiteboard stacked at the end of the lecture hall.""",

    {"north":"Computer Lab", "east":"Seminar Room", "south":"The Great Hall"}
)

#2
Computer_lab = Room(
    "Computer Lab", 
    
    """You are now in the computer suite.
    There are rows upon rows of personal computers hooked up to cheap monitors on the desks.
    On the desks are empty plug sockets and turned off switches.
    The keyboards are full of breadcrumbs and surrounded by empty crisp packets.""", 
    
    {"south":"Lecture Room"}, 
)

#3
Seminar_Room = Room(
    "Seminar Room",
    
    """You are now in the seminar Room.
    There are desks upon desks littered across the Room.
    On top of the desks are piles of scribbled paper sheets and empty pencil cases.""",
    
    {"west":"Lecture Room"}

    
)

#4
The_Great_hall = Room(
    "The Great Hall",

    """You are now in the great hall of the student union.
    Surrounding you is vast plains of empty space, with left over cardboard cutouts from the previous freshers fair.
    With a capacity of over 1,600 people, there is no shortage of empty space here.""",

    {"north":"Lecture Room", "east":"Seminar Room", "south":"The Taff", "west":"The Lounge"}
)

#5
The_Taff = Room(
    "The Taff",

    """You are now in the taff.
    The taff is the local pub built into the student union.
    The stench of cheap beer and stale lager is rampant.
    The floor is littered with empty beer bottles and tissues.""",

    {"north":"The Great Hall", "east":"Love Cardiff Shop"}
)

#6
The_Lounge = Room(
    "The Lounge",

    """You are now in the lounge.
    Around you are study spaces where students could sit and chat.
    There are also play areas filled with table tennis tables and pool tables.""",

    {"north":"Lecture Room","east":"The Great Hall"}
)

#7
Love_Cardiff_shop = Room(
    "Love Cardiff Shop",

    """You are now in the Love Cardiff Shop.
    Inside the store are rows upon rows of stacked clothing.
    T-shirts and crew neck jumpers marked at half price.
    There are receipt papers and coat hangers littered across the floor.
    """,

    {"east":"Ferris Wheel"}
)

#8
Ferris_wheel = Room(
    "Ferris Wheel",

    """You are now at the giant Ferris wheel in the Cardiff Bay.
    The Cardiff bay has endless seagulls and birds scattered across its coats.
    The sea is deep blue and its sand is bright white.
    The Ferris wheel itself stand large and tall.
    It is easily the largest structure in Cardiff bay.""",

    {"north":"Queens Arcade", "south":"Cardiff Docks", "west":"Millenium Centre"}
)

#9
Cardiff_docks = Room(
    "Cardiff Docks",

    """You are now at the Cardiff bay and docks.
    There are boats surrounding the entire area.
    Seagulls are squeaking as they are flying through the air and the sky has a bright blue hue to it.""",

    {"north":"Ferris Wheel", "south":"Roald Dahl Plass"}
)

#10
Roald_Dahl_plass = Room(
    "Roald Dahl Plass",

    """You are now at the roald dahl plass.
    This is a plaza with plenty of places to eat and drink and it is surrounded by illuminated pillars.
    The smell of burnt popcorn and cotton candy has filled the air and there is magical atmosphere which fills your mood.""",

    {"north":"Cardiff Docks", "east":"Seminar Room", "west":"The Senedd Room 1"}
)

#11
Millenium_centre = Room(
    "Millenium Centre",

    """Description goes here""",

    {"east":"Ferris Wheel", "south":"Cardiff Docks"}
)

#12
The_Senedd_1 = Room(
    "The Senedd Room 1",
    
    """Description goes here""",

    {"north":"The Senedd Room 2"}
)

#13
The_Senedd_2 = Room(
    "The Senedd Room 2",
    
    """Description goes here""",

    {"east":"Millenium Centre"}
)

#14
Cardiff_museum = Room(
    "Queens Arcade",
    
    """Description goes here""",

    {"north":"Cardiff Museum"}
)

#15
Queens_arcade = Room(
    "Cardiff Museum",
    
    """Description goes here""",

    {"north":"Cardiff Castle", "east":"Principality Stadium", "west":"NQ64"}
)

#16
NQ64 = Room(
    "NQ64",
    
    """Description goes here""",

    {"north":"The Earnest Willows", "east":"Cardiff Museum"}
)

#17
The_Earnest_willows = Room(
    "The Earnest Willows",
    
    """Description goes here""",

    {"north":"The Prince of Wales"}
)

#18
The_Prince_of_Wales = Room(
    "The Prince of Wales",
    
    """Description goes here""",

    {"south":"NQ64"}
)

#19
Principality_stadium = Room(
    "Principality Stadium",
    
    """Description goes here""",

    {"west":"Cardiff Museum"}
)

#20
Cardiff_castle = Room(
    "Cardiff Castle",
    
    """Description goes here""",

    {"north":"END"}
)

rooms = {
    "Lecture Room":Lecture_Room,
    "Computer lab":Computer_lab,
    "Seminar Room":Seminar_Room,
    "The Great hall":The_Great_hall,
    "The Taff":The_Taff,
    "The Lounge":The_Lounge,
    "Love Cardiff shop":Love_Cardiff_shop,
    "Ferris wheel":Ferris_wheel,
    "Cardiff docks":Cardiff_docks,
    "Roald Dahl plass":Roald_Dahl_plass,
    "The Senedd Room 1":The_Senedd_1,
    "Millennium centre":Millenium_centre,
    "The Senedd Room 2":The_Senedd_2,
    "Queens arcade":Queens_arcade,
    "Cardiff museum":Cardiff_museum,
    "NQ64":NQ64,
    "The Earnest willows":The_Earnest_willows,
    "The Prince of Wales":The_Prince_of_Wales,
    "Principality stadium":Principality_stadium,
    "Cardiff castle":Cardiff_castle
}


