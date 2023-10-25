#This is the program which contains most of the important ascpects to the game such as the game loop

#libraries to be used in the program

from random import choice

#sys allows us to quit the file once the game is done and for the scrolling text
import sys

#time allows the scrolling text
import time

#keyboard allows the user to skip the scrolling text
import keyboard

#required information from other programs is imported
from instance_creator import *
from items import *
from game_parser import *

def print_menu():
    """This function displays the menu of available actions to the player."""

    print("You can:")
    time.sleep(0.25)
    player.current_room.print_all_exits_name()
    
    for item in player.current_room.items:
        print("TAKE", items[item].id.upper(), "to take", items[item].name)
        time.sleep(0.25)

    for item in player.inventory:
        print("DROP", items[item].id.upper(), "to drop your", items[item].name)
        time.sleep(0.25)

    for enemy in player.current_room.enemies:
        print("ATTACK", enemy.name.upper(), "to start a battle.")
        time.sleep(0.25)

    print("What do you want to do?")


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."""

    
    if player.current_room.is_valid_exit(direction):
        if player.current_room.all_enemies_dead():
            room = player.current_room.exits[direction]

            if room == "Queens Arcade":
                if items["room 14 key"] not in player.inventory:
                    print("Please collect the key to access room 14!")

                elif items["room 14 key"] in player.inventory:
                    player.current_room = rooms[room]

            elif room == "Cardiff Castle":
                if items["room 20 key"] not in player.inventory:
                    print("Please collect the key to access room 20!")

                elif items["room 20 key"] in player.inventory:
                    player.current_room = rooms[room]

            if room != "END":
                player.current_room = rooms[room]


            if room == "Computer Lab":
                solved = False

                player.current_room.print_room()

                scrolling_text("""In a computer lab, five students - Alex, Ben, Carol, Dave, and Emma - are working on different assignments using five different computers. Can you determine who is using which computer based on the following clues?
The computers are labelled A, B, C, D, and E in a row.
                               
Alex is not using computer C.
Dave is using computer D.
Emma is using a computer next to Ben's.
Ben is not using computer B.
Carol is using a computer on one end of the row.
Alex and Dave have 2 computers between them.
                               
What is the one-word answer to indicate who is sitting at computer A?\n""")
                
                while not solved:
                    user_input = input("> ")

                    user_input = user_input.lower()

                    if user_input == "alex":
                        solved = True

                    else:
                        print("That is wrong! Please try again.")


            if room == "Seminar Room":
                print("Press 's' to skip the scrolling text!\n")
                scrolling_text(player.current_room.dialouge)

                print("Would you like to give up (Y/N)?")
                user_input = input("> ")

                user_input = normalise_input(user_input)

                if user_input == "Y":
                    player.give_up = True
                    end_condition_met()


            if room == "Ferris Wheel":
                print("Press 's' to skip the scrolling text!\n")
                scrolling_text(player.current_room.dialouge)

            
            if room == "Queens Arcade":
                print("Press 's' to skip the scrolling text!\n")
                scrolling_text(player.current_room.dialouge)

            
            if room == "Cardiff Museum":
                scrolling_text("""In your decisions, I'm your guiding star, The path that leads you near and far. When you choose me, you'll be on track, No deviation, no looking back.
I'm the opposite of wrong, not amiss, A synonym for correct, hit or kiss. In a circle of options, I stand out, A room with a key, there's no doubt.""")


            if room == "The Earnest Willows":

                player.current_room.print_room()

                scrolling_text("""In this puzzle, I'll set the stage,
A tale of love, a desperate cage.
To rescue one, a hostage must be held,
A drastic choice, may your fears be quelled.
 
In shadows deep or daylight's gleam,
To set them free, a daring scheme.
But remember, love's the end in sight,
Who might you seize to make it right?""")

        else:
            print("Please kill all the enemies in this room!")
    

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints "You cannot take that."""
    
    taken = False
    count = 0

    while not taken:
        try:
            if item_id == items[player.current_room.items[count]].id:
                player.pick_up_item(player.current_room.items[count])
                taken = True

            elif not taken and count == len(player.current_room.items) -1:
                print("You cannot pick that up.")
                taken = True
        
            count += 1
        
        except:
            pass

        
