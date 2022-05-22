import sys
import pygame
from pygame.locals import KEYDOWN, K_q
from pygame.locals import MOUSEBUTTONDOWN
import numpy as np
import time
import math
# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 1280, 720
BG = pygame.image.load("Assets/pixil-frame-0.png")
BG = pygame.transform.scale(BG, (SCREENSIZE))
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
YELLOW = (255, 255, 0)
TOMATO = (255, 0, 0)
DBLUE = (30, 144, 255)
LIME = (0, 255, 0)
WHITE = (255, 255, 255)
button1_1 = pygame.Rect((633, 193),
                         (695-633, 226-193))
grid1_1 = False

rect0_0 = pygame.Rect((635, 202.5),(50, 25))

rect1_0 = pygame.Rect((585, 227.5),(50, 25))

rect2_0 = pygame.Rect((535, 252.5),(50, 25)) 

rect3_0 = pygame.Rect((485, 277.5),(50, 25)) 

rect4_0 = pygame.Rect((435, 302.5),(50, 25))

rect5_0 = pygame.Rect((385, 327.5),(50, 25))

rect6_0 = pygame.Rect((335, 352.5),(50, 25))

rect7_0 = pygame.Rect((285, 377.5),(50, 25))

rect8_0 = pygame.Rect((235, 402.5),(50, 25)) 

rect9_0 = pygame.Rect((185, 427.5),(50, 25)) 

rect0_1 = pygame.Rect((685, 227.5),(50, 25)) 

rect1_1 = pygame.Rect((635, 252.5),(50, 25)) 

rect2_1 = pygame.Rect((585, 277.5),(50, 25)) 

rect3_1 = pygame.Rect((535, 302.5),(50, 25)) 

rect4_1 = pygame.Rect((485, 327.5),(50, 25)) 

rect5_1 = pygame.Rect((435, 352.5),(50, 25)) 

rect6_1 = pygame.Rect((385, 377.5),(50, 25)) 

rect7_1 = pygame.Rect((335, 402.5),(50, 25)) 

rect8_1 = pygame.Rect((285, 427.5),(50, 25))

rect9_1 = pygame.Rect((235, 452.5),(50, 25)) 

rect0_2 = pygame.Rect((735, 252.5),(50, 25)) 

rect1_2 = pygame.Rect((685, 277.5),(50, 25)) 

rect2_2 = pygame.Rect((635, 302.5),(50, 25)) 

rect3_2 = pygame.Rect((585, 327.5),(50, 25)) 

rect4_2 = pygame.Rect((535, 352.5),(50, 25)) 

rect5_2 = pygame.Rect((485, 377.5),(50, 25)) 

rect6_2 = pygame.Rect((435, 402.5),(50, 25)) 

rect7_2 = pygame.Rect((385, 427.5),(50, 25)) 

rect8_2 = pygame.Rect((335, 452.5),(50, 25))

rect9_2 = pygame.Rect((285, 477.5),(50, 25)) 

rect0_3 = pygame.Rect((785, 277.5),(50, 25)) 

rect1_3 = pygame.Rect((735, 302.5),(50, 25)) 

rect2_3 = pygame.Rect((685, 327.5),(50, 25)) 

rect3_3 = pygame.Rect((635, 352.5),(50, 25)) 

rect4_3 = pygame.Rect((585, 377.5),(50, 25)) 

rect5_3 = pygame.Rect((535, 402.5),(50, 25)) 

rect6_3 = pygame.Rect((485, 427.5),(50, 25)) 

rect7_3 = pygame.Rect((435, 452.5),(50, 25)) 

rect8_3 = pygame.Rect((385, 477.5),(50, 25)) 

rect9_3 = pygame.Rect((335, 502.5),(50, 25)) 

rect0_4 = pygame.Rect((835, 302.5),(50, 25)) 

rect1_4 = pygame.Rect((785, 327.5),(50, 25)) 

rect2_4 = pygame.Rect((735, 352.5),(50, 25)) 

rect3_4 = pygame.Rect((685, 377.5),(50, 25)) 

rect4_4 = pygame.Rect((635, 402.5),(50, 25)) 

rect5_4 = pygame.Rect((585, 427.5),(50, 25)) 

rect6_4 = pygame.Rect((535, 452.5),(50, 25)) 

rect7_4 = pygame.Rect((485, 477.5),(50, 25)) 

rect8_4 = pygame.Rect((435, 502.5),(50, 25)) 

rect9_4 = pygame.Rect((385, 527.5),(50, 25)) 

rect0_5 = pygame.Rect((885, 327.5),(50, 25)) 

rect1_5 = pygame.Rect((835, 352.5),(50, 25)) 

rect2_5 = pygame.Rect((785, 377.5),(50, 25)) 

rect3_5 = pygame.Rect((735, 402.5),(50, 25)) 

rect4_5 = pygame.Rect((685, 427.5),(50, 25)) 


rect5_5 = pygame.Rect((635, 452.5),(50, 25)) 

rect6_5 = pygame.Rect((585, 477.5),(50, 25)) 

rect7_5 = pygame.Rect((535, 502.5),(50, 25)) 

rect8_5 = pygame.Rect((485, 527.5),(50, 25))

rect9_5 = pygame.Rect((435, 552.5),(50, 25)) 

rect0_6 = pygame.Rect((935, 352.5),(50, 25)) 

rect1_6 = pygame.Rect((885, 377.5),(50, 25)) 

