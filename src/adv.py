from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Gilderoy', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# I didn't see that we were supposed to instantiate the player outside the loop so I created this first
# player_name_in = input("player_name>")

# print("Welcome to Matt's Adventure Game \n Please create your player by entering a name")

# if player_name_in:
#     compass_in = input("directions>")
#     player1 = Player(f"{player_name_in}")
#     print(f"Welcome {player1.name}")
#     if player1.current_room == 'outside':
#         print()
turn_off = False

while not turn_off:

    print(f"{player1.current_room.name}")
    print(f"{player1.current_room.description}")

    compass_in = input("directions>")
    # print(f"Welcome brave {player1.name}, to Matt's Adventure Game\n to progress enter the direction you would like to go")
    if compass_in == 'n':  
        if player1.current_room.n_to == None:
            print("You can't go that way! Try again!")
            player1.current_room
        else:
            player1.current_room = player1.current_room.n_to
    elif compass_in == 's':
        if player1.current_room.s_to == None:
            print("You can't go that way! Try again!")
            player1.current_room
        else:
            player1.current_room = player1.current_room.s_to
    elif compass_in == 'e':
        if player1.current_room.e_to == None:
            print("You can't go that way! Try again!")
            player1.current_room
        else:
            player1.current_room = player1.current_room.e_to
    elif compass_in == 'w':
        if player1.current_room.w_to == None:
            print("You can't go that way! Try again!")
            player1.current_room
        else:
            player1.current_room = player1.current_room.w_to

        # if player1.current_room = room[""]
    elif compass_in == 'q':
        print("Game Over!")
        turn_off = True
    


        



