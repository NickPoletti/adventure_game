import adventure_game.my_utils as utils

r14_inventory = {

}

# # # # #
# ROOM 14
#
# Serves as a good template for blank rooms
room14_description = '''
    . . .  Exit ... 
   You have done it. You can feel the warm sunlight on your skin, the cool breeze running through your hair, and the
   overwhelming joy of leaving that smelly,dark abomination of a dungeon behind you. There is nothing left to do,but 
   chose something better to do than navigating bleak hallways and absurd obstacles.
   
   
                                Game Complete'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room14_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -5

    done_with_room = True
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == 'east':
                next_room = 6
                done_with_room = True
            else:
                print('You cannot go:', go_where)
        else:
            print("The command:", the_command, "has not been implemented in Room 14")

    # END of WHILE LOOP
    return next_room