rect2_6 = pygame.Rect((835, 402.5),(50, 25)) 

rect3_6 = pygame.Rect((785, 427.5),(50, 25)) 

rect4_6 = pygame.Rect((735, 452.5),(50, 25)) 

rect5_6 = pygame.Rect((685, 477.5),(50, 25)) 

rect6_6 = pygame.Rect((635, 502.5),(50, 25)) 

rect7_6 = pygame.Rect((585, 527.5),(50, 25)) 

rect8_6 = pygame.Rect((535, 552.5),(50, 25)) 

rect9_6 = pygame.Rect((485, 577.5),(50, 25)) 

rect0_7 = pygame.Rect((985, 377.5),(50, 25)) 

rect1_7 = pygame.Rect((935, 402.5),(50, 25)) 

rect2_7 = pygame.Rect((885, 427.5),(50, 25)) 

rect3_7 = pygame.Rect((835, 452.5),(50, 25)) 

rect4_7 = pygame.Rect((785, 477.5),(50, 25)) 

rect5_7 = pygame.Rect((735, 502.5),(50, 25)) 

rect6_7 = pygame.Rect((685, 527.5),(50, 25)) 

rect7_7 = pygame.Rect((635, 552.5),(50, 25)) 

rect8_7 = pygame.Rect((585, 577.5),(50, 25)) 

rect9_7 = pygame.Rect((535, 602.5),(50, 25)) 

rect0_8 = pygame.Rect((1035, 402.5),(50, 25)) 

rect1_8 = pygame.Rect((985, 427.5),(50, 25)) 

rect2_8 = pygame.Rect((935, 452.5),(50, 25)) 

rect3_8 = pygame.Rect((885, 477.5),(50, 25)) 

rect4_8 = pygame.Rect((835, 502.5),(50, 25)) 

rect5_8 = pygame.Rect((785, 527.5),(50, 25)) 

rect6_8 = pygame.Rect((735, 552.5),(50, 25)) 

rect7_8 = pygame.Rect((685, 577.5),(50, 25)) 

rect8_8 = pygame.Rect((635, 602.5),(50, 25)) 

rect9_8 = pygame.Rect((585, 627.5),(50, 25)) 

rect0_9 = pygame.Rect((1085, 427.5),(50, 25)) 

rect1_9 = pygame.Rect((1035, 452.5),(50, 25)) 

rect2_9 = pygame.Rect((985, 477.5),(50, 25)) 

rect3_9 = pygame.Rect((935, 502.5),(50, 25)) 

rect4_9 = pygame.Rect((885, 527.5),(50, 25)) 

rect5_9 = pygame.Rect((835, 552.5),(50, 25)) 

rect6_9 = pygame.Rect((785, 577.5),(50, 25)) 

rect7_9 = pygame.Rect((735, 602.5),(50, 25)) 

rect8_9 = pygame.Rect((685, 627.5),(50, 25)) 

rect9_9 = pygame.Rect((635, 652.5),(50, 25)) 











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
    pygame.init()  # Initial Setup
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    red = 0
    blue = 0
    green = 0
    ascending = True
    #placeISOTiles()
    while True:
        
        _VARS['surf'].fill((red, blue, green))
        _VARS['surf'].blit(BG, (0, 0))
        # PLacing tiles first to avoid tile border issues
        placeISOTiles()
        
        drawIsometricGrid(_VARS['isoGridOrigin'],
                          _VARS['gridSize'],
                          _VARS['cellSize'])
        
        #pygame.draw.rect(_VARS["surf"], BLACK, button1_1, 2)
        checkEvents()
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_5, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_6, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect0_9, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_5, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_6, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect1_9, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_5, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_6, 2) 
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect2_9, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_5, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_6, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect3_9, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_5, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_6, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect4_9, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_5, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_6, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect5_9, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_5, 2)  
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_6, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect6_9, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_5, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_6, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect7_9, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_5, 2)  
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_6, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect8_9, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_0, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_1, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_2, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_3, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_4, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_5, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_6, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_7, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_8, 2)
        pygame.draw.rect(_VARS["surf"], BLACK, rect9_9, 2)
      

        pygame.display.update()

      
        if ascending:
          blue += 1
          green +=1
          red += 1
          if blue == 255:
            ascending = False
        else: 
          blue -= 1
          green -=1
          red -=1
          if blue == 0:
              ascending = True
        time.sleep(.000001)


def cartToIso(point):
    isoX = point[0] - point[1]
    isoY = (point[0] + point[1])/2
    return [isoX, isoY]

def isoToCart(point):
  y = (2*point[1]-point[0])/2 -13
  x = (2*point[1]+point[0])/2 + 10
  return [x, y]


def placeISOTile(origin, color, cellSize):
    print(origin, color, cellSize)
    tilePoints = [cartToIso(origin),
                  cartToIso([origin[0], cellSize + origin[1]]),
                  cartToIso([cellSize + origin[0], cellSize + origin[1]]),
                  cartToIso([cellSize + origin[0], origin[1]])]
    pygame.draw.polygon(_VARS['surf'], color, tilePoints)


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
            

              pygame.draw.polygon(_VARS['surf'], TOMATO, tilePoints)


def checkEvents():
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            if button1_1.collidepoint(x, y):
              print("pressed")
              point = [633, 193]
              placeISOTile(isoToCart(point), YELLOW, 50)
    
        
              
                 
               
     
main()