def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."""

    dropped = False
    count = 0

    while not dropped:
        try:
            if item_id == items[player.inventory[count]].id:
                player.drop_item(player.inventory[count])
                dropped = True

            elif not dropped and count == len(player.inventory) - 1:
                print("You cannot drop that.")
                dropped = True
        
            count += 1
        
        except:
            pass
        

def execute_inspect(item_id):
    for item in player.inventory:
        if items[item].id == item_id:
            item = "This item is a", items[item].name, "and it", items[item].description
            scrolling_text(item)

def execute_attack(enemy_name):
    enemy = None
    for e in player.current_room.enemies:
        if e.name.lower() == enemy_name.lower():
            enemy = e
            break

    if enemy is None:
        print(f"No enemy named '{enemy_name}' found in this room.")
        return

    while not enemy.is_dead() and not player.is_dead():
        print(f"Your health: {player.health}")
        print(f"Enemy health: {enemy.health}\n")
        print("Your turn:")
        player.print_inventory_items()
        print("type 1 to Attack")
        print("type 2 Use Health Potion")
        player_choice = input("Choose an action: ")
        print("")

        if player_choice == "1":
            player_weapons = []
            for item in player.inventory:
                if items[item].damage_increase > 0:
                    player_weapons.append(item)
                
            weapon_string = ""
            for weapon in player_weapons:
                weapon_string += str(weapon) + ", "
            weapon_string = weapon_string[:-2]

            print("you can attack with:", weapon_string)
            attack_item = input("Choose an item to attack with: ")
            print("")
            if attack_item not in player.inventory:
                print("You do not have that item. \n")
                continue

            item = items[attack_item]
            damage = item.damage_increase + player.damage_per_hit
            print(f"You attacked with {item.name} and dealt {damage} damage.\n")
            enemy.remove_health(damage)

        if player_choice == "2":
            if "potion" in player.inventory:
                player.add_health(75)
                player.inventory.remove("potion")
                print("You used a health potion.")
            else:
                print("You don't have any health potions to use.")

        if enemy.is_dead():
            enemy_items = enemy.items
            dropped_items = ", ".join(item.upper() for item in enemy_items)
            print(f"You defeated {enemy.name}.")
            print(f"Enemy dropped: {dropped_items}")
            player.current_room.pick_up_enemy_items(enemy)
            player.add_experience(enemy)
            player.current_room.enemies.remove(enemy)
            break

        print(f"Your health: {player.health}")
        print(f"Enemy health: {enemy.health} \n")
        print(f"Enemy's turn:\n")
        time.sleep(2)
        print("")
        enemy_choice = choice(enemy.items)
        enemy_item = items[enemy_choice]
        enemy_damage = enemy_item.damage_increase + enemy.damage_per_hit
        print(f"Enemy attacked with {enemy_item.name} and dealt {enemy_damage} damage.")
        player.remove_health(enemy_damage)
        print("")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument."""

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "attack":
        if len(command) > 1:
            enemy_name = " ".join(command[1:])
            execute_attack(enemy_name)
        else:
            print("Attack what?")
    
    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])

    else:
        print("This makes no sense.")


