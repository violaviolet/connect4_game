import pygame
import sys
from pygame.locals import *


def draw_board(screen):
    for row in range(0, 6):
        for column in range(0, 7):
            pygame.draw.rect(screen, (255, 255, 255), Rect((column * 50, row * 50), (50, 50)), 3)


def drop_disc_in_column(selected_column, board, user):
    empty_row = 0
    for row in range(len(board)):
        if board[row][selected_column] == 0:
            empty_row = row
        else:
            break
    board[empty_row][selected_column] = user
    return board


def draw_dropped_disc(board, screen):
    for row in range(0, 6):
        for column in range(0, 7):
            x = column * 50 + 25
            y = row * 50 + 25

            if board[row][column] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)

            elif board[row][column] == 2:
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)


def check_row_of_last_move(board, selected_column):
    row_index = 0
    for row in range(len(board)):
        if board[row][selected_column] == 0:
            row_index = row + 1
    return row_index


def is_vertical_four_in_line(board, selected_column, user):
    win_counter = 0
    for row in range(len(board)):
        if board[row][selected_column] == user:
            win_counter = win_counter + 1
    if win_counter >= 4:
        return True


def is_horizontal_four_in_line(board, selected_column, user):
    win_counter = 0
    last_move_row_index = check_row_of_last_move(board, selected_column)
    for column in range(len(board[last_move_row_index])):
        if board[last_move_row_index][column] == user:
            win_counter = win_counter + 1
        else:
            win_counter = 0
    if win_counter >= 4:
        return True


def check_winner(board, selected_column, user):
    if is_horizontal_four_in_line(board, selected_column, user) is True or is_vertical_four_in_line(board, selected_column, user) is True:
        print("Congrats you won player:", user)
    return True


def draw_winner_info(user, screen):
    font_object = pygame.font.SysFont("freesansbold", 26)
    if user == 1:
        information = "Winner is Player:"+ str(user)
    elif user == 2:
        information = "Winner is PLayer:" + str(user)
    text_frame = font_object.render(information, True, (20, 255, 20))
    text_rect = text_frame.get_rect()
    text_rect_center = (75, 75)
    screen. blit(text_frame, text_rect)
