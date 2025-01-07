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
    ai = game.ai
    
    def make_move(row, col):
        board.mark_sqr(row, col, game.player)
        game.draw_fig(screen, row, col, game.player)
        game.next_turn()       
    
    # mainloop
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN: 
                # g-gamemode    
                if event.key == pygame.K_g:
                    game.change_gamemode()
                
                # r-reset
                if event.key == pygame.K_r:
                    game.reset(screen)
                    board = game.board
                    ai = game.ai
                    
                # 0-random ai
                if event.key == pygame.K_0:
                    ai.level = 0
                    print('Random AI selected')
                # 1-unbeatable ai
                if event.key == pygame.K_1:
                    ai.level = 1 
                    print('Unbeatable AI selected')
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                
                if board.empty_sqr(row, col) and game.running:
                    make_move(row, col)
                
                #print(board.squares)
                if game.isover(screen):
                    game.running = False
                    print('Game Over')
                              
        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            if game.isover(screen):
                game.running = False
                print('Game Over')
            
            else:
                pygame.display.update()
            
                # ai methods
                row, col = ai.eval(board)
                
                # Move into a function
                make_move(row, col)
             
        pygame.display.update()
            
main()