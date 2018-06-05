import adventure_game.my_utils as utils

r13_inventory = {

}

# # # # #
# ROOM 13
#
# Serves as a good template for blank rooms
room13_description = '''
    . . .  13th room ... 
   For some reason this room fills you with a seen of pride and accomplishment. The walls of give of a calming vibe due 
   to their conform smoothness and polished stone grey color. While scanning the room you are surprised to see a button 
   on the ground rather than on the wall. Besides the door you came the room travels no further in any direction.'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room13_description)

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
                next_room = 12
                done_with_room = True
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, r13_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, r13_inventory, drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'button':
                player_inventory['special_item3'] = 7
                print("The button is pressed")
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r13_inventory)
        elif the_command == 'examine':
            print(room13_description)
        elif the_command == 'help':
            utils.player_help()
        else:
            print("The command:", the_command, "has not been implemented in Room 13")

    # END of WHILE LOOP
    return next_room