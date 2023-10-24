#OOP for the enemies

from player import player
from items import *


class Enemy():
    def __init__(self, name, health, damage_per_hit, items, current_room):
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
        overall_weight = 0
        for item in self.items:
            overall_weight += item["weight"]
        for item in self.items:
            player.pick_up_item(item, self)
            self.items.remove(item)
        
            
            

first_year = Enemy("First Year", 50, 10, ["rock"], "")

mature_first_year = Enemy("Mature First Year", 70, 20, ["bare fists", "glasses"], "")

second_year = Enemy("Second Year", 80, 25, ["lynx africa", "glasses"], "")

second_year = Enemy("Second Year", 80, 25, ["lynx africa", "glasses", "health potion"], "")

communist_society_president = Enemy("Communist Society President", 200, 30, ["shield", "Communist Manifesto" "room 14 key"], "")

mark_drakeford = Enemy("Mark Drakeford", 120, 35, ["swatter", "Peitho's voice"], "")

phd_student = Enemy("PHD Student", 120, 35, ["shovel", "timberland boots"], "")

medicine_student = Enemy("Medicine Student", 160, 40, ["spine", "frog", "health potion"], "")

law_student = Enemy("Law Student", 160, 40, ["mallet", "necklace"], "")

professor_stuart_allen = Enemy("Professor Student Allen", 200, 50, ["boss bare fists", "gpu", "Chris"], "")

                
            

