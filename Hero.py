import pygame
from pygame.locals import *
from Constantes import *

class Hero:

    def __intit__(self, hero, maze):
        self.Hero = hero
        self.case_x = 0
        self.cas_y = 0
        self.x = 0
        self.y = 0
        self.maze = maze

    def move(self, direction):

        if direction == "right":
            if self.case_x < (number_sprite_size - 1):
                if self.maze.structure[self.case_y][self.case_x+1] != 'm':
                    self.case_x += 1
                    self.x = self.case_x * taille_sprite
                self.direction = self.droite
