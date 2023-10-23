#This is the program which contains most of the important ascpects to the game such as the game loop

from map import rooms
from player import *
from items import *
from game_parser import *
from enemies import *


def print_menu():
    """This function displays the menu of available actions to the player."""

    print("You can:")
    player.current_room.print_all_exits_name()
    
    for item in player.current_room.items:
        print("TAKE", item.id.upper(), "to take a", item.name)

    for item in player.inventory:
        print("DROP", item.id.upper(), "to drop your", item.name)
    print(" ")

    print("What do you want to do?")


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."""

    
    if player.current_room.is_valid_exit(direction):
        player.current_room = rooms[player.current_room.exits[direction]]
    

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints "You cannot take that."""
    
    taken = False
    for item in player.current_room.items:
        if item_id == item.id:
            player.pick_up_item(item)
            taken -= True

    if taken == False:
        print("You cannot take that.")

        
def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."""

    picked_up = False
    for item in player.inventory:
        if item_id == item.id:
            player.current_room.items.append(item)
            player.drop_item(item)
            picked_up = True

    if picked_up:
        print("You cannot drop that.")
    
    

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

    else:
        print("This makes no sense.")


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

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def win_condition_met():
    pass

# This is the entry point of our program
def main():

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        player.current_room.print_room()
        player.print_inventory_items()

        # Show the menu with possible actions and ask the player
        command = menu(player.current_room.exits, player.current_room.items)

        # Execute the player's command
        execute_command(command)

        if win_condition_met():
            break

    print("YOU WIN!!")



if __name__ == "__main__":
    main()

