import Map
from Constants import *
import pygame
import random
import numpy as np


map1 = Map.makeMap()

FOOD_chance = 0.6 #1
WOOD = 0.25 #2
STONE = 0.15 #3

def spread_food(floor_map, num_piles, pile_radius):
    food_map = np.zeros(floor_map.shape)
    piles = []
    for i in range(num_piles):
        pile_placed = False
        while not pile_placed:
            R = np.random.choice([1,2,3], p=[FOOD_chance, WOOD, STONE])
            x, y = np.random.randint(0, floor_map.shape[0]), np.random.randint(0, floor_map.shape[1])
            if floor_map[x][y] == 1:
                piles.append([(x, y),R])
                pile_placed = True

                # for i in range(x-pile_radius, x+pile_radius+1):
                #     for j in range(y-pile_radius, y+pile_radius+1):
                #         if i >= 0 and i < floor_map.shape[0] and j >= 0 and j < floor_map.shape[1] and floor_map[i][j] == 1:
                #             food_map[i][j] = R

                # # CAN PUT ANY ALGO HERE
                # steps = random.randint(300,600)
                max_in_direction = 100
                for i in range(300):
                    coord_x = x
                    coord_y = y
                    for i in range(max_in_direction):
                        direction = random.choice(["north", "west","south","east"])

                        if direction == "north":
                            if coord_y-1>= 0 and floor_map[coord_x][coord_y-1] == 1:
                                coord_y = coord_y-1
                            else:
                                pass
                        
                        elif direction == "south":
                            if coord_y+1< height and floor_map[coord_x][coord_y+1] == 1:
                                coord_y = coord_y+1
                            else:
                                pass

                        elif direction == "west":
                            if coord_x-1>= 0 and floor_map[coord_x-1][coord_y] == 1:
                                coord_x = coord_x-1
                            else:
                                pass

                        elif direction == "east":
                            if coord_x+1< width and floor_map[coord_x+1][coord_y] == 1:
                                coord_x = coord_x+1
                            else:
                                pass

                        food_map[coord_x][coord_y] = R

        # try to make sure a good dist btw resources                        
        for pile in piles[:-1]:
            distance = np.sqrt((x-pile[0][0])**2 + (y-pile[0][1])**2)
            if distance < 2 * pile_radius:
                pile_placed = False
                break
    return (food_map, piles)


num_piles = random.randint(30, 45)
pile_radius = 15
food_map, piles = spread_food(map1, num_piles, pile_radius)
# print(piles)
main_map = map1+food_map

map_surface = pygame.Surface((main_map.shape[1], main_map.shape[0]))
# Iterate through the map array and set the color of each pixel on the surface
for i in range(main_map.shape[0]):
    for j in range(main_map.shape[1]):
        if main_map[i, j] == 0:  # walls
            color = (20, 20, 20)

        elif main_map[i, j] == 1:  # Floor
            color = (200, 200, 200)
        
        elif main_map[i, j] == 2:  # Food
            color = (90, 220, 90)

        elif main_map[i, j] == 3:  # Wood
            color = (133, 87, 35)

        elif main_map[i, j] == 4:  # Stone
            color = (80, 80, 80)
        map_surface.set_at((j, i), color)


    # Convert the map surface to a memory buffer
map_buffer = pygame.image.tostring(map_surface, "RGBA")

# Create a surface from the memory buffer
map_surface = pygame.image.fromstring(map_buffer, map_surface.get_size(), "RGBA")

# Create a Pygame window to display the map
screen = pygame.display.set_mode((map_surface.get_width(), map_surface.get_height()))


WORLD_trace = np.zeros((height,width,2))
WORLD_trace[...,0] = map1
WORLD_trace[...,1] = food_map

import sys
np.set_printoptions(threshold=sys.maxsize)

print(sum(WORLD_trace[...,1]))

def draw_map():
    screen.fill((0, 0, 0))
    screen.blit(map_surface, (0, 0))
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_map()
    
pygame.quit()