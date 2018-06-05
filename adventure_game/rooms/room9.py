import adventure_game.my_utils as utils

r9_inventory = {

}

# # # # #
# ROOM 9
#
# Serves as a good template for blank rooms
room9_description = '''
    . . .  9th room ... 
   Another empty room with three doors and a sense of loneliness. You start to wonder if there even is another living 
   soul in this god forsaken dungeon full of ridiculous puzzles. Luckily, none of the doors (eastern, western, southern)
   are locked.'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room9_description)

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
            if go_where == 'east':
                next_room = 11
                done_with_room = True
            elif go_where == 'west':
                next_room = 3
                done_with_room = True
            elif go_where == 'south':
                next_room = 10
                done_with_room = True
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, r9_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, r9_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r9_inventory)
        elif the_command == 'examine':
            print(room9_description)
        elif the_command == 'help':
            utils.player_help()
        else:
            print("The command:", the_command, "has not been implemented in Room 9")

    # END of WHILE LOOP
    return next_room