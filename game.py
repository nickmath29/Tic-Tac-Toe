import sys
import pygame

from constants import *
from board import Board
from AI import AI


class Game:
    
    def __init__(self, screen):
        self.board = Board(screen)
        self.ai = AI()
        self.player = 1 # 1-Cross 2-Circles
        self.gamemode = 'pvp'
        self.running =  True
        self.show_lines(screen)
    
    def show_lines(self, screen):
        screen.fill(BG_COLOR)
        
        # vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH-SQSIZE, HEIGHT), LINE_WIDTH)
        
        # horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
        
    def draw_fig(self, screen, row, col, player):
        if player == 1:
            # draw cross
            
            # descending line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            
            # ascending line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
            
        elif player == 2:
            # draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)
    
    def next_turn(self):
        self.player = self.player % 2 + 1
    
    def change_gamemode(self):
        if self.gamemode == 'pvp':
            self.gamemode = 'ai'
            print(f'Gamemode: {self.gamemode}')
        else:
            self.gamemode = 'pvp'
            print(f'Gamemode: {self.gamemode}')
    
    def isover(self, screen):
        return self.board.final_state(screen, show=True) != 0 or self.board.isfull()
 
    def reset(self, screen):
        self.__init__(screen)
