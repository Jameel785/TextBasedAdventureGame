from items import *
from map import Room
from character_classes import Enemy, Player
    
#defining each enemy for each room
first_year_room_4 = Enemy("Fresher", "First Year", 50, 5, ["rock"])

first_year_room_5_1 = Enemy("Fresher", "First Year", 50, 5, ["rock"])
first_year_room_5_2 = Enemy("Fresher", "First Year", 50, 5, ["rock"])

mature_first_year_room_6_1 = Enemy("Old_Fresher", "Mature First Year", 70, 10, ["knuckle_dusters", "glasses"])
first_year_room_6_1 = Enemy("Fresher", "First Year", 50, 5, ["rock"])
first_year_room_6_2 = Enemy("Fresher", "First Year", 50, 5, ["rock"])

second_year_room_7_1 = Enemy("Second_Year", "Second Year", 80, 20, ["lynx africa", "glasses"])
mature_first_year_room_7_1 = Enemy("Old_Fresher", "Mature First Year", 70, 10, ["knuckle_dusters", "glasses"])
mature_first_year_room_7_2 = Enemy("Old_Fresher", "Mature First Year", 70, 10, ["knuckle_dusters", "glasses"])

second_year_room_9_1 = Enemy("Second_Year", "Second Year", 80, 20, ["lynx africa", "glasses"])
second_year_room_9_2 = Enemy("Second_Year", "Second Year", 80, 20, ["lynx africa", "glasses"])

buff_art_second_year_room_11 = Enemy("BUFF ART Second Year", "Second Year", 200, 50, ["lynx africa", "glasses"])

communist_society_president_room_12_1 = Enemy("Communist_Pres", "Communist Society President", 200, 30, ["necklace", "Communist Manifesto"])
first_year_room_room_12_1 = Enemy("Fresher", "First Year", 50, 10, ["rock"])
first_year_room_room_12_2 = Enemy("Fresher", "First Year", 50, 10, ["rock"])


mark_drakeford_room_13_1 = Enemy("Mark", "Mark Drakeford", 120, 35, ["speech"])

phd_student_room_16_1 = Enemy("PHD", "PHD Student", 120, 35, ["shovel", "boots"])

medicine_student_room_18_1 = Enemy("Med_Student", "Medicine Student", 160, 40, ["spine", "frog"])
medicine_student_room_18_2 = Enemy("Med_Student", "Medicine Student", 160, 40, ["spine", "frog"])
law_student_room_18 = Enemy("Law_Student", "Law Student", 160, 40, ["mallet", "necklace", "Stuart Allen's Mum"])

professor_stuart_allen_room_20 = Enemy("Prof_Stuart", "Professor Stuart Allen", 200, 50, ["boss bare fists", "gpu", "Chris"])



#1
Lecture_Room = Room(
    "Lecture Room",

"""
You are in the lecture Room for computer science.
The odour of sweaty armpits and stale deodorant is rampant.
Alongside is empty bottles of energy drinks on the floor.
There are rows of seats lined across the hall with a large whiteboard stacked at the end of the lecture hall.""",

    {"north":"Computer Lab", "east":"Seminar Room", "south":"The Great Hall"},

    [],

    [],

"""\nOnce upon a time in the land of Cardiff lived a happy beautiful couple.
Kirill and Chris held hands affectionately as they watched the golden sun set behind the majestic castle.
They had met at a league of legends tournament and Kirill had caught a glance at Chris who was sat at the opposite side of the room.
It was love at first site and ever since then they have passionately enjoyed each other’s company for 6 loving months.
The sun had fully set now and the glowing moon caressed Kirill and Chris who were laying down gazing at the stars.
The night was getting late, and they had both fell asleep on the grass holding each other close, dreaming of the day of their wedding.
Suddenly Kirill was awoken by the sounds of unsettling screams.
He had turned to look at Chris, but he had vanished!
He then sees in the distance, the distressed Chris being carried away by a hooded figure, struggling to break free. Chris had been kidnapped!!!

Sheep:
“Baaah, hello the great mighty Kirill!
I am a sheep and I have been sent to give you some terrible news. Baaaah!
Your beloved Chris has been kidnapped by an evil being capable of causing the most destructive atrocities known to man.
Bahh! But I believe with your mighty strength and immense will power, 
you will be able to rid this horrid being from all the lands and save your beloved Chris.
But be warned, I have heard the evil monster has hired foot soldiers to stop you from reaching him in his evil lair.
Hurry! You must go now! Bahhhhhh!”\n\n"""
)

#2
Computer_lab = Room(
    "Computer Lab", 
    
"""
You are now in the computer suite.
There are rows upon rows of personal computers hooked up to cheap monitors on the desks.
On the desks are empty plug sockets and turned off switches.
The keyboards are full of breadcrumbs and surrounded by empty crisp packets.""", 
    
    {"south":"Lecture Room"}, 

    [],

    [],

    ""
)

