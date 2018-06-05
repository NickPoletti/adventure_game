import adventure_game.my_utils as utils

r4_inventory = {
    'key': 0
}

room_state = {
    'pitch_black': True
}


# # # # #
# ROOM 4
#
# Serves as a good template for blank rooms
room4_dim_description = '''
    . . .  4th room ... 
   You stumble in to this room due to the lack of any kind light. Your hands are not visible five inches away from your
   face. Without any sort of radiance this room will be impossible to operate in.'''

room4_lit_description = '''
    . . . 4th room . . .
    The room now radiates exposing the interior not seen before. Propped up against the corner of the room lies an empty
    sheath fit for a blade of smaller stature. Next to it a chest sits with no visible lids.  
    '''
def run_room(player_inventory):
    # Let the user know what the room looks like
    if room_state['pitch_black'] == True:
        print(room4_dim_description)
    else:
        print(room4_lit_description)

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
                    next_room = 3
                    done_with_room = True
                elif go_where == 'north':
                    next_room = 5
                    done_with_room = True
                else:
                    print('You cannot go:', go_where)
            elif the_command == 'take':
                response = utils.scrub_response(response)
                take_what = response[1]
                utils.take_item(player_inventory, r4_inventory, take_what)
            elif the_command == 'drop':
                drop_what = response[1]
                utils.drop_item(player_inventory, r4_inventory, drop_what)
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
                elif use_what == 'sword':
                    if utils.has_a(player_inventory, 'short sword'):
                        print("You put your short sword into the sheath and it fits perfectly. The chest next to it "
                                "opens and inside you can see a key.")
                        player_inventory['short sword'] = player_inventory['short sword'] - 1
                        r4_inventory['key'] = r4_inventory['key'] + 1
                    else:
                        print("You don't possess the correct item")
                else:
                    print("You need a torch to operate in this room")
            elif the_command == 'status':
                utils.player_status(player_inventory)
                utils.room_status(r4_inventory)
            elif the_command == 'examine':
                print(room4_lit_description)
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
                            print(room4_lit_description)
                        else:
                            print("The room is already lit!")
                    else:
                        print("You need a torch to operate in this room")
                else:
                    print("You cannot use that")
            elif the_command == 'examine':
                print(room4_dim_description)
            elif the_command == 'status':
                utils.player_status(player_inventory)
            elif the_command == 'go':
                go_where = response[1].lower()
                if go_where == 'south':
                    next_room = 3
                    done_with_room = True
            elif the_command == 'help':
                utils.player_help()
            else:
                print("The command:", the_command, "has not been implemented in Room 4")



    # END of WHILE LOOP
    return next_room
