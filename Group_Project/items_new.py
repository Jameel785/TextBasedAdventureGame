

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

item_blunderbuss = ("blunderbuss", "blunderbuss", "blast your enemies back to the 18th century.", 45, 10, None)


item_frog = ("frog","a friendly frog","will follow you and lick the eyes of your enemies causing damage",5,0,None)

item_swatter = ("swatter","a venemous fly swatter","provides poison damage over time. damage for 3 turns.",10,5,None)

item_key1 = ("key1","a large key","a comically large key. opens a comically large door",0,1,None)

item_key2 = ("key2","a larger key","an even larger, more comedic key. most likey opens a larger door too",0,2)

item_health = ("health_potion","a health potion","increases health by 35%.\n rasberry flavour (403 calories)",0,3,None)

item_necklace = ("necklace","a cross necklace","the last signs of faith in this ungodly land. increases max health by 20",0,2,None)

item_rock = ("rock","a large rock","the caveman's wepon of choice.",20,6,None)

item_gloves = ("gloves","mohamed ali's boxing gloves","immediately gain the boxing ability mohamed ali. can be used to dammage enemies.",25,4,None)

item_spine = ("spine","a human spine","who does this belong to? sharp and jagged, perfect for killing enemies.",40,5,None)

item_shovel = ("shovel","a shovel","like a spade but different. good for killing enemies.",30,3,None)

item_boots = ("timberland_boots","a pair of timberland boots","can kick enemies in beige.",35,4,None)

item_glasses = ("glasses","a pair of sun glasses","looks cool.",0,1)

item_mallet = ("mallet","a large wooden mallet","will leave a tom and jerry esque mound on your enemies head.",40,8,None)

item_africa = ("lynx_africa","a can of lynx aftrica","severely toxic to anyone in range. can be sprayed on enemies. deals damage over 2 turns",15,3,None)

item_GPU = ("gpu","an ASUS ROG strix gaming RTX 4090 ti extreme blue eddition","has more names than an italian painter and is the size and weight of a cinder block. can hit enemies with it.",50,20,None)

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