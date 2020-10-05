import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((700, 600), 0, 32)
pygame.display.set_caption("Connect 4")
screen_color = (51, 51, 255)

board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

keys_numbers = {K_1: 1, K_2: 2, K_3: 3, K_4: 4, K_5: 5, K_6: 6, K_7: 7}


def draw_board():
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


def draw_user_move(board):
    for row in range(0, 6):
        for column in range(0, 7):
            x = column * 50 + 25
            y = row * 50 + 25

            if board[row][column] == 1:
                pygame.draw.circle(screen, (255, 0, 255), (x, y), 10)

            elif board[row][column] == 2:
                pygame.draw.circle(screen, (0, 10, 255), (x, y), 10)


while True:
    user = 1
    turn = 1
    selected_column = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key in keys_numbers.keys():
                selected_column = int(event.unicode) - 1


    #print(keys_numbers["K_1"])

    screen.fill(screen_color)
    draw_board()
    #draw_user_move(board)
    board = drop_disc_in_column(selected_column, board, user)
    #draw_user_move(board)
    pygame.display.update()
    turn += 1
    user = (user % 2) + 1
