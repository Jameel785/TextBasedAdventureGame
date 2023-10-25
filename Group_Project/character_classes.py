from items import items
import time
#OOP for the player

class Player():
    def __init__(self, current_room, inventory, max_weight):
        self.character_class = self.class_choice()
        self.class_stats()
        
        self.current_room = current_room

        self.inventory = inventory
        self.max_weight = max_weight
        self.weight = self.weight_calculator()

        self.give_up = False


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
        print("You have dropped your", items[item].name + ".")
        self.current_room.items.append(item)


    def pick_up_item(self, item):
        """This method allows the user to pick up a specified item"""

        self.current_room.items.remove(item)
        if self.weight_calculator():
            print("You have picked up the", item.name + ".")
        self.inventory.append(item)
        self.inventory = sorted(self.inventory)

        
    def list_of_items(self):
        """This methods takes all the items in the players 
        inventory and places them in a formatted list"""

        item_string = ""
        for item in self.inventory:
            item_string += (items[item].name + ", ")
        item_string = item_string[:-2]
        return item_string


    def print_inventory_items(self):
        """This method prints out all the items in the players 
        inventory in a print statement"""

        if len(self.inventory) > 0:
            print("You have", self.list_of_items() + ". \n")


    def weight_calculator(self):
        """This method calculates the weight of all the items on 
        the user and if the weight of these items is greater than
        the max weight the player can carry it asks them to drop 
        a specific item"""

        weight = 0
        for item in self.inventory:
            weight += items[item].weight

        while weight > self.max_weight:
            print("You cannot carry this many items, please drop an item (1, 2...):")
            time.sleep(0.5)
            
            item_string = ""
            for item in self.inventory:
                item_string += items[item].id + ", "
            item_string = item_string[:-2]
            print("You can drop:", item_string + ".")
            item_dropped = int(input("> "))

            try:
                self.drop_item(self.inventory[item_dropped - 1])
                weight -= items[item].weight

            except IndexError:
                print("Please try again! \n")

            if weight < self.max_weight:
                self.weight = weight


    def class_choice(self):

        choice_valid = False

        while not choice_valid:
            print("")
            print("Chose your class:")
            print("type WARRIOR to select the WARRIOR Kirill. High damage, low health, low xp")
            print("type WIZARD to select the WIZARD Kirill. Low damage, low health, high xp")
            print("type BARBARIAN to select the BARBARIAN Kirill. Low damage, high health, low xp")
            print("type CHALLENGE to select the CHALLENGED Kirill. Low damage, low health, low xp")
            choice = input ("> ")
            normalised_choice = choice.lower()
            normalised_choice = normalised_choice.strip()

            if normalised_choice == "warrior":
                choice_valid = True

            elif normalised_choice == "wizard":
                choice_valid = True

            elif normalised_choice == "barbarian":
                choice_valid = True
                
            elif normalised_choice == "challenge":
                choice_valid = True
            
            else:
                print("invalid input")
                choice_valid = False

        print("")
        return normalised_choice


    def class_stats(self):
        if self.character_class == "warrior":
            self.name = "Warrior Kirill"
            self.health = 70
            self.damage_per_hit = 20
            self.experience_gain = 1
    
        elif self.character_class == "wizard":
            self.name = "Wizard Kirill"
            self.health = 70
            self.damage_per_hit = 10
            self.experience_gain = 5

        elif self.character_class == "barbarian":
            self.name = "Barbarian Kirill"
            self.health = 100
            self.damage_per_hit = 10
            self.experience_gain = 1

        elif self.character_class == "challenge":
            self.name = "Challenged Kirill"
            self.health = 70
            self.damage_per_hit = 10
            self.experience_gain = 1

#OOP for the enemies

class Enemy():
    def __init__(self, id, name, health, damage_per_hit, items):
        self.id = id
        self.name = name
        self.health = health
        self.damage_per_hit = damage_per_hit
        self.items = items


    def remove_health(self, damage):
        """This method decreases the health of an enemy by 
        the damage variable"""

        self.health -= damage
            

    def add_health(self, healing):
        """This method increases the health of an enemy by
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
        
            

        

    
