#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from pygame.locals import *
from Constantes import *

class Maze: # class allowing maze creation

    def __init__(self, maze):
        self.maze = maze
        self.structure = 0

    def generate(self): # method to generate the structure
                        # of the maze from the text file

        with open(self.maze, "r") as maze:
            maze_structure = []

            for line in maze:
                maze_line = []

                for sprite in line:
                    if sprite != '\n':

                        maze_line.append(sprite)
                        
                maze_structure.append(maze_line)

            self.structure = maze_structure
                        

    def display(self, window):


        #start = pygame.image.load(start_image).convert()
        wall = pygame.image.load(wall_image).convert()
        guard = pygame.image.load(guard_image).convert_alpha()

        line_num = 0
        for line in self.structure:

            case_num = 0
            for sprite in line:

                x = case_num * sprite_size
                y = line_num * sprite_size
                #x = case_num
                #y = line_num
                
                if sprite == 'w':
                    window.blit(wall, (x,y))

                #elif sprite == 's':
                    #window.blit(start, (x,y))

                elif sprite == 'g':
                    window.blit(guard, (x,y))

                case_num += 1
            line_num += 1
