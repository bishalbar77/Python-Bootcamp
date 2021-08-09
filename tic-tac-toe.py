'''
Steps followed:
1. Board Design
2. Update board (User input on board)
3. Play game
4. Handle player (switch between X and O)
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
# Access a index position in list
students =  ["Rohan", "Subham" , "Aditya", 'John', "Rutuja" ] # List Variable
students[2] = "Manoj"
print(students)

# Design the board
board = [
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"
        ]
# userInput = int(input())
# board[userInput - 1] = "X"

has_won = None  # To store the winner name

# Display the board with updated user input
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "    1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "    4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "    7 | 8 | 9")
    print("\n")

def handle_player():
    return

def check_if_game_over():
    return

def flip_player():
    return

def play_game():
    display_board()
    handle_player()
    check_if_game_over()
    flip_player()

    if has_won == "X" or has_won == "O":
        print("Our winner is "+has_won)
    elif has_won == None:
        print("Game Tie")
