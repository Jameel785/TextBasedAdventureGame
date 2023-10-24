from player import Player
from enemies import Enemy
from map import rooms
from items import *

#This allows starts the players journeys
player = Player(100, 15, rooms["Lecture Room"], {item_health, item_health, item_rock}, 20)  


#defining each enemy for each room
first_year_room_4 = Enemy("First Year", 50, 10, ["rock"])

first_year_room_5_1 = Enemy("First Year", 50, 10, ["rock"])
first_year_room_5_2 = Enemy("First Year", 50, 10, ["rock"])

mature_first_year_room_6_1 = Enemy("Mature First Year", 70, 20, ["bare fists", "glasses"])
first_year_room_6_1 = Enemy("First Year", 50, 10, ["rock"])
first_year_room_6_2 = Enemy("First Year", 50, 10, ["rock"])

second_year_room_7_1 = Enemy("Second Year", 80, 25, ["lynx africa", "glasses", "health potion"])
mature_first_year_room_6_1 = Enemy("Mature First Year", 70, 20, ["bare fists", "glasses"])
mature_first_year_room_6_2 = Enemy("Mature First Year", 70, 20, ["bare fists", "glasses"])

second_year_room_9_1 = Enemy("Second Year", 80, 25, ["lynx africa", "glasses", "health potion"])
second_year_room_9_2 = Enemy("Second Year", 80, 25, ["lynx africa", "glasses", "health potion"])

second_year_room_11_1 = Enemy("Second Year", 80, 25, ["lynx africa", "glasses", "health potion"])

communist_society_president_room_12_1 = Enemy("Communist Society President", 200, 30, ["shield", "Communist Manifesto" "room 14 key"])
first_year_room_room_12_1 = Enemy("First Year", 50, 10, ["rock"])
first_year_room_room_12_2 = Enemy("First Year", 50, 10, ["rock"])


mark_drakeford_room_13_1 = Enemy("Mark Drakeford", 120, 35, ["swatter", "Peitho's voice"])

phd_student_room_16_1 = Enemy("PHD Student", 120, 35, ["shovel", "timberland boots"])

medicine_student_room_18_1 = Enemy("Medicine Student", 160, 40, ["spine", "frog", "health potion"])
medicine_student_room_18_2 = Enemy("Medicine Student", 160, 40, ["spine", "frog", "health potion"])
law_student_room_18_1 = Enemy("Law Student", 160, 40, ["mallet", "necklace"])
law_student_room_18_2 = Enemy("Law Student", 160, 40, ["mallet", "necklace"])

professor_stuart_allen_room_20_1 = Enemy("Professor Student Allen", 200, 50, ["boss bare fists", "gpu", "Chris"])
