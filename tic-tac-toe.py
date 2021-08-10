'''
Steps followed:
1. Board Design
2. Update board (User input on board)
3. Play game
4. Handle turn (switch between X and O)
5. Check if game is over - Who wins
    - check for rows
    - check for column
    - check for diagonal
6. Check for Tie
7. Flip Player
8. Back to 2

Starting point computer case => 0
Instead of 1
'''
# Type Casting - Converting one data type into another
# Access a index position in list
# students =  ["Rohan", "Subham" , "Aditya", 'John', "Rutuja" ] # List Variable
# students[2] = "Manoj"
# print(students)
# userInput = int(input())
# board[userInput - 1] = "X"


'''Tic Tac Toe'''
# Design the board
board = [
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"
        ]

has_won = None  # To store the winner name

game_is_still_going = True  # To check if the game is still going on

current_player = "X"  #  To store the current player
  
# Display the board with updated user input
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "    1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "    4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "    7 | 8 | 9")
    print("\n")

# Check if current user has valid input or not 
def handle_turn(player):

    print(player + "'s turn")
    position = input("Choose a position between (1-9): ")

    # Check if input is valid
    valid = False
    while not valid:

        # Check if position is between 1 - 9
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Not valid postion! Please choose another position between (1-9): ")
        
        position = int(position) - 1

        # Check whether there is some input in that position or not
        if(board[position] == "-"):
            valid = True
        else:
            print("You can't overwrite a position!")

    board[position] = player
    display_board()

# Check if game over
def check_if_game_over():
    check_if_win()
    check_if_tie()

# Check if there is tie
def check_if_tie():
    return

# Check if someone won
def check_if_win():
    return

# Flip the current player to next player
def flip_player():
    # Call Global variable
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

# Play the game
def play_game():
    display_board()
    
    # To check if the game is still running
    while game_is_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if has_won == "X" or has_won == "O":
        print("Our winner is "+has_won)
    elif has_won == None:
        print("Game Tie")

play_game()