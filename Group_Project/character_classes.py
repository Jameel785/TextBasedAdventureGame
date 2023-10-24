from items import items

#OOP for the player

class Player():
    def __init__(self, health, damage_per_hit, current_room, inventory, max_weight):
        self.name = "Kirill"
        self.health = health
        self.damage_per_hit = damage_per_hit
        self.current_room = current_room

        self.inventory = inventory
        self.max_weight = max_weight
        self.weight = self.weight_calculator()


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
            item_dropped = int(input("You cannot carry this many items, please drop one \n"+ self.list_of_items() + "\n >>"))
            
            count = 0
            for item in self.inventory:
                if item.name == item_dropped:
                    self.drop_item(item)
                    weight -= item.weight
                    count += 1

            if count == 0:
                print("Please try again! \n")
            
            if weight > self.max_weight:
                print("You still cannot carry this much, please drop another item! \n")

            elif weight < self.max_weight:
                return True
    


#OOP for the enemies

class Enemy():
    def __init__(self, id, name, health, damage_per_hit, items):
        self.id = id
        self.name = name
        self.health = health
        self.damage_per_hit = damage_per_hit
        self.weapon = items[0]
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
            self.drop_items()
            return True
        else:
            return False
        

    def drop_items(self):
        """This method drops items from the dead enemies
        and allows the player to pick them up from the room"""
        
        overall_weight = 0
        for item in self.items:
            overall_weight += item["weight"]
        for item in self.items:
            player.current_room.items.append(item)
            self.items.remove(item)
