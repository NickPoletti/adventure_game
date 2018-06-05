import adventure_game.my_utils as utils

from colorama import Fore, Style

r1_inventory = {

}

room_state = {
    'door_locked': True
}

# # # # # # # # # # # # # # #
#  This is the main room you will start in.
#
#  GO: From this room you can get to Room 2 (SOUTH) and Room 1 (East)
#  Take: There is nothing to take in this room
#  Use: There is nothing to use in this room
#
def run_room(player_inventory):
    room1_description = '''
    . . . Main Room . . .
    You open your eyes. The room you see is musty and dank. You look around and see a brightly lit
    doorway to the SOUTH as well as a closed door with a small keyhole To the EAST. Inside this room is nothing
    to pick up, but you scan and see a rather large button is protruding in the northern wall. 

    '''
    print(room1_description)
    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'south':
                next_room = 2
                done_with_room = True
            elif direction == 'east':
                is_locked = room_state['door_locked']
                if not is_locked:
                    next_room = 3
                    done_with_room = True
                else:
                    print("Key required to open locked door.")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, r1_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, r1_inventory, drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'key':
                if utils.has_a(player_inventory, 'key') == True:
                    door_locked = room_state['door_locked']
                    if door_locked:
                        room_state['door_locked'] = False
                        print("The door to the EAST is unlocked!")
                        player_inventory['key'] = player_inventory['key'] - 1
                    else:
                        print("The door was already unlocked!")
                else:
                    print("You need a key to open this door")
            if use_what == 'button':
                player_inventory['special_item'] = 7
                print("The button is pressed")
        elif the_command == 'examine':
            print(room1_description)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r1_inventory)
        elif the_command == 'help':
            utils.player_help()
        else:
            print("Command not implemented in ROOM 1,", the_command)

    # end of while loop
    return next_room
