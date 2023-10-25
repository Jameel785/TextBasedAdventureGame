from items import items
from game_parser import normalise_input
from game import scrolling_text
import time
#OOP for the player

class Player():
    def __init__(self, current_room, inventory, max_weight):
        self.current_room = current_room

        self.start_dialogue()
        self.character_class = self.class_choice()
        self.class_stats()
        self.experience = 100

        self.inventory = inventory
        self.max_weight = max_weight
        self.weight = self.weight_calculator()

        self.give_up = False
    

    def start_dialogue(self):
        print("\nPress 's' to skip the scrolling text!")
        text = self.current_room.dialouge
        scrolling_text(text)

    def remove_health(self, damage):
        """This method decreases the health of the player by 
        the damage variable"""

        self.health -= damage


    def add_health(self, healing):
        """This method increases the health of the player by
        the healing variable"""

        if self.health + healing <= self.max_health:
            self.health += healing

        else:
            self.health = self.max_health

    
    def add_experience(self, enemy):
        if enemy.is_dead():
            self.experience += self.experience_gain

        self.level_up()

    
    def level_up(self):
        while self.experience >= 50:
            self.experience -= 50

            chosen_stat = False

            while not chosen_stat:
                scrolling_text("\nYou've Levelled Up! What stat would you like to increase? (damage, health, exp_gain).\n")
                user_input = input("> ")
                try:
                    user_input = normalise_input(user_input)[0]
                
                except:
                    print("Invalid input")
                    continue

                if user_input == "damage":
                    self.damage_per_hit += 5 
                    chosen_stat = True

                elif user_input == "health":
                    self.max_health += 20
                    self.health += 20
                    chosen_stat = True

                elif user_input == "exp_gain":
                    self.experience_gain += 10
                    chosen_stat = True

            




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
        
        if items[item].id == "key1":

            print("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                   
   8 8 8 8                     ,ooo.       
   8a8 8a8                    oP   ?b      
  d888a888zzzzzzzzzzzzzzzzzzzz8     8b     
   `""^""'                    ?o___oP'     
                              ________      
                              |room 14|     
                              `-------'     
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                  """)

            time.sleep(3)

        elif items[item].id == "key2":

            print('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                    
    ad8888888888ba                                    
    dP          ``8b,                                  
    8  ,aaa,       `Y888a     ,aaaa,     ,aaa,  ,aa,   
    8  8  `8           "88baadP""""YbaaadP"""YbdP""Yb  
    8  8   8              """        """      ""    8b 
    8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P 
    8  `"""         d8                                 
    Yb,         ,ad8"                                  
    "Y8888888888P"                                     
        ________                                      
        |room 20|                                     
        |_______|                                     
                                                        
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                  ''')

            time.sleep(3)

        self.inventory.append(item)
        self.inventory = sorted(self.inventory)

        
    def list_of_items(self):
        """This methods takes all the items in the players 
        inventory and places them in a formatted list"""

        item_string = ""
        for item in self.inventory:
            item_string += (items[item].name.upper() + ", ")
        item_string = item_string[:-2]
        return item_string


    def print_inventory_items(self):
        """This method prints out all the items in the players 
        inventory in a print statement"""

        if len(self.inventory) > 0:
            print("\nInventory items:")
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

        scrolling_text("Before you, Kirill, embark on your journey through this mystical realm, choose your class wisely as your decision will shape your destiny in this epic RPG tale.\n")

        while not choice_valid:
            print("")
            print("Please choose your class:")
            print("type WARRIOR to select the WARRIOR Kirill. High damage, low health, low xp")
            print("type WIZARD to select the WIZARD Kirill. Low damage, low health, high xp")
            print("type BARBARIAN to select the BARBARIAN Kirill. Low damage, high health, low xp")
            print("type CHALLENGE to select the CHALLENGED Kirill. Low damage, low health, low xp")
            user_input = input ("> ")
            user_input = normalise_input(user_input)[0]

            if user_input == "warrior":
                choice_valid = True

            elif user_input == "wizard":
                choice_valid = True

            elif user_input == "barbarian":
                choice_valid = True
                
            elif user_input == "challenge":
                choice_valid = True
            
            else:
                print("invalid input")
                choice_valid = False

        print("")
        return user_input


    def class_stats(self):
        if self.character_class == "warrior":
            self.name = "Warrior Kirill"
            self.health = 150
            self.max_health = 150
            self.damage_per_hit = 40
            self.experience_gain = 20
    
        elif self.character_class == "wizard":
            self.name = "Wizard Kirill"
            self.health = 120
            self.max_health = 120
            self.damage_per_hit = 30
            self.experience_gain = 40

        elif self.character_class == "barbarian":
            self.name = "Barbarian Kirill"
            self.health = 150
            self.max_health = 150
            self.damage_per_hit = 30
            self.experience_gain = 20

        elif self.character_class == "challenge":
            self.name = "Challenged Kirill"
            self.health = 100
            self.max_health = 100
            self.damage_per_hit = 30
            self.experience_gain = 20

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
        
            

        

    
