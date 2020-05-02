import pygame
from pygame.locals import *
from Constantes import *

class Hero:

    def __init__(self, hero_image, MAZE):
        
        self.Hero = pygame.image.load(hero_image).convert_alpha()
        
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        
        self.maze = MAZE

    def move(self):

        if direction == "right":
            if self.case_x < (number_sprite_size - 1):
                if self.maze.structure[self.case_y][self.case_x+1] != 'w':
                    self.case_x += 1
                    self.x = self.case_x * sprite_size
                self.direction = self.right

        if direction == "left":
            if self.case_x > 0:
                if self.maze.structure[self.case_y][self.case_x-1] != 'w':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size
                self.direction = self.left
                
        if direction == "up":
            if self.case_y > 0:
                if self.maze.structure[self.case_y-1][self.case_x] != 'w':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size
                self.direction = self.up
                
        if direction == "down":
            if self.case_y < (number_sprite_size - 1):
                if self.maze.structure[self.case_y+1][self.case_x] != 'w':
                    self.case_y += 1
                    self.y = self.case_y * sprite_size
                self.direction = self.down
