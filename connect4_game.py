import sys
from termcolor import colored

""" 
def draw_board2(board):
    for podlista in board:
        print("|", end=" ")
        for i in podlista:
            print(i, end=" ")
        print("| ")
    print("| " * 5, end=" ")
    print("")
    (board[0])[1]


def draw_board1(board):
    for row in board:
        print("|", end=" ")
        for column in row:
            print(column, end=" ")
        print(("| "))
    print("| " * 7, end=" ")
    print("")
"""


def draw_board(board):
    for row in range(len(board)):
        print("|", end="")
        for column in range(len(board[row])):
            print(board[row][column], end="")
        print("|")
    print(colored("-" * 9,  'green'))
    print("")


def drop_disc_in_column(selected_column, board, user):
    empty_row = 0
    for row in range(len(board)):
        if board[row][selected_column] == "*":
            empty_row = row
        else:
            break
    board[empty_row][selected_column] = user
    return board


test_board = [["*", "*", "*", "*", "*", "*", "*"],
             ["*", "*", "*", "*", "*", "*", "*"],
             ["*", "*", "*", 2, "*", "*", "*"],
             ["*", "*", "*", 2, "*", 2, "*"],
             ["*", "*", "*", 2, "*", 2, "*"],
             [2,    2,   1,  2,  2,  2,  2]]

#print(drop_disc_in_column(2, test_board, 1))


def check_row_of_last_move(board, selected_column, user):
    row_index = 0
    for row in range(len(board)):
        if board[row][selected_column] == "*":
            row_index = row + 1
    return row_index

#print(check_row_of_last_move(test_board, 5, 2))


def is_vertical_four_in_line(board, selected_column, user):
    win_counter = 0
    for row in range(len(board)):
        if board[row][selected_column] == user:
            win_counter = win_counter + 1
    if win_counter >= 4:
        return True



def is_horizontal_four_in_line(board, selected_column, user):
    win_counter = 0
    last_move_row_index = check_row_of_last_move(board, selected_column, user)
    for column in range(len(board[last_move_row_index])):
        if board[last_move_row_index][column] == user:
            win_counter = win_counter + 1
        else:
            win_counter = 0
    if win_counter >= 4:
        return True

#print(is_vertical_four_in_line(test_board, 3, 2))


def check_winner(board, selected_column, user):
    if is_horizontal_four_in_line(board, selected_column, user) is True or is_vertical_four_in_line(board, selected_column, user) is True:
        print("Congrats you won player:", user)
    return

#print(is_vertical_four_in_line(test_board, 5, 2))
#print(is_horizontal_four_in_line(test_board, 5, 2))


def game_start():
    user_input = " "
    turn = 1
    board = [["*", "*", "*", "*", "*", "*", "*"],
             ["*", "*", "*", "*", "*", "*", "*"],
             ["*", "*", "*", "*", "*", "*", "*"],
             [2,   "*", 2,  "*",  "*", "*", "*"],
             [2,   "*", 2,  "*",  "*", "*", "*"],
             [2,    2,  2,  "*",  "*", "*", "*"]]
    user = 1
    exit_command = {"x", "z"}
    while user_input not in exit_command:
        print("Runda :", turn)
        user_input = input("Twój ruch graczu:" + str(user)).lower()
        if user_input in exit_command:
            print("Koniec gry")
            return
        try:
            user_input = int(user_input)
        except:
            print("Wrong type")
            continue
        if user_input > 7:
            print("Wrong value")
            continue
        draw_board(board)
        board = drop_disc_in_column(user_input, board, user)
        draw_board(board)
        check_winner(board, user_input, user)
        turn += 1
        user = (user % 2) + 1


"""
sprawdzenie w 1;column 2:row czy jest wygrany, robię licznik wygranych,
zabezpieczam out of range 
sprawdzam w pionie czy jest wygrany, cały rząd dodaje do licznika
jeśli jest wygrany to po każdym ruchu- każdym sprawdzeniu kończę grę z Wygranym 
"""

# def players_turn():
#    player = input("Press 1 -player 1, Press 2 - player 2")
#    if player == "2":

# def players_move():

# print(draw_board())
print(game_start())