#3
Seminar_Room = Room(
    "Seminar Room",
    
"""
You are now in the seminar Room.
There are desks upon desks littered across the Room.
On top of the desks are piles of scribbled paper sheets and empty pencil cases.""",
    
    {"west":"Lecture Room"},

    [],

    [],

    """Squidward:
“Oh barnicles. You really think you can save Chris?
Its impossible, just give up already.
The evil being is too powerful for someone like you to defeat. Just let go of Chris and come work at the Krusty Krab.
SpongeBob is totally useless and extreeemmly annoying to be quite frank and I am in urgent need of a second pair of hands,
not SpongeBobs hands of course, so please come work here.”"""
)

#4
The_Great_hall = Room(
    "The Great Hall",

"""
You are now in the great hall of the student union.
Surrounding you is vast plains of empty space, with left over cardboard cutouts from the previous freshers fair.
With a capacity of over 1,600 people, there is no shortage of empty space here.""",

    {"north":"Lecture Room", "east":"Seminar Room", "south":"The Taff", "west":"The Lounge"},

    [first_year_room_4],

    [],

    ""
)

#5
The_Taff = Room(
    "The Taff",

"""
You are now in the taff.
The taff is the local pub built into the student union.
The stench of cheap beer and stale lager is rampant.
The floor is littered with empty beer bottles and tissues.""",

    {"north":"The Great Hall", "west":"Love Cardiff Shop"},

    [first_year_room_5_1, first_year_room_5_2],

    [],

    ""
)

#6
The_Lounge = Room(
    "The Lounge",

"""
You are now in the lounge.
Around you are study spaces where students could sit and chat.
There are also play areas filled with table tennis tables and pool tables.""",

    {"north":"Lecture Room", "east":"The Great Hall"},

    [mature_first_year_room_6_1, first_year_room_6_1, first_year_room_6_2],

    [],

    ""
)

#7
Love_Cardiff_shop = Room(
    "Love Cardiff Shop",

"""
You are now in the Love Cardiff Shop.
Inside the store are rows upon rows of stacked clothing.
T-shirts and crew neck jumpers marked at half price.
There are receipt papers and coat hangers littered across the floor.""",

    {"west":"Ferris Wheel"},

    [second_year_room_7_1, mature_first_year_room_7_1, mature_first_year_room_7_2],

    [],

    ""
)

#8
Ferris_wheel = Room(
    "Ferris Wheel",

"""
You are now at the giant Ferris wheel in the Cardiff Bay.
The Cardiff bay has endless seagulls and birds scattered across its coats.
The sea is deep blue and its sand is bright white.
The Ferris wheel itself stand large and tall.
It is easily the largest structure in Cardiff bay.""",

    {"north":"Queens Arcade", "south":"Cardiff Docks", "west":"Millenium Centre"},

    [],

    [],

    """Gandalf:
“Greetings fellow traveller.
Well done on getting this far, you have slain many powerful enemies, and you are getting stronger by the minute!
Keep fighting and soon you will finally defeat the evil all powerful being and save the beautiful Chris.
However, heed my warning, the enemies that lie ahead will be more powerful than you have faced so far.
Second-year students lie in this part of town and have much more health and damage per hit than the first years so make sure you are prepared!”"""
)

#9
Cardiff_docks = Room(
    "Cardiff Docks",

"""
You are now at the Cardiff bay and docks.
There are boats surrounding the entire area.
Seagulls are squeaking as they are flying through the air and the sky has a bright blue hue to it.""",

    {"north":"Ferris Wheel", "south":"Roald Dahl Plass"},

    [second_year_room_9_1, second_year_room_9_2],

    [],

    ""
)

#10
Roald_Dahl_plass = Room(
    "Roald Dahl Plass",

"""
You are now at the roald dahl plass.
This is a plaza with plenty of places to eat and drink and it is surrounded by illuminated pillars.
The smell of burnt popcorn and cotton candy has filled the air and there is magical atmosphere which fills your mood.""",

    {"north":"Cardiff Docks", "east":"Seminar Room"},

    [],

    ["room 14 key"],

    ""
)

#11
Millenium_centre = Room(
    "Millenium Centre",

"""You are now at the Millennium Centre.
The sound of opera pierces the air around you, worrying you that if you get too close, your glasses may shatter.
Luxuriously dressed men and women saunter around, carrying stylish fans and theatre binoculars. 
Judgemental looks are cast your way, presumably due to your more casual attire.""",

    {"east":"Ferris Wheel", "south":"Cardiff Docks"},

    [buff_art_second_year_room_11],

    [],

    ""
)

#12
The_Senedd_1 = Room(
    "The Senedd Room 1",
    
"""You are now in the Senedds first room.
Distant noises of shouting politicians can be heard, 
you struggle to understand what they are saying.
The water from the bay casts glistening streaks of light across its walls, 
somehow making a parliamentary building seem quite relaxing.""",

    {"north":"The Senedd Room 2"},

    [communist_society_president_room_12_1, first_year_room_room_12_1, first_year_room_room_12_2],

    [],

    ""
)

