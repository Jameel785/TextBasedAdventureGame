#class for the items heald by players, enemies, and rooms

class Item():
    def __init__(self, id, name, description, damage_increase, weight):
        self.id = id
        self.name = name
        self.description = description
        self.damage_increase = damage_increase
        self.weight = weight


#item class name          item id      name of item     decription of item                        damage  weight
item_blunderbuss = Item("blunderbuss", "blunderbuss", "will blast your enemies back to the 18th century.", 45, 10)

item_frog = Item("frog", "friendly frog", "will follow you and lick your eyes, But Jerry likes licking.", 5, 0.3)

room_14_key = Item("key1", "large key", "is a comically large key and it opens a comically large door.", 0, 1)

room_20_key = Item("key2", "HUGE key", "is an even larger, more comedic key. Honestly how can you even carry it!", 0, 2)

item_potion = Item("potion", "potion", "heals health by 20 points it also comes in rasberry flavour (403 calories)", 0, 3)

item_necklace = Item("necklace", "cross necklace", "is the last signs of faith in this ungodly land.", 0, 2)

item_rock = Item("rock", "large rock", "is the caveman's wepon of choice.", 20, 6)

item_spine = Item("spine", "human spine", "belongs to... who does this belong to?", 15, 5)

item_shovel = Item("shovel", "shovel", "is like a spade but different...", 25, 3)

item_boots = Item("boots", "boots", "can kick enemies in beige.", 35, 4)

item_glasses = Item("glasses", "pair of sun glasses", "looks cool.", 0, 1)

item_mallet = Item("mallet", "large wooden mallet", "will leave a Tom and Jerry esque mound on your enemies head.", 40, 8)

item_lynx_africa = Item("lynx", "can of lynx africa", "is severely toxic to anyone in range, can be sprayed on enemies.", 20, 3)

item_GPU = Item("gpu", "ASUS ROG strix gaming RTX 4090 ti extreme blue edition", "has more names than an italian painter and is the size and weight of a cinder block.", 50, 20)

item_knuckle_dusters = Item("knuckle", "knuckle_dusters", "is for those with pure skill and ability no hadicaps here.", 30, 0)

item_speech = Item("speech", "a magical yaping ability", "gives the user an incredibaly compelling voice that fills the room with definately not paid actors forced to listen.", 0, 0)

item_boss_bare_fist = Item("Stuarts_hands", "Stuarts_fingies", "is the hand that control the minds of the whole Computer science school.", 50, 100)

Chris = Item("Chris", "Chris", "is the love of Kirill's life.", 0, 0)

Stuart_Allens_Mum = Item("Stuart Allen's Mum", "Stuart Allen's Mum", "is the mother of the head of the computer science school, and now you've taken her hostage!!", 0, 0) 

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
    "rock": item_rock,
    "necklace": item_necklace,
    "potion": item_potion,
    "room 14 key": room_14_key,
    "room 20 key": room_20_key,
    "blunderbuss": item_blunderbuss,
    "knuckle_dusters": item_knuckle_dusters,
    "speech": item_speech,
    "boss bare fist": item_boss_bare_fist,
    "Chris": Chris,
    "Stuart_Allens_Mum": Stuart_Allens_Mum
}

