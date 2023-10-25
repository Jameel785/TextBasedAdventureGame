from game import scrolling_text
import time

class Room():
    def __init__(self, name, description, exits, enemies, items):
        self.name = name
        self.description = description
        self.exits = exits
        self.enemies = enemies
        self.items = items
    
    def print_all_exits_name(self):
        directions = ["north", "east", "south", "west"]
        for direction in directions:
            try:
                if self.exits[direction] is not None:
                    print("GO " + direction.upper() + " to " + self.exits[direction] + ".")
                    time.sleep(0.5)
            except KeyError:
                pass

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

        print("press 's' to skip the scrolling text!\n")
        scrolling_text(self.name.upper())
        print("")
        scrolling_text(self.description + "\n ")
        print("")
        self.print_enemies()


    def list_of_items(self):
        """This methods takes all the items in the rooms 
        inventory and places them in a formatted list"""

        item_string = ""
        for item in self.inventory:
            item_string += (item.name + ", ")
        item_string = item_string[:-2]
        return item_string
    
    
    def list_of_enemies(self):
        """This methods takes all the enemies in the room 
            and places them in a formatted list"""

        enemy_string = ""
        for enemy in self.enemies:
            enemy_string += (" a " + enemy.name + ", ")
        enemy_string = enemy_string[:-2]
        return enemy_string


    def print_enemies(self):
        """This function takes a room as an input and nicely displays a list of items
        found in this Room (followed by a blank line). If there are no items in
        the Room, nothing is printed."""
        
        if len(self.enemies) > 0:
            text = "There is", self.list_of_enemies(), " here. \n"
            print("press 's' to skip the scrolling text!")
            scrolling_text(text)

    
    def is_valid_exit(self, direction):
        """returns the value of the key in the directions of the room"""
        
        return direction in self.exits

    



