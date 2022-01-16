'''
Solo Checkpoint 02
Author: Bro. Hayes
'''


def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    global game
    global board
    print("Welcome to this TicTacToe!")
    question = input(
        "If you would like to start type 'Y' and if not, type 'N': ")
    if question.lower() == "y":
        while game:
            display_board(board)
            player_choice(board)
            next_player()
            is_draw(board)
            is_winner()
        display_board(board)
        print("That was fun! Thank you for playing TicTacToe!")
    else:
        print("Thank you for visiting! We hope you'll be back!")


# global variable so I can use it in functions
# create the board list
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player = "X"
winner = " "
game = True

# display the game board


def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

# User input

# def make_move(player, board):
#     ''' Prompts player to select a square to play
#         Assigns the player to that board location if it is a legal move
#         return: None
#     '''


def player_choice(board):
    choice = int(input("It's your turn! Choose between 1-9: "))
    if choice >= 1 and choice <= 9 and board[choice-1] == "-":
        board[choice-1] = player
    else:
        print("This spot is already taken! ")


# Check all the rows, columns and diagonals for winning.
def column(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


# def is_draw(board):
# if there are no longer any space to add it is a tie and game should be False to stop the game
def is_draw(board):
    global game
    global winner
    if "-" not in board:
        display_board(board)
        print("It is a tie! We have no Winner")
        winner = None
        game = False


# def is_winner(board):
#     ''' return: True if someone won, False if there is no winner '''
# Compare all the three parts and if it is true, game is False to end the game
def is_winner():
    global game
    if diag(board) or column(board) or row(board):
        print(
            f"We have a WINNER!!!! Congratulations {winner}, you are the Winner!")
        game = False

# def next_player(current):
#     ''' return: x if current is o, otherwise x '''


def next_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# run main if this has been called from the command line
if __name__ == "__main__":
    main()
