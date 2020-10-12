import pygame
import sys
from pygame.locals import *
from pygame_connect4 import game_functions as gf

pygame.init()

screen = pygame.display.set_mode((700, 600), 0, 32)
pygame.display.set_caption("Connect 4")
screen_color = (0, 10, 255)

user = 1
turn = 1
selected_column = 0
board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

keys_numbers = {K_1: 0, K_2: 1, K_3: 2, K_4: 3, K_5: 4, K_6: 5, K_7: 6}
screen.fill(screen_color)
gf.draw_board(screen)
winner = 0
while winner == 0:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            selected_column = keys_numbers[event.key]
            row = gf.drop_disc_in_column(selected_column, board, user)
            gf.draw_dropped_disc(board, screen)

            if gf.is_horizontal_four_in_line(board, row, selected_column, user) or gf.is_vertical_four_in_line(board,row,selected_column, user):
                gf.draw_winner_info(user, screen)
                pygame.time.wait(400)
                winner = user
            turn += 1
            user = (user % 2) + 1
        pygame.display.update()


