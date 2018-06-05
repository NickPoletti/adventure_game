import adventure_game.my_utils as utils

r3_inventory = {

}

room_state = {
    'door_locked': True
}
# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room3_description = '''
    . . .  3rd room ... 
    A junction! You are aware that this is the room that connects all of the dungeon branches together. Besides from 
    being the central hub this room seems to serve no other significance as it is rather empty. To the NORTH there is a 
    door as well as the EAST and the WEST. Sadly, the eastern door is locked.'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room3_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == 'west':
                next_room = 1
                done_with_room = True
            elif go_where == 'north':
                next_room = 4
                done_with_room = True
            elif go_where == 'east':
                is_locked = room_state['door_locked']
                if not is_locked:
                    next_room = 9
                    done_with_room = True
                else:
                    print("Key required to open locked door.")
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, r3_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, r3_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r3_inventory)
        elif the_command == 'examine':
            print(room3_description)
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
        elif the_command == 'help':
            utils.player_help()
        else:
            print("The command:", the_command, "has not been implemented in Room 3")

    # END of WHILE LOOP
    return next_room
