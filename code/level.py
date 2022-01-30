from re import X
import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()


        #setting up sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
    #sprit setup again
        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites])
        
    
    def run(self):
        pass