#OOP for the enemies

from game import *

#Could add:
#Different strengths and weaknesses

class Enemy():
    def __init__(self, name, health, damage_per_hit, items, current_room):
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
        
            
            

"""Add all the room classes in the format of:"""

# enemies_name_here = Enemy(enemies_name, enemies_health, enemies_damage_per_hit, enemies_items, enemies_current_room)

    
            
            
#Jameel

