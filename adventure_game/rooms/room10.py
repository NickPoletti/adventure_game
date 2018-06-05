import adventure_game.my_utils as utils

r10_inventory = {
    'key': 0,
    'cake': 0,
    'milk': 0
}

room_state = {
    'empty': False
}
# # # # #
# ROOM 10
#
# Serves as a good template for blank rooms
room10_initial_description = '''
    . . .  10th room ... 
   You hear a noise that is unmistakable, another human voice. Turning to your right you observe this old fellow lying
   against the western wall trying to get your attention. "My friend" He exclaims in a tired fashion "Have you anything
   to drink and eat." By the looks of him you can guess he hasn't feasted for many nights and you feel sorry for his
   withering form. "If you can provide me with what I need I might be able to benefit you in return."'''

room10_finished_description = '''
    . . . 10th room . . .
    The old man is gone and all is quiet within this room'''


def run_room(player_inventory):
    # Let the user know what the room looks like
    if room_state['empty'] == False:
        print(room10_initial_description)
    else:
        print(room10_finished_description)

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
            if go_where == 'north':
                if utils.has_a(r10_inventory, 'cake'):
                    if utils.has_a(r10_inventory, 'milk'):
                        print('"Wait adventurer" says the old man in a panicked fashion "Do not forgot your reward."'
                              '\nHe reaches into this robes and pulls out a key, but soon drops it to finish his tasty'
                              '\ntreat. "It is yours" He proceeds "I have no need for it anymore"')
                        r10_inventory['key'] = r10_inventory['key']+1
                        r10_inventory['cake'] = r10_inventory['cake']-1
                        r10_inventory['milk'] = r10_inventory['milk']-1
                        empty = room_state['empty']
                        if empty == False:
                            room_state['empty'] = True
                    else:
                        next_room = 9
                        done_with_room = True
                else:
                    next_room = 9
                    done_with_room = True
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, r10_inventory, take_what)
        elif the_command == 'drop':
            response = utils.scrub_response(response)
            drop_what = response[1]
            utils.drop_item(player_inventory, r10_inventory, drop_what)
            if drop_what == 'cake':
                print('"Thank you kind person" the old man says')
            if drop_what == 'milk':
                print('"Thank you kind person" the old man says')
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(r10_inventory)
        elif the_command == 'examine':
            print(room10_initial_description)
        elif the_command == 'help':
            utils.player_help()
        else:
            print("The command:", the_command, "has not been implemented in Room 10")

    # END of WHILE LOOP
    return next_room