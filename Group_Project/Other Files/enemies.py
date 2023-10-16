#OOP for the enemies

#Could add:
#Different strengths and weaknesses

class Enemy():
    def __init__(self, name, health, damage_per_hit):
        self.name = name
        self.health = health
        self.damage_per_hit = damage_per_hit

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