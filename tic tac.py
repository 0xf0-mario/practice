#-------global vari-------



# Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# If game is still going
game_still_going = True

# Who Won
winner = None

# Turn?
current_player = "X"


# Display
def display_board():
    print(board[0] + " │ " + board[1] + " │ " + board[2])
    print(board[3] + " │ " + board[4] + " │ " + board[5])
    print(board[6] + " │ " + board[7] + " │ " + board[8])
# Play Game
def play_game():
    #display initial board
    display_board()

    while game_still_going:
        #hnadle a single turn of a player
        handle_turn(current_player)
        #CHECK IF THE GAME HAS ENDED
        check_if_game_over()
        #flip to the other player
        flip_player()
        #the game is ending??
    if winner == "X" or winner == "O":
        print(winner + " WON! YEAA BUDDY!")
    elif winner == None:
        print("SCRATCHHHHH. meoww")

def handle_turn(player):

    print(player + " 's turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

#amazing solution I found on google to solve the issue when a player inputted a number higher than 9 the code would break
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")


        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't do that. Go again.")

    board[position] = player

    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    #setup global varibales
    global winner
    # Check Rows
    row_win = check_rows()
    # Check Columns
    column_win = check_columns()
    # Check Diagonals
    diagonal_win = check_diagonals()
    if row_win:
        winner = row_win
       #there was a win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None
    return



def check_rows():
    #set up global vari
    global game_still_going
    #check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #Flag for win
    if row_1 or row_2 or row_3:
        game_still_going = False
        #return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    #set up global vari
    global game_still_going
    # check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # Flag for win
    if column_1 or column_2 or column_3:
        game_still_going = False
        # return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # set up global vari
    global game_still_going
    # check if any of the columns have all the same value (and is not empty)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    # Flag for win
    if diagonals_1 or diagonals_2:
        game_still_going = False
        # return the winner
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
#global variable
    global current_player
#from X to O
    if current_player == "X":
        current_player = "O"
#From O to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()





