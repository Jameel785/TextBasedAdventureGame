

class Item():
    def __init__(self, id, name, description, damage_increase, weight, owned_by):
        self.id = id
        self.name = name
        self.description = description
        self.damage_increase = damage_increase
        self.weight = weight
        self.owned_by = owned_by


"""Add all the item classes in the format of:"""

# item_name_here = Item(item_id, item_name, item_description, item_damage_increase, item_weight, item_is_owned_by)

#example:

item_blunderbuss = ("blunderbuss-firearm", "blunderbuss", "blast your enemies back to the 18th century.", "damage increase", "weight", None)

item_swatter = ()

item_key2 = ()

item_key1 = ()

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

item_africa = ()

item_GPU = ()

items = {
    "gpu": item_GPU,
    "lynx_africa": item_africa,
    "mallet": item_mallet,
    "glasses": item_glasses,
    "timberland_boots": item_boots,
    "shovel": item_shovel,
    "frog": item_frog,
    "spine": item_spine,
    "gloves": item_gloves,
    "rock": item_rock,
    "necklace": item_necklace,
    "health_potion": item_health,
    "key1": item_key1,
    "key2": item_key2,
    "swatter": item_swatter,
    "blunderbuss": item_blunderbuss,
}


#Dan