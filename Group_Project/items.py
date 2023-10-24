#class for the items heald by players, enemies, and rooms

class Item():
    def __init__(self, id, name, description, damage_increase, weight):
        self.id = id
        self.name = name
        self.description = description
        self.damage_increase = damage_increase
        self.weight = weight


#item class name          item id      name of item     decription of item                        damage  weight
item_blunderbuss = Item("blunderbuss", "blunderbuss", "blast your enemies back to the 18th century.", 45, 10)

item_frog = Item("frog", "friendly frog", "will follow you and lick the eyes of your enemies causing damage", 5, 0.3)

item_swatter = Item("swatter", "venemous fly swatter", "provides poison damage over time. damage for 3 turns.", 10, 5)

room_14_key = Item("key", "large key", "a comically large key. opens a comically large door", 0, 1)

room_20_key = Item("key", "HUGE key", "an even larger, more comedic key. most likey opens a larger door too", 0, 2)

item_potion = Item("potion", "potion", "heals health by 35%.\n rasberry flavour (403 calories)", 0, 3)

item_necklace = Item("necklace", "cross necklace", "the last signs of faith in this ungodly land. increases max health by 20", 0, 2)

item_rock = Item("rock", "large rock", "the caveman's wepon of choice.",20,6)

item_gloves = Item("gloves", "boxing gloves taken from Mohamed Ali's ", "immediately gain the boxing ability mohamed ali. can be used to dammage enemies.", 25, 4)

item_spine = Item("spine", "human spine", "who does this belong to? sharp and jagged, perfect for killing enemies.", 40, 5)

item_shovel = Item("shovel", "shovel", "like a spade but different. good for killing enemies.", 30, 3)

item_boots = Item("timberland_boots", "pair of timberland boots", "can kick enemies in beige.", 35, 4)

item_glasses = Item("glasses", "pair of sun glasses", "looks cool.", 0, 1)

item_mallet = Item("mallet", "large wooden mallet", "will leave a tom and jerry esque mound on your enemies head.", 40, 8)

item_lynx_africa = Item("lynx_africa", "can of lynx aftrica", "severely toxic to anyone in range. can be sprayed on enemies. deals damage over 2 turns", 15, 3)

item_GPU = Item("gpu", "ASUS ROG strix gaming RTX 4090 ti extreme blue eddition", "has more names than an italian painter and is the size and weight of a cinder block. can hit enemies with it.", 50, 20)

item_knuckle_dusters = Item("knuckle_dusters", "knuckle dusters", "pure skill and avbility no hadicaps here", 5, 0)

item_coffee = Item("coffee", "a pretentiously brewed coffee", "may cause caffeen addiction. restores 45 health.", 0, 4)

item_shield = Item("shield", "a great warriors shield (skate board)", "negate incoming attacks from enemies ONLY if you can land a kickflip", 0,8)

item_speech = Item("speech", "a magical captivating yaping ability", "gives the user an incredibaly compelling voice that fills the room with definately not paid actors forced to listen", 0, 0)

item_boss_bare_fist = Item("boss_bare_fist", "Stuart Allen's mighty hands", "The hands that control the minds of the whole Computer science school", 50, 100)

Chris = Item("Chris", "Chris", "The love of Kirill's life", 0, 0)

Stuart_Allens_Mum = ("Stuart Allen's Mum", "Stuart Allen's Mum", "The mother of the head of the computer science school, maybe you could hold her hostage?", 0, 0) 

items = {  

    #a dictionary storing all the items under the name items for ease of access.    

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
    "potion": item_potion,
    "room 14 key": room_14_key,
    "room 20 key": room_20_key,
    "swatter": item_swatter,
    "blunderbuss": item_blunderbuss,
    "knuckle dusters": item_knuckle_dusters,
    "coffee": item_coffee,
    "shield": item_shield,
    "speech": item_speech,
    "boss bare fist": item_boss_bare_fist,
    "Chris": Chris,
    "Stuart Allen's Mum": Stuart_Allens_Mum
}

