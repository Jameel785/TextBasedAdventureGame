from game import scrolling_text
import time

class Room():
    def __init__(self, name, description, exits, enemies, items, dialouge):
        self.name = name
        self.description = description
        self.exits = exits
        self.enemies = enemies
        self.items = items
        self.dialouge = dialouge
    
    def print_all_exits_name(self):
        directions = ["north", "east", "south", "west"]
        for direction in directions:
            try:
                if self.exits[direction] is not None:
                    print("GO " + direction.upper() + " to " + self.exits[direction] + ".")
                    time.sleep(0.25)
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
    

    def all_enemies_dead(self):
        enemies_dead = 0
        for enemy in self.enemies:
            if enemy.is_dead():
                enemies_dead += 1
        
        if enemies_dead == len(self.enemies):
            return True

        else:
            return False
    

    def print_room(self):
        """This function takes a Room as an input and nicely displays its name,
        description and items within it."""

        print("Press 's' to skip the scrolling text!\n")
        scrolling_text(self.name.upper())
        print("")
        scrolling_text(self.description)
        print("")
        self.print_enemies()


    def has_dialouge(self):
        if self.dialouge != "":
            return True
        else:
            return False
        
    
    def print_dialogue(self):
        if self.has_dialouge():
            print("Press 's' to skip the scrolling text!\n")
            scrolling_text(self.dialouge)

    
    def puzzle_room(self):#-------------------------------------------------------
        if self.dialouge["puzzle"] is not None:
            pass



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
            print("\nEnemies:")
            print("There is" + self.list_of_enemies(), "here.")

    
    def is_valid_exit(self, direction):
        """returns the value of the key in the directions of the room"""
        
        return direction in self.exits
    

    def pick_up_enemy_items(self, enemy):
        """This method picks up items from the dead enemies
        and allows the player to pick them up from the room"""
        
        for item in enemy.items:
            self.items.append(item)
            enemy.items.remove(item)
            

    



