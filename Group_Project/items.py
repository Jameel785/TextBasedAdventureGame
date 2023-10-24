from player import player
from enemies import *

class Item():
    def __init__(self, id, name, description, damage_increase, weight, owned_by):
        self.id = id
        self.name = name
        self.description = description
        self.damage_increase = damage_increase
        self.weight = weight
        self.owned_by = owned_by



item_blunderbuss = ("blunderbuss-firearm", "blunderbuss", "blast your enemies back to the 18th century.", "damage increase", "weight", None)

item_swatter = ()

room_20_key = ()

room_14_key = ()

item_health = ()

item_necklace = ()

item_rock = ()

item_gloves = ()

item_spine = ()

item_frog = ()

item_shovel = ()

item_boots = ()

item_glasses = ()

item_mallet = ()

item_lynx_africa = ()

item_GPU = ()

item_bare_fists = ()

item_coffee = ()

item_shield = ()

item_peitho_voice = ()

item_boss_bare_fist = ()

Chris = ()


items = {
    "gpu": item_GPU,
    "lynx africa": item_lynx_africa,
    "mallet": item_mallet,
    "glasses": item_glasses,
    "timberland boots": item_boots,
    "shovel": item_shovel,
    "frog": item_frog,
    "spine": item_spine,
    "gloves": item_gloves,
    "rock": item_rock,
    "necklace": item_necklace,
    "health potion": item_health,
    "room 14 key": room_14_key,
    "room 20 key": room_20_key,
    "swatter": item_swatter,
    "blunderbuss": item_blunderbuss,
    "bare fists": item_bare_fists,
    "coffee": item_coffee,
    "shield": item_shield,
    "Peitho's voice": item_peitho_voice,
    "boss bare fist": item_boss_bare_fist,
    "Chris": Chris
}

