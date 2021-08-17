'''Tic Tac Toe'''

board = [
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"
        ]

is_won = None  

game_is_still_going = True  

current_player = "M"  
  

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "    1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "    4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "    7 | 8 | 9")
    print("\n")

def handle_turn(player):

    print(player + "'S turn")
    position = input("Choose a number between (1-9): ")

    
    valid = False
    while not valid:

        
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Not valid postion! Please choose another position between (1-9): ")
        
        position = int(position) - 1

    
        if(board[position] == "-"):
            valid = True
        else:
            print("This number is already taken")

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_tie():
    global game_is_still_going
    if "-" not in board:
        game_is_still_going = False
        return True
    else:
        return False


def check_if_win():
   
    global is_won

  
    row_winner = check_row_winner()
    
    column_winner = check_column_winner()
 
    diagonal_winner = check_diagonal_winner()

 
    if row_winner:
        is_won = row_winner
    elif column_winner:
        is_won = column_winner
    elif diagonal_winner:
        is_won = diagonal_winner
    else:
    
        is_won = None


def check_row_winner():
    global game_is_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
def check_column_winner():
    global game_is_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_is_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

def check_diagonal_winner():
    global game_is_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_is_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None
    

def flip_player():
   
    global current_player

    if current_player == "M":
        current_player = "K"
    elif current_player == "K":
        current_player = "M"
        
def play_game():
    display_board()
  
    while game_is_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if is_won == "M" or is_won == "K":
        print("The  winner is "+is_won)
    elif is_won == None:
        print("Game has  Tie")

play_game()