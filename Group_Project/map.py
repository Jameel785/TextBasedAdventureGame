class Room():
    def __init__(self, name, description, exits, enemies):
        self.name = name
        self.description = description
        self.exits = exits
        self.enemies = enemies
        self.items = []
    
    def print_all_exits_name(self):
        directions = ["north", "east", "south", "west"]
        for direction in directions:
            try:
                if self.exits[direction] is not None:
                    print("GO " + direction.upper() + " to " + self.exits[direction] + ".")
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
        
        print("\n" + self.name.upper())
        print(self.description + "\n")
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
            enemy_string += (enemy.name + ", ")
        enemy_string = enemy_string[:-2]
        return enemy_string


    def print_items(self):
        """This function takes a Room as an input and nicely displays a list of items
        found in this Room (followed by a blank line). If there are no items in
        the Room, nothing is printed."""
        
        if len(self.items) > 0:
            print("There is", self.list_of_items(), "here. \n")


    def print_enemies(self):
        """This function takes a room as an input and nicely displays a list of items
        found in this Room (followed by a blank line). If there are no items in
        the Room, nothing is printed."""
        
        if len(self.enemies) > 0:
            print("There is", self.list_of_enemies(), "here. \n")

    
    def is_valid_exit(self, direction):
        return direction in self.exits


    def exit_leads_to(self, direction):
        """This function takes a dictionary of exits and a direction (a particular
        exit taken from this dictionary). It returns the name of the Room into which
        this exit leads."""
        
        return rooms[self.exits[direction]].name
    



