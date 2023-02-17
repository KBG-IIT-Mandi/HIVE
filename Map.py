import random
import numpy as np
import math
from Constants import *
import pygame

pygame.init()


def makeMap():
    map1 = np.zeros((height, width))


    # # center square for spawn remove later and make proper spawn loc
    # k = 0.6
    # for y in range(height//2-50, height//2+50):
    #     for x in range(width//2-50, width//2+50):
    #         if random.random() < k:
    #             map1[y][x] = 1

    #start for dunark walk
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)

    # Walk
    count = 1
    for i in range(2):
        steps = int((width*height*2.5))

        for i in range(steps):
            # Choose a random direction
            direction = random.choice(["north", "west","south",  "east"])

            if direction == "north":
                if y-1>= 0:
                    y = y-1
                else:
                    y=height-1
            
            elif direction == "south":
                if y+1< height:
                    y = y+1
                else:
                    y=0

            elif direction == "west":
                if x-1>= 0:
                    x = x-1
                else:
                    x=width-1

            elif direction == "east":
                if x+1< width:
                    x = x+1
                else:
                    x=0

            map1[y][x] = 1
        count+=1


    ref_array = map1.copy()


    # cellular automata
    def auto(base_map, main_map):
        for x in range(1,height-1):
            for y in range(1,width-1):
                count = 0
                for val in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                    if base_map[x+val[0]][y+val[1]] == 1:
                            count += 1
                if count >= 4:
                    main_map[x][y] = 1
    
        return(main_map)

    for i in range(3):
        main = auto(ref_array, map1)
        ref_array = main.copy()
        map1 = main.copy()


    thickness = 20
    for y in range(height):
        for x in range(width):
            if x< thickness or y< thickness or x>width-thickness or y>height-thickness:
                map1[y][x] = 0

    # map_surface = pygame.Surface((map1.shape[1], map1.shape[0]))

    # # Iterate through the map array and set the color of each pixel on the surface
    # for i in range(map1.shape[0]):
    #     for j in range(map1.shape[1]):
    #         if map1[i, j] == 0:
    #             color = (20, 20, 20)
    #         else:
    #             color = (200, 200, 200)
    #         map_surface.set_at((j, i), color)

    # # Convert the map surface to a memory buffer
    # map_buffer = pygame.image.tostring(map_surface, "RGBA")

    # # Create a surface from the memory buffer
    # map_surface = pygame.image.fromstring(map_buffer, map_surface.get_size(), "RGBA")

    # # Create a Pygame window to display the map
    # screen = pygame.display.set_mode((map_surface.get_width(), map_surface.get_height()))

    return(map1)




