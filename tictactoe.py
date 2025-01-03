import sys
import pygame

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
                
        pygame.display.update()
            


main()