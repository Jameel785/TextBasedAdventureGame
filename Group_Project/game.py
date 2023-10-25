#This is the program which contains most of the important ascpects to the game such as the game loop

#libraries to be used in the program
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
    time.sleep(0.5)
    player.current_room.print_all_exits_name()
    
    for item in player.current_room.items:
        print("TAKE", items[item].id.upper(), "to take", items[item].name)
        time.sleep(0.5)

    for item in player.inventory:
        print("DROP", items[item].id.upper(), "to drop your", items[item].name)
        time.sleep(0.5)

    for enemy in player.current_room.enemies:
        print("ATTACK", enemy.name.upper(), "to start a battle with")
        time.sleep(0.5)

    if player.current_room.name == "Roald Dahl Plass":
        print("CRAWL to", rooms["The Senedd Room 1"].name.upper() + ".")
    print(" ")

    print("What do you want to do?")


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."""

    
    if player.current_room.is_valid_exit(direction):
        room = player.current_room.exits[direction]
        change_room = False

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
        print(f"Player health: {player.health}")
        print(f"Enemy health: {enemy.health}")
        print("Your turn!")
        player.print_inventory_items()
        print("type 1 to Attack")
        print("type 2 Use Health Potion")
        player_choice = input("Choose an action: ")

        if player_choice == "1":
            print(player.inventory)
            attack_item = input("Choose an item to attack with: ")
            if attack_item not in player.inventory:
                print("You dont have that item")
                continue

            item = items[attack_item]
            damage = item.damage_increase
            print(f"You attacked with {item.name} and dealt {damage} damage.")
            enemy.remove_health(damage)

        if player_choice == "2":
            print(player.inventory)
            if "potion" in player.inventory:
                player.add_health(35)
                print("You used a health potion.")
            else:
                print("You don't have any health potions to use.")

        if enemy.is_dead():
            print(f"You defeated {enemy.name}.")
            player.current_room.pick_up_enemy_items()


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

    else:
        print("This makes no sense.")


def end_condition_met():
    win = False
    died = False

    if professor_stuart_allen_room_20.is_dead():
        print("stuart allen killed")
        win = True
    
    elif "Stuart Allen's Mum" in player.inventory:
        print("stuarts mum taken hostage")
        win = True

    elif player.is_dead():
        print("player died")
        died = True

    elif player.give_up:
        print("player gave up")
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

        sys.exit()



def scrolling_text(text):
    character_print_time = 0.025

    for character in text:
        if keyboard.is_pressed("s"):
            character_print_time = 0
        
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(character_print_time)

def class_choice():
    while True:
        print("Chose your class:")
        print("type WARRIOR to select the warrior Kirill. High damage, low health, low xp")
        print("type WIZARD to select the wizard Kirill. Low damage, low health, high xp")
        print("type BIG to select the big Kirill. Low damage, high health, low xp")
        print("type CHALLENGE to select the challenge mode. Low damage, low health, low xp")
        choice = input ("> ")
        normal_choice: normalise_input(choice)
        if normal_choice == "warrior":
            break

        elif normal_choice == "wizard":
            break

        elif normal_choice == "big":
            break
            
        elif normal_choice == "challenge":
            break
        
        else:
            print("invalid input")

    blah blah blah



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
    class_choice()
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

