#OOP for the enemies

#Could add:
#Different strengths and weaknesses

class Enemy():
    def __init__(self, name, health, damage_per_hit):
        self.name = name
        self.health = health
        self.damage_per_hit = damage_per_hit

    def remove_health(self, damage):
        self.health -= damage

    def add_health(self, healing):
        self.health += healing

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False