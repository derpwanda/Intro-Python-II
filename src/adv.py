from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Item("kerosene lamp", "old and rusty"),Item("pickaxe", "suprisingly new")]),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# this line creates a Player object that required a name and room.
# the room is from the dictionary above, referencing the 'outside' room
# whose value is a room created the Room class which includes the name,
# description and empty item list.
player = Player('Wanda', room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the player enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True: # will run until it hits the return or break statement
    print(f"{player.p_name} is in: {player.p_room.r_name}")
    print(f"{player.p_room.r_description}")

    if player.p_room.items:
        print(f"Here are the items in {player.p_room.r_name}:")
        for item in player.p_room.items:
            print(f"   {item.iname}")
    else:
        print("There are no items in this room!")

    print("\nIn which direction would you like to go?:")
    playermove = input("[n]orth [s]outh [e]ast [w]est: ")

    if playermove == 'n':
        player.p_room = player.p_room.n_to
    elif playermove == 'e':
        player.p_room = player.p_room.e_to
    elif playermove == 's':
        player.p_room = player.p_room.s_to
    elif playermove == 'w':
        player.p_room = player.p_room.w_to
    elif player.p_room == None:
        print('No')





print(f"{player.p_room.r_name} holds list:{player.p_room.items}")
print(player)
