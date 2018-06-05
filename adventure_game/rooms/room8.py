import adventure_game.my_utils as utils

r8_inventory = {
    "cake": 1
}

# # # # #
# ROOM 8
#
# Serves as a good template for blank rooms
room8_description = '''
    . . .  8th room ... 
   As you enter this tiny room you can't help but notice the wonderful smell emitting from the back. You look up and 
   focus your eyes on a beautiful cake. Your stomach growls but you are weary of what the dessert contains.'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room8_description)

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
                next_room = 7
                done_with_room = True
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, r8_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, r8_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r8_inventory)
        elif the_command == 'examine':
            print(room8_description)
        elif the_command == 'help':
            utils.player_help()
        else:
            print("The command:", the_command, "has not been implemented in Room 8")

    # END of WHILE LOOP
    return next_room