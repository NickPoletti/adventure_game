import adventure_game.my_utils as utils

r7_inventory = {
    "golden goblet": 1,
    "torch": 1
}


# # # # #
# ROOM 7
#
# Serves as a good template for blank rooms
room7_description = '''
    . . .  7th room ... 
   You enter what seems to be a treasure room. This room has a high ceiling as well as pillars made of a particularly 
   shiny metal that has partial rusted away. In the center of the room lies a stone pedestal with a golden goblet rested
   atop. The room is lit by a singular torch on the western wall.'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room7_description)

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
                next_room = 8
                done_with_room = True
            elif go_where == 'north':
                if utils.has_a(player_inventory, 'golden goblet') == True:
                    print("The door is slammed shut")
                else:
                    next_room = 2
                    done_with_room = True
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, r7_inventory, take_what)
            if take_what == 'golden goblet':
                print("The door suddenly slams to the north!")
        elif the_command == 'drop':
            response = utils.scrub_response(response)
            drop_what = response[1]
            utils.drop_item(player_inventory, r7_inventory, drop_what)
            if drop_what == 'golden goblet':
                print("The door to the north swings back open!")
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r7_inventory)
        elif the_command == 'examine':
            print(room7_description)
        elif the_command == 'help':
            utils.player_help()
        else:
            print("The command:", the_command, "has not been implemented in Room 7")

    # END of WHILE LOOP
    return next_room