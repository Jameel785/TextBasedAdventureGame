#OOP for the player

from game import *

#Could add:
#Different strengths and weaknesses

class Player():
    def __init__(self, name, health, damage_per_hit, current_room, inventory, max_weight):
        self.name = "Kirill"
        self.health = health
        self.damage_per_hit = damage_per_hit
        self.current_room = current_room

        self.inventory = inventory
        self.weight = self.weight_calculator()
        self.max_weight = max_weight

    def remove_health(self, damage):
        """This method decreases the health of the player by 
        the damage variable"""

        self.health -= damage
            

    def add_health(self, healing):
        """This method increases the health of the player by
        the healing variable"""

        self.health += healing

    def is_dead(self):
        """This method checks if the health of an enemy is 
        less than zero (if they are dead) and returns if 
        True for dead and False for not dead"""

        if self.health <= 0:
            return True
        else:
            return False
        
        
    def drop_item(self, item):
        """This method allows the user to drop a specified item"""

        self.inventory.remove(item)
        print("You have dropped,", item["name"])

        self.current_room["items"].append(item)


    def pick_up_item(self, item):
        """This method allows the user to pick up a specified item"""

        self.inventory.append(item)
        if self.weight_calculator():
            print("You have picked up the item!") # maybe add item name later

        self.current_room["items"].remove(item)


    def weight_calculator(self):
        """This method calculates the weight of all the items on 
        the user and if the weight of these items is greater than
        the max weight the player can carry it asks them to drop 
        a specific item"""

        weight = 0
        for item in self.inventory:
            weight += item["weight"]

        while weight > self.max_weight:
            item_dropped = int(input("You cannot carry this many items, please drop one \n"+ list_of_items(self.inventory) + "\n >>"))
            
            count = 0
            for item in self.inventory:
                if item["name"] == item_dropped:
                    self.drop_item(item)
                    weight -= item["weight"]
                    count += 1
            if count == 0:
                print("Please try again!")
            
            if weight > self.max_weight:
                print("You still cannot carry all this please drop another item!")

            elif weight < self.max_weight:
                return True
    

            

            
            
           

