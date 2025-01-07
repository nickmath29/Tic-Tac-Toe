import sys
import pygame
import random
import numpy as np

from constants import *
from game import Game

# PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

def main():
    
    # objects
    game = Game(screen)
    board = game.board
    ai = game.ai
    
    # mainloop
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                
                if board.empty_sqr(row, col):
                    board.mark_sqr(row, col, game.player)
                    game.draw_fig(screen, row, col, game.player)
                    game.next_turn()
                    #print(board.squares)
                if board.final_state() == 1 or board.final_state() == 2:
                    print('Game Over')
        
        if game.gamemode == 'ai' and game.player == ai.player:
            pygame.display.update()
        
            # ai methods
            row, col = ai.eval(board)
            
            # Move into a function
            board.mark_sqr(row, col, game.player)
            game.draw_fig(screen, row, col, game.player)
            game.next_turn()
            
            
                    
                
        pygame.display.update()
            


main()