#OOP for the enemies

from player import player


class Enemy():
    def __init__(self, name, health, damage_per_hit, weapon,  items, current_room):
        self.name = name
        self.health = health
        self.damage_per_hit = damage_per_hit
        self.weapon = weapon
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
        overall_weight = 0
        for item in self.items:
            overall_weight += item["weight"]
        for item in self.items:
            player.current_room.inventory.append(item)
        
            
            

first_year = Enemy("First Year", 50, 10, "macbook", ["4 cans of cider", "hoodie", "macbook"], "")

mature_first_year = Enemy("Mature First Year", 70, 20, "bare hands", ["money", "gold ring", "key"], ["The_Taff", "The_Lounge", "Love_Cardiff_shop"])

second_year = Enemy("Second Year", 80, 25, ["hot coffee", "knives"], ["knives", "car keys"], "")

society_president = Enemy("Society President", 200, 30, "big red sword", ["big red sword", "Shield", "key"], "The_Senedd")

phd_student = Enemy("PHD Student", 120, 35, "walking stick", ["doctor certificate", "ak47", "walking stick"], "")

medicine_student = Enemy("Medicine Student", 160, 40, ["stethoscope", "syringe"], ["syringe", "scissors", "dictionary", "stethoscope", "bag of money"], "The_Prince_of_Wales")

professor_stuart_allen = Enemy("Professor Student Allen", 200, 50, ["firing book", "teaching associates robots"], "cris", "")

                
            

