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


def draw_user_move(board, screen):
    for row in range(0, 6):
        for column in range(0, 7):
            x = column * 50 + 25
            y = row * 50 + 25

            if board[row][column] == 1:
                pygame.draw.circle(screen, (255, 0, 255), (x, y), 10)

            elif board[row][column] == 2:
                pygame.draw.circle(screen, (0, 10, 255), (x, y), 10)


