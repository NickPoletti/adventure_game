import adventure_game.my_utils as utils

r11_inventory = {

}

# # # # #
# ROOM 11
#
# Serves as a good template for blank rooms
room11_description = '''
    . . .  11th room ... 
   This room seems cleaner than most and has a lone barrel in the south eastern corner. Naturally you inspect the
   contents of the barrel and see it holds a vast amount of milk. This barrel would be too heavy to lug around the
   dungeon, so you must find another way to obtain the liquid inside. There is also a door leading north.'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room11_description)

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
                next_room = 9
                done_with_room = True
            elif go_where == 'north':
                next_room = 12
                done_with_room = True
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, r11_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, r11_inventory, drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'flask':
                if utils.has_a(player_inventory, 'flask'):
                    print("You scoop the milk up into the flask and put it into your inventory")
                    player_inventory['flask'] = player_inventory['flask']-1
                    player_inventory['milk'] = player_inventory['milk']+1
                else:
                    print("You cannot use imaginary objects")
            else:
                print("Not useful in this room")
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r11_inventory)
        elif the_command == 'examine':
            print(room11_description)
        elif the_command == 'help':
            utils.player_help()
        else:
            print("The command:", the_command, "has not been implemented in Room 11")

    # END of WHILE LOOP
    return next_room