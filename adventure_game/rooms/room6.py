import adventure_game.my_utils as utils

r6_inventory = {

}

room_state = {
    'ending_closed': True
}

# # # # #
# ROOM 6
#
# Serves as a good template for blank rooms
room6_description = '''
    . . .  6th room ... 
   Instantly you feel strange entering this mysteriously grand, yet hollow room made of marble. All of the walls are
   in perfect condition except for the western one, which is blemished by a hole the circumference of a good sized
   melon.'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room6_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    if utils.has_a(player_inventory, 'special_item'):
        if utils.has_a(player_inventory, 'special_item2'):
            if utils.has_a(player_inventory, 'special_item3'):
                print("\tA hole has opened up in the western wall and you can see the light of day."
                      "\n\tIt is apparent the end is near.")

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == 'east':
                next_room = 5
                done_with_room = True
            elif go_where == 'west':
                if utils.has_a(player_inventory, 'special_item'):
                    if utils.has_a(player_inventory, 'special_item2'):
                        if utils.has_a(player_inventory, 'special_item3'):
                            room_state['ending_closed'] = False
                            is_closed = room_state['ending_closed']
                            if not is_closed:
                                next_room = 14
                                done_with_room = True
                            else:
                                print("You cannot fit through this small of an opening.")
                        else:
                            print("You cannot fit through this small of an opening.")
                    else:
                        print("You cannot fit through this small of an opening.")
                else:
                    print("You cannot fit through this small of an opening.")
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, r6_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, r6_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r6_inventory)
        elif the_command == 'examine':
            print(room6_description)
        elif the_command == 'help':
            utils.player_help()
        else:
            print("Command not implemented in ROOM 6,", the_command)

    # END of WHILE LOOP
    return next_room