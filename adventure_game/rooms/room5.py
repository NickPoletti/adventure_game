import adventure_game.my_utils as utils

r5_inventory = {

}

# # # # #
# ROOM 5
#
# Serves as a good template for blank rooms
room5_description = '''
    . . .  5th room ... 
   You enter another lack luster room with four walls of stone surrounding you. The only point of interest is another
   stone button on the northern wall pushed out from it.'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room5_description)

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
            if go_where == 'south':
                next_room = 4
                done_with_room = True
            elif go_where == 'west':
                next_room = 6
                done_with_room = True
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, r5_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, r5_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r5_inventory)
        elif the_command == 'examine':
            print(room5_description)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'button':
                player_inventory['special_item2'] = 7
                print("The button is pressed")
        elif the_command == 'help':
            utils.player_help()
        else:
            print("The command:", the_command, "has not been implemented in Room 5")

    # END of WHILE LOOP
    return next_room