def end_condition_met():
    win = False
    died = False

    if professor_stuart_allen_room_20.is_dead():
        scrolling_text("""\n\nAs Stuart’s weak body crumbles into ashes, beams of light twinkle around the room.
You turn your attention over to Chris, who is still chained up behind what was Stuart.
He looks at you with wide eyes - “Thank you so much for saving me! How ever will i repay you?!”
Unchaining him, he grabs your arm and you walk into the sunset, living happily ever after.\n\n""")
        win = True
    
    elif law_student_room_18.is_dead():
        scrolling_text("""\n\n“Please,” Stuart pleads, “Don’t do this Kirill.”
                       
“Release Chris and then we can talk.” You demand. 
                       
“Okay, okay… You can have Chris as long as you unchain my Mum first!” He exclaims. 

Releasing Stuart’s Mum, she crawls back over to him, thanking you feebly. 
Stuart has a look of deception in his eyes, but nonetheless, he unlocks Chris’s chains who also crawls over to you.
The air is silent in the room, with only the shuffling of the hostages piercing the silence.
Grabbing Chris’s arm, you walk out into the sun set, living happily ever after.\n""")
        win = True

    elif player.is_dead():
        scrolling_text("""\nCollapsing to the ground, you realise you have been defeated and that this is the end of you and Chris.
Your soul aches for him, feeling nothing but pain and disappointment that you could not succeed in saving him.
Finding relief in the fact that you may see him again in the afterlife, you close your eyes and let the thought of him take you away…\n\n""")
        died = True

    elif player.give_up:
        scrolling_text("""\n\nCollapsing with exhaustion, you realise that you cannot do this anymore and a wave of disappointment washes over you. 
As tears fall from your eyes, you wonder if you will ever see Chris again and if you do, will he forgive you for giving up on him? 
“Will I ever find love like that again?” You wander as Chris’s distant shouts become quieter and quieter…\n\n""")
        died = True
        
    if win:
        print("")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("                                                                                                   ")
        print("                                                                                                   ")
        print("oooooo   oooo   .oooooo.   ooooo     ooo     oooooo   oooooo     oooo ooooo ooooo      ooo      .o.")
        print(" `888.   .8'   d8P'  `Y8b  `888'     `8'      `888.    `888.     .8'  `888' `888b.     `8'      888")
        print("  `888. .8'   888      888  888       8        `888.   .8888.   .8'    888   8 `88b.    8       888")
        print("   `888.8'    888      888  888       8         `888  .8'`888. .8'     888   8   `88b.  8       Y8P")
        print("    `888'     888      888  888       8          `888.8'  `888.8'      888   8     `88b.8       `8'")
        print("     888      `88b    d88'  `88.    .8'           `888'    `888'       888   8       `888       .o.")
        print("    o888o      `Y8bood8P'     `YbodP'              `8'      `8'       o888o o8o        `8       Y8P")
        print("                                                                                                   ")
        print("                                                                                                   ")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("")

        time.sleep(10)

        sys.exit()

        
    
    if died:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("                                                                                           ")
        print("                                                                                           ")
        print("oooooo   oooo   .oooooo.   ooooo     ooo     oooooooooo.   ooooo oooooooooooo oooooooooo.  ")
        print(" `888.   .8'   d8P'  `Y8b  `888'     `8'     `888'   `Y8b  `888' `888'     `8 `888'   `Y8b ")
        print("  `888. .8'   888      888  888       8       888      888  888   888          888      888")
        print("   `888.8'    888      888  888       8       888      888  888   888oooo8     888      888")
        print("    `888'     888      888  888       8       888      888  888   888    '     888      888")
        print("     888      `88b    d88'  `88.    .8'       888     d88'  888   888       o  888     d88'")
        print("    o888o      `Y8bood8P'     `YbodP'        o888bood8P'   o888o o888ooooood8 o888bood8P'  ")
        print("                                                                                           ")
        print("                                                                                           ")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        time.sleep(10)

        sys.exit()

        

    



def scrolling_text(text):
    character_print_time = 0.025
    pressed_s = False

    for character in text:
        if keyboard.is_pressed("s"):
            pressed_s = True
            character_print_time = 0
        
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(character_print_time)

    if pressed_s:
        keyboard.press_and_release("backspace")


def menu():
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned."""

    # Display menu
    print_menu()

    # Read player's input
    user_input = input("> ")
    print("")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


# This is the entry point of our program
def main():
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        player.current_room.print_room()
        player.print_inventory_items()

        # Show the menu with possible actions and ask the player
        command = menu()

        # Execute the player's command
        execute_command(command) 

        # Check's if the any of the endings have been triggered
        end_condition_met()
        print("\n")


if __name__ == "__main__":
    main()