#13
The_Senedd_2 = Room(
    "The Senedd Room 2",

"""You are now in the Senedds second room.
You try and listen along to what everyone is saying, 
but everything is half in Welsh and your Duolingo hasn’t quite reached politics yet.
“I believe we should raise taxes across South Wales!”""",

    {"east":"Millenium Centre"},

    [mark_drakeford_room_13_1],

    [],

    ""
)

#14
Queens_arcade = Room(
    "Queens Arcade",
    
"""You are now in the Queens Arcade.
Students bustle around you, gripping their id cards for dear life in search of discounts.
Walking past an American sweet shop, you hear the classic 
“It’s a front for money laundering you know, I never see anyone in there!”""",

    {"north":"Cardiff Museum"},

    [],

    [],

    """
    Wise Mystical Tree –
    “Welcome Kirill.
    My senses tell me that you are a brave mighty warrior.
    And that you will soon defeat the evil being that has tormented these lands for many years and save the enchanted Chris.
    However, the enemies that await you, will be challenging even for someone as brave and mighty as yourself.
    You are now in the territory of the third-year and PHD students.
    They possess greater strength and wield mightier attacks than what you have faced so far.
    So please do take these health potions growing from my branch to aid you in your battles.”
    """
)

#15
Cardiff_museum = Room(
    "Cardiff Museum",
    
"""You are now in the Cardiff Museum.
The air is quiet and filled only with the sound of quiet murmurs and shuffling feet.
You admire the painting-adorned walls, pausing momentarily to gaze at a beautiful, bearded princess.""",

    {"north":"Cardiff Castle", "east":"Principality Stadium", "west":"NQ64"},

    [],

    [],

    ""
)

#16
NQ64 = Room(
    "NQ64",
    
"""You have now entered NQ64.
The air is buzzing with electrifying gunshot sounds and cheers of celebration.
Bartenders dish out neon, overpriced drinks, 
with the manager smiling gleefully in the back as the pings of Apple Pay break through the sounds of joy.""",

    {"north":"The Earnest Willows", "east":"Cardiff Museum"},

    [phd_student_room_16_1],

    [],

    ""
)

#17
The_Earnest_willows = Room(
    "The Earnest Willows",
    
"""You have now entered the Earnest Willows.
The stench of cheap, poorly poured pints is rampant, 
being drank by a group of elderly men who glare with every movement you take.
With every step, your foot seems to stick more and more to the beer covered floor.""",

    {"north":"The Prince of Wales"},

    [],

    [],

    ""
)

#18
The_Prince_of_Wales = Room(
    "The Prince Of Wales",
    
"""You have now entered the Prince of Wales.
Formally a sex cinema, it is now a hub full of students and locals alike.
Blue plates covered in stale burgers and soggy chips cast a foggy haze across the walls,
 and the sound of rugby and chatter is almost defeaning.""",

    {"south":"NQ64"},

    [medicine_student_room_18_1, medicine_student_room_18_2, law_student_room_18],

    [],

    ""
)

#19
Principality_stadium = Room(
    "Principality Stadium",
    
"""You have now entered Principality Stadium.
Filled to the brim with supporters of both teams, screams and cheers fill the air.
You pause for a moment to watch two big bald burly men fighting in the stands, 
while their wives look upon with disappointment.""",

    {"west":"Cardiff Museum"},

    [],

    ["room 20 key"],

    ""
)

#20
Cardiff_castle = Room(
    "Cardiff Castle",
    
"""You have now entered Cardiff Castle.
Screaming with joy, children loop around you, 
covered in foam chainmail gear and whacking each other with swords and maces.
Light pierces through gaps in the stone walls, 
and the foggy autumn air creates an atmosphere that can only be described as the “calm before the storm”.""",

    {"north":"END"},

    [professor_stuart_allen_room_20],

    [],

    ""
)

rooms = {
    "Lecture Room":Lecture_Room,
    "Computer Lab":Computer_lab,
    "Seminar Room":Seminar_Room,
    "The Great Hall":The_Great_hall,
    "The Taff":The_Taff,
    "The Lounge":The_Lounge,
    "Love Cardiff Shop":Love_Cardiff_shop,
    "Ferris Wheel":Ferris_wheel,
    "Cardiff Docks":Cardiff_docks,
    "Roald Dahl Plass":Roald_Dahl_plass,
    "The Senedd Room 1":The_Senedd_1,
    "Millenium Centre":Millenium_centre,
    "The Senedd Room 2":The_Senedd_2,
    "Queens Arcade":Queens_arcade,
    "Cardiff Museum":Cardiff_museum,
    "NQ64":NQ64,
    "The Earnest Willows":The_Earnest_willows,
    "The Prince Of Wales":The_Prince_of_Wales,
    "Principality Stadium":Principality_stadium,
    "Cardiff Castle":Cardiff_castle
}


#This allows starts the players journeys
player = Player(rooms["Lecture Room"], ["potion", "potion", "rock"], 25) 
