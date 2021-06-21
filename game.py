
# TIC TAC TOE
import boar as boar

board =["-" ,"-" ,"-",
       "-" ,"-" ,"-",
       "-" ,"-" ,"-",]

currentplayer = "X"

gameisgoing =True

winner =None

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turns():
    global  gameisgoing
    position =int(input("Enter the position number:")  )  # 3
    board[position] = currentplayer

    # if board[position]!="-":
    #   gameisgoing=False


def swap_players():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    elif currentplayer == "O":
        currentplayer = "X"



def check_who_is_the_winner():
    global winner
    rowwinner =check_row()
    colwinner =check_column()
    diawinner =check_dia()
    check_draw()

    if rowwinner:
        winner =rowwinner
    elif colwinner:
        winner =colwinner
    elif diawinner:
        winner =diawinner



def check_row():
    global gameisgoing
    row1 = board[0] == board[1] == board[2] != "-  "  # empty
    row2 = board[3] == board[4] == board[5] != "-  "  # X
    row3 = board[6] == board[7] == board[8] != "-  "  # empty

    if row1 or row2 or row3:
        gameisgoing =False


    if row1  :  # inside row1 variable if something is present
        return board[2]
    elif row2:
        return board[5]

    elif row3:
        return board[6]



def check_column():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "-"  # empty
    col2 = board[1] == board[4] == board[7] != "-"  # empty
    col3 = board[2] == board[5] == board[8] != "-"  # X

    if col1 or col2 or col3:
        gameisgoing = False

    if col1:  # inside row1 variable if something is present
        return board[6]
    elif col2:
        return board[1]

    elif col3:
        return board[5]


def check_dia():
    global gameisgoing
    dia1 = board[0] == board[4] == board[8] != "-"  # empty
    dia2 = board[2] == board[4] == board[6] != "-"  # empty


    if dia1 or dia2:
        gameisgoing = False

    if dia1:  # inside row1 variable if something is present
        return board[4]
    elif dia2:
        return board[6]


def check_draw():
    global gameisgoing
    if board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] != "-":
        gameisgoing =False
        print("Match is Drawn")



def play_game():
    global gameisgoing
    while gameisgoing:
        display_board()

        handle_turns()

        swap_players()

        check_who_is_the_winner()

    if winner == "X":
        print("X is the winner")
    elif winner == "O":
        print("O is the winner")


play_game()