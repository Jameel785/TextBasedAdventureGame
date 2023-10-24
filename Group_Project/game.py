#This is the program which contains most of the important ascpects to the game such as the game loop

#libraries to be used in the program
#sys allows us to quit the file once the game is done and for the scrolling text
import sys

#time allows the scrolling text
import time

#required information from other programs is imported
from instance_creator import *
from items import *
from game_parser import *

skip_scrolling_text = False

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

            else:
                change_room = True

        elif room == "Cardiff Castle":
            if items["room 20 key"] not in player.inventory:
                print("Please collect the key to access room 20!")

            else:
                change_room = True
        
        elif room != "END":
            change_room = True

        if change_room:
            player.current_room = rooms[player.current_room.exits[direction]]
    

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

    elif command[0] == "crawl" and player.current_room.name == "Roald Dahl Plass":
        if len(command) == 1:
            player.current_room = rooms["The Senedd Room 1"]
        else:
            print("Crawl where?")

    else:
        print("This makes no sense.")


def end_condition_met():
    win = False

    if professor_stuart_allen_room_20.is_dead():
        print("stuart allen killed")
        win = True
    
    elif "Stuart Allen's Mum" in player.inventory:
        print("stuarts mum taken hostage")
        win = True

    elif player.is_dead():
        print("player died")

    elif player.give_up:
        print("player gave up")
        
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


def scrolling_text(text):
    if skip_scrolling_text:
        print(text)

    else:
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.025)


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

    # print("Before our text-based adventure begins, would you prefer if the text did not take so long to type out (Y/N)?")
    # scroll_text = input("> ")

    # if scroll_text == "Y":
    #     global skip_scrolling_text
    #     skip_scrolling_text = True


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

