#Roxana Reed

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {

        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }
CURRENT_ROOM = 'Great Hall'
DIRECTIONS = ['North', 'South', 'East', 'West']
EXIT_COMMAND = "Exit"

# display the game rules
def displayRules():
    print('Welcome to the Rooms game! Please enter a direction ( North, South, East, or West ) to move between rooms or Exit to stop the game.')

# move player location
def changeLocation(direction):
    global rooms
    global CURRENT_ROOM
    
    # check if there is a room in the specified direction
    if direction in rooms[CURRENT_ROOM]:
        CURRENT_ROOM = rooms[CURRENT_ROOM][direction]

    # error handling
    else:
        print("There is nothing in that direction!")

    # return the player state
    return CURRENT_ROOM

def main():
    displayRules()

    while True:
        print(f'You are in the {CURRENT_ROOM}.')
        print('----------------------------\n')
        user_move = input('Please enter a direction:')
        if user_move == EXIT_COMMAND:
            break 
        elif user_move in DIRECTIONS:
            changeLocation(user_move)
        else:
            print('Please enter a valid move.')

main()