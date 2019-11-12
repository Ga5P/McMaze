#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import usefull libraries

import pygame
from pygame.locals import *

from Hero import *
from Maze import *
from Constantes import *

# Initialize Pygame

pygame.init()

# Displaying window

window = pygame.display.set_mode((window_size,window_size))

# Window title

window_title = 'Help McGyver !'
pygame.display.set_caption(window_title)

# Window icon
icone = pygame.image.load(icone).convert_alpha()
pygame.display.set_icon(icone)

# Loading game images

hero = pygame.image.load(hero_image).convert_alpha()
guard = pygame.image.load(guard_image).convert_alpha()
start = pygame.image.load(start_image).convert()
wall = pygame.image.load(wall_image).convert()
needle = pygame.image.load(needle_image).convert_alpha()
tube = pygame.image.load(tube_image).convert_alpha()
ether = pygame.image.load(ether_image).convert_alpha()

pygame.key.set_repeat(100, 30) # Allow to move holdin' key

# Displaying background

background = pygame.image.load(background_image).convert()
window.blit(background, (0, 0))

pygame.display.flip()

continue_game = 1
while continue_game:

        pygame.time.Clock().tick(30)

        MAZE = Maze(maze)
        MAZE.generate()
        MAZE.display(window)

#        MG = Hero(Hero, maze)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    MG.move("right")
                elif event.key == K_LEFT:
                    MG.move("left")
                elif event.key == K_DOWN:
                    MG.move("down")
                elif event.key == K_UP:
                    MG.move("up")

#        window.blit(background, (0,0))
#        MAZE.display(window)
