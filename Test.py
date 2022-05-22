import sys
import pygame
from pygame.locals import KEYDOWN, K_q
import numpy as np
import time

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 1280, 720
BG = pygame.image.load("Assets/MysteryBack.jpg")
BG = pygame.transform.scale(BG, (SCREENSIZE))
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
YELLOW = (255, 255, 0)
TOMATO = (255, 0, 0)
DBLUE = (30, 144, 255)
LIME = (0, 255, 0)
WHITE = (255, 255, 255)

pygame.init()  # Initial Setup

# OUR GRID MAP:
cellMAP = np.random.randint(2, size=(10, 10))
print(cellMAP)

# e.g. >>
# [[1 1 1 1 1 1]
#  [0 0 1 1 0 1]
#  [1 0 0 0 1 1]
#  [0 0 0 1 1 0]
#  [0 1 1 0 0 0]
#  [1 0 0 0 0 0]]


_VARS = {'surf': False,
         'gridSize': cellMAP.shape[0],
         'cellSize': 50,
         'cartGridOrigin': [80, 100],
         'isoGridOrigin': [520, -140]}

def main():

    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    red = 0
    blue = 0
    green = 0
    while True:
        checkEvents()
        _VARS['surf'].fill((red, blue, green))
        _VARS['surf'].blit(BG, (0, 0))
        # PLacing tiles first to avoid tile border issues
        placeISOTiles()
        drawIsometricGrid(_VARS['isoGridOrigin'],
                          _VARS['gridSize'],
                          _VARS['cellSize'])
        pygame.display.update()

def cartToIso(point):
    isoX = point[0] - point[1]
    isoY = (point[0] + point[1])/2
    return [isoX, isoY]

def drawIsometricGrid(origin, size, cellSize):
    hw = cellSize*size
    borderPoints = [cartToIso(origin),
                    cartToIso([origin[0], hw + origin[1]]),
                    cartToIso([hw + origin[0], hw + origin[1]]),
                    cartToIso([hw + origin[0], origin[1]])]
    # Draw border
    pygame.draw.polygon(_VARS['surf'], BLACK, borderPoints, 2)
    # Draw inner grid :
    for colRow in range(1, size):
        dim = cellSize*colRow
        pygame.draw.line(_VARS['surf'], BLACK,
                         cartToIso([origin[0], origin[1] + dim]),
                         cartToIso([hw + origin[0], origin[1] + dim]), 1)
        pygame.draw.line(_VARS['surf'], BLACK,
                         cartToIso([origin[0] + dim, origin[1]]),
                         cartToIso([origin[0] + dim, hw + origin[1]]), 1)

def placeISOTiles():
    tileDIM = _VARS['cellSize']
    origin = _VARS['isoGridOrigin']
    originX, originY = origin[0], origin[1]
    for row in range(cellMAP.shape[0]):
        for column in range(cellMAP.shape[1]):
            # Is the grid cell tiled ?
            if(cellMAP[column][row] == 1):
                tilePoints = [cartToIso([originX + (tileDIM*row),
                              originY + (tileDIM*column)]),
                              cartToIso([originX + (tileDIM*(row + 1)),
                                         originY + (tileDIM*column)]),
                              cartToIso([originX + (tileDIM*(row + 1)),
                                         originY + (tileDIM*(column + 1))]),
                              cartToIso([originX + (tileDIM*row),
                                         originY + (tileDIM*(column + 1))])
                              ]
                pygame.draw.polygon(_VARS['surf'], TOMATO, tilePoints, )

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()



main()