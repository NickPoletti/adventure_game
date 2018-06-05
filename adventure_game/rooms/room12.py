import adventure_game.my_utils as utils

r12_inventory = {

}

room_state = {
    'pitch_black': True,
    'door_locked': True
}
# # # # #
# ROOM 12
#
# Serves as a good template for blank rooms
room12_dim_description = '''
    . . .  12th room ... 
   Alas, you have encountered another dark room. You know what you must do.'''

room12_lit_description = '''
    . . . 12th room . . .
    For the most part this room seems untouched and unused. It is almost like no one has ever gone into this room, which
    frightens and excites you simultaneously. There is a single door leading to the east, but it requires a key. '''

def run_room(player_inventory):
    # Let the user know what the room looks like
    if room_state['pitch_black']:
        print(room12_dim_description)
    else:
        print(room12_lit_description)

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
        if room_state['pitch_black'] == False:
            if the_command == 'go':
                go_where = response[1].lower()
                if go_where == 'south':
                    next_room = 11
                    done_with_room = True
                elif go_where == 'east':
                    is_locked = room_state['door_locked']
                    if not is_locked:
                        next_room = 13
                        done_with_room = True
                    else:
                        print("Key required to open locked door.")
                else:
                    print('You cannot go:', go_where)
            elif the_command == 'take':
                response = utils.scrub_response(response)
                take_what = response[1]
                utils.take_item(player_inventory, r12_inventory, take_what)
            elif the_command == 'drop':
                drop_what = response[1]
                utils.drop_item(player_inventory, r12_inventory, drop_what)
            elif the_command == 'use':
                use_what = response[1]
                if use_what == 'torch':
                    if utils.has_a(player_inventory, 'torch') == True:
                        pitch_black = room_state['pitch_black']
                        if pitch_black:
                            room_state['pitch_black'] = False
                            print("The room is filled with bright light!")
                        else:
                            print("The room is already lit!")
                elif use_what == 'key':
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
                else:
                    print("You need a torch to operate in this room")
            elif the_command == 'status':
                utils.player_status(player_inventory)
                utils.room_status(r12_inventory)
            elif the_command == 'examine':
                print(room12_lit_description)
            elif the_command == 'help':
                utils.player_help()
            else:
                print("The command:", the_command, "has not been implemented in Room 4")
        else:
            if the_command == 'use':
                use_what = response[1]
                if use_what == 'torch':
                    if utils.has_a(player_inventory, 'torch') == True:
                        pitch_black = room_state['pitch_black']
                        if pitch_black:
                            room_state['pitch_black'] = False
                            print("The room is filled with bright light!")
                            player_inventory['torch'] = player_inventory['torch'] - 1
                            print(room12_lit_description)
                        else:
                            print("The room is already lit!")
                    else:
                        print("You need a torch to operate in this room")
                else:
                    print("You cannot use that")
            elif the_command == 'examine':
                print(room12_dim_description)
            elif the_command == 'status':
                utils.player_status(player_inventory)
            elif the_command == 'go':
                go_where = response[1].lower()
                if go_where == 'south':
                    next_room = 11
                    done_with_room = True
            elif the_command == 'help':
                utils.player_help()
            else:
                print("The command:", the_command, "has not been implemented in Room 12")

    # END of WHILE LOOP
    return next_room