from player import Player


class Item():
    def __init__(self, id, name, description, damage_increase, weight):
        self.id = id
        self.name = name
        self.description = description
        self.damage_increase = damage_increase
        self.weight = weight



item_blunderbuss = Item("blunderbuss", "blunderbuss", "blast your enemies back to the 18th century.", 45, 10)

item_frog = Item("frog", "a friendly frog", "will follow you and lick the eyes of your enemies causing damage", 5, 0)

item_swatter = Item("swatter", "a venemous fly swatter", "provides poison damage over time. damage for 3 turns.", 10, 5)

room_14_key = Item("key1", "a large key", "a comically large key. opens a comically large door", 0, 1)

room_20_key = Item("key2", "a larger key", "an even larger, more comedic key. most likey opens a larger door too", 0, 2)

item_health = Item("health_potion", "a health potion", "increases health by 35%.\n rasberry flavour (403 calories)", 0, 3)

item_necklace = Item("necklace", "a cross necklace", "the last signs of faith in this ungodly land. increases max health by 20", 0, 2)

item_rock = Item("rock", "a large rock", "the caveman's wepon of choice.",20,6)

item_gloves = Item("gloves", "mohamed ali's boxing gloves", "immediately gain the boxing ability mohamed ali. can be used to dammage enemies.", 25, 4)

item_spine = Item("spine", "a human spine", "who does this belong to? sharp and jagged, perfect for killing enemies.", 40, 5)

item_shovel = Item("shovel", "a shovel", "like a spade but different. good for killing enemies.", 30, 3)

item_boots = Item("timberland_boots", "a pair of timberland boots", "can kick enemies in beige.", 35, 4)

item_glasses = Item("glasses", "a pair of sun glasses", "looks cool.", 0, 1)

item_mallet = Item("mallet", "a large wooden mallet", "will leave a tom and jerry esque mound on your enemies head.", 40, 8)

item_lynx_africa = Item("lynx_africa", "a can of lynx aftrica", "severely toxic to anyone in range. can be sprayed on enemies. deals damage over 2 turns", 15, 3)

item_GPU = Item("gpu", "an ASUS ROG strix gaming RTX 4090 ti extreme blue eddition", "has more names than an italian painter and is the size and weight of a cinder block. can hit enemies with it.", 50, 20)

item_bare_fists = Item("fist", "your bare fists", "pure skill and avbility no hadicaps here", 5, 0)

item_coffee = Item("coffie", "a pretentiously brewed coffee", "may cause caffeen addiction. restores 45 health.", 0, 4)

item_shield = Item("shield", "a great warriors shield (skate board)", "negate incoming attacks from enemies ONLY if you can land a kickflip", 0,8)

item_peitho_voice = Item("speach", "a magical captivating yaping ability", "gives the user an incredibaly compelling voice that fills the room with definately not paid actors forced to listen", 0, 0)

item_boss_bare_fist = Item("boss_bare_fist", "Stuart Allen's mighty hands", "The hands that control the minds of the whole Computer science school", 50, 100)

Chris = Item("Chris", "Chris", "The love of Kirill's life", 0, 0)


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

