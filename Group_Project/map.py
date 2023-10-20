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
    

    def print_room_items(self):
        if len(self.items) > 0:
            print("There is", self.list_of_items(), "here. \n")


    def exit_leads_to(self, direction):
        return rooms[self.exits[direction]].name

"""Add all the room classes in the format of:"""

# room_name_here = Room(room_name, room_description, room_exit_dictionary*, room_items_dictionary**, room_enemies_list)

"""*formatted like:"""

#{"direction": "room_name_here", "direction": "room_name_here"}

"""*formatted like:"""
#{"item_name": item_}



rooms = {

    """Add all the rooms in here in the format of:"""

    #"room_name": room_name_here
    
    """for all the rooms"""

}


#Zohaib