# Roxana Reed

# varialbe declaraions
ROOMS = {
    'Dressing Room': {'East': 'Bedroom', 'South': 'Courtyard'},
    'Bedroom': {'South': 'Dining Room', 'West': 'Dressing Room'},
    'Dining Room': {'North': 'Bedroom', 'South': 'Office'},
    'Office': {'North': 'Dining Room', 'West': 'Courtyard'},
    'Courtyard': {'East': 'Office', 'North': 'Dressing Room', 'West': 'Stable', 'South': 'Chapel'},
    'Stable': {'East': 'Courtyard'},
    'Crypt': {'East': 'Chapel'},
    'Chapel': {'North': 'Courtyard', 'West': 'Crypt', 'East': 'Armory'},
    'Armory': {'West': 'Chapel'}
}

ITEMS_TO_COLLECT = {
    'Dressing Room': 'mirror',
    'Dining Room': 'garlic',
    'Bedroom': 'cross',
    'Office': 'knife',
    'Chapel': 'water',
    'Armory': 'stake',
    'Stable': 'horse'
}
INVENTORY = []
CURRENT_ROOM = 'Dressing Room'
DIRECTIONS = ['North', 'South', 'East', 'West']
EXIT_COMMAND = "Exit"
DRACULA = ""

# display the game rules


def displayRules():
    print('Welcome to the Dracula game! Please enter a direction to move between rooms or Exit to stop the game.')
    print("Collect 6 items to kill Dracula, or he will bring death to the English countryside.")
    print("Move commands: South, North, East, West")
    print("Add to Inventory: get 'item name'")
    print('---------------------------')

# display the current room and items available in that room


def displayRoomAndItems():
    print(f'You are in the {CURRENT_ROOM}.')
    print(f'Inventory: {INVENTORY}')

    if CURRENT_ROOM in ITEMS_TO_COLLECT:
        print(f'You see the {ITEMS_TO_COLLECT[CURRENT_ROOM]}.')
        print('------------')
    else:
        print('Nothing to collect in this room.')
        print('------------')

# kill Dracula and win, or lose if not all inventory items are collected


def endGame():
    global DRACULA
    items = list(ITEMS_TO_COLLECT.values())

    print("You're in the Crypt!")
    new_inv = []
    for value in ITEMS_TO_COLLECT.values():
        if value in INVENTORY:
            new_inv.append(value)
    if len(new_inv) == len(items):
        print("You killed Dracula!")
        DRACULA = "KILLED"
    else:
        print('Dracula killed you and he will now kill the English countryside!')
    return "Exit"

# move player room based on game map


def changePlayerRoom(direction):
    global ROOMS
    global CURRENT_ROOM

    # check if there is a room in the specified direction
    if direction in ROOMS[CURRENT_ROOM]:
        CURRENT_ROOM = ROOMS[CURRENT_ROOM][direction]

        # check if this is Dracula's room
        if CURRENT_ROOM == 'Crypt':
            endGame()

    # error handling
    else:
        print("There is nothing in that direction!")
        print("-----------------------------------")
    # return the player state
    return CURRENT_ROOM

# collect inventory object availabe in current room


def collect_inventory(collect_item):
    global ITEMS_TO_COLLECT
    global INVENTORY

    item = collect_item.split()

    if item[1] in ITEMS_TO_COLLECT.values():
        if item[1] not in INVENTORY:
            INVENTORY.append(item[1])
        else:
            print('You already have this object!')
    else:
        print('Invalid inventory object.')

# main function


def main():
    displayRules()

    while True:
        displayRoomAndItems()
        if DRACULA != "KILLED":
            user_move = input('Enter your move:\n\n')
        else:
            break
        if user_move == EXIT_COMMAND:
            break
        elif user_move in DIRECTIONS:
            changePlayerRoom(user_move)
        elif user_move.startswith('get '):
            collect_inventory(user_move)
        else:
            print('Please enter a valid move.')


main()
