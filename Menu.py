from xml.etree.ElementTree import TreeBuilder
import pygame, sys
from button import Button
from tkinter import CENTER
import time, random
from pygame.locals import *
import numpy as np

#Constants
GREY = (160, 160, 160)
YELLOW = (255, 255, 0)
TOMATO = (255, 0, 0)
DBLUE = (30, 144, 255)
LIME = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (252, 186, 3)
#fonts = pygame.font.Font(None, 80)
#Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
#font = pygame.font.SysFont(None, 80)
#WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Colonization Simulator")
pygame.init()

pygame.display.set_caption("Menu")

BG = pygame.image.load("Assets/MenuScreenBackGround2.jpg")
BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))

#Setup Functions
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Assets/zerovelo.ttf", size)
def get_font2(size):
    return pygame.font.Font("Assets/SF Atarian System.ttf", size)
def writeText(text, font, color, surface,    x, y):
    text = font.render(text, 1, color)
    box = text.get_rect()
    box.center = (x, y)
    surface.blit(text, box)
    button = pygame.Rect((box.left - 4, box.top - 4),
                         (box.width + 8, box.height + 8))
    pygame.draw.rect(_VARS['surf'], BLACK, button, 2)
    return button
def hud(health, population, money):
  writeText(f'Health: {health}%   Population: {population}   Money:  ${money} ', get_font2(30), GOLD, _VARS['surf'], 1000, 50) 


#-----------------Rectangle Buttons------------------
rect0_0 = pygame.Rect((635, 202.5),(50, 25))
point0_0 = [635, 202.5]
rect1_0 = pygame.Rect((585, 227.5),(50, 25))
point1_0 = [585, 227.5]
rect2_0 = pygame.Rect((535, 252.5),(50, 25)) 
point2_0 = [535, 252.5]
rect3_0 = pygame.Rect((485, 277.5),(50, 25)) 
point3_0 = [485, 277.5]
rect4_0 = pygame.Rect((435, 302.5),(50, 25))
point4_0 = [435, 302.5]
rect5_0 = pygame.Rect((385, 327.5),(50, 25))
point5_0 = [385, 327.5]
rect6_0 = pygame.Rect((335, 352.5),(50, 25))
point6_0 = [335, 352.5]
rect7_0 = pygame.Rect((285, 377.5),(50, 25))
point7_0 = [285, 377.5]
rect8_0 = pygame.Rect((235, 402.5),(50, 25)) 
#8 0
point8_0 = 235, 402.5
rect9_0 = pygame.Rect((185, 427.5),(50, 25)) 
#9 0
point9_0 = [185, 427.5]
rect0_1 = pygame.Rect((685, 227.5),(50, 25)) 
#0 1
point0_1 = [685, 227.5]
rect1_1 = pygame.Rect((635, 252.5),(50, 25)) 
#1 1
point1_1 = [635, 252.5]
rect2_1 = pygame.Rect((585, 277.5),(50, 25)) 
#2 1
point2_1 = [585, 277.5]
rect3_1 = pygame.Rect((535, 302.5),(50, 25)) 
#3 1
point3_1 = [535, 302.5]
rect4_1 = pygame.Rect((485, 327.5),(50, 25)) 
#4 1
point4_1 = [485, 327.5]
rect5_1 = pygame.Rect((435, 352.5),(50, 25)) 
#5 1
point5_1 = [435, 352.5]
rect6_1 = pygame.Rect((385, 377.5),(50, 25)) 
#6 1
point6_1 = [385, 377.5]
rect7_1 = pygame.Rect((335, 402.5),(50, 25)) 
#7 1
point7_1 = [335, 402.5]
rect8_1 = pygame.Rect((285, 427.5),(50, 25))
#8 1
point8_1 = [285, 427.5]
rect9_1 = pygame.Rect((235, 452.5),(50, 25)) 
#9 1
point9_1 = [235, 452.5]
rect0_2 = pygame.Rect((735, 252.5),(50, 25)) 
#0 2
point0_2 = [735, 252.5]
rect1_2 = pygame.Rect((685, 277.5),(50, 25)) 
#1 2
point1_2 = [685, 277.5]
rect2_2 = pygame.Rect((635, 302.5),(50, 25)) 
#2 2
point2_2 = [635, 302.5]
rect3_2 = pygame.Rect((585, 327.5),(50, 25)) 
#3 2
point3_2 = [585, 327.5]
rect4_2 = pygame.Rect((535, 352.5),(50, 25)) 
#4 2
point4_2 = [535, 352.5]
rect5_2 = pygame.Rect((485, 377.5),(50, 25)) 
#5 2
point5_2 = [485, 377.5]
rect6_2 = pygame.Rect((435, 402.5),(50, 25)) 
#6 2
point6_2 = [435, 402.5]
rect7_2 = pygame.Rect((385, 427.5),(50, 25)) 
#7 2
point7_2 = [385, 427.5]
rect8_2 = pygame.Rect((335, 452.5),(50, 25))
#8 2
point8_2 = [335, 452.5]
rect9_2 = pygame.Rect((285, 477.5),(50, 25)) 
#9 2
point9_2 = [285, 477.5]
rect0_3 = pygame.Rect((785, 277.5),(50, 25)) 
#0 3
point0_3 = [785, 277.5]
rect1_3 = pygame.Rect((735, 302.5),(50, 25)) 
#1 3
point1_3 = [735, 302.5]
rect2_3 = pygame.Rect((685, 327.5),(50, 25)) 
#2 3
point2_3 = [685, 327.5]
rect3_3 = pygame.Rect((635, 352.5),(50, 25)) 
#3 3
point3_3 = [635, 352.5]
rect4_3 = pygame.Rect((585, 377.5),(50, 25)) 
#4 3
point4_3 = [585, 377.5]
rect5_3 = pygame.Rect((535, 402.5),(50, 25)) 
#5 3
point5_3 = [535, 402.5]
rect6_3 = pygame.Rect((485, 427.5),(50, 25)) 
#6 3
point6_3 = [485, 427.5]
rect7_3 = pygame.Rect((435, 452.5),(50, 25)) 
#7 3
point7_3 = [435, 452.5]
rect8_3 = pygame.Rect((385, 477.5),(50, 25)) 
#8 3
point8_3 = [385, 477.5]
rect9_3 = pygame.Rect((335, 502.5),(50, 25)) 
#9 3
point9_3 = [335, 502.5]
rect0_4 = pygame.Rect((835, 302.5),(50, 25)) 
#0 4
point0_4 = [835, 302.5]
rect1_4 = pygame.Rect((785, 327.5),(50, 25)) 
#1 4
point1_4 = [785, 327.5]
rect2_4 = pygame.Rect((735, 352.5),(50, 25)) 
#2 4
point2_4 = [735, 352.5]
rect3_4 = pygame.Rect((685, 377.5),(50, 25)) 
#3 4
point3_4 = [685, 377.5]
rect4_4 = pygame.Rect((635, 402.5),(50, 25)) 
#4 4
point4_4 = [635, 402.5]
rect5_4 = pygame.Rect((585, 427.5),(50, 25)) 
#5 4
point5_4 = [585, 427.5]
rect6_4 = pygame.Rect((535, 452.5),(50, 25)) 
#6 4
point6_4 = [535, 452.5]
rect7_4 = pygame.Rect((485, 477.5),(50, 25)) 
#7 4
point7_4 = [485, 477.5]
rect8_4 = pygame.Rect((435, 502.5),(50, 25)) 
#8 4
point8_4 = [435, 502.5]
rect9_4 = pygame.Rect((385, 527.5),(50, 25)) 
#9 4
point9_4 = [385, 527.5]
rect0_5 = pygame.Rect((885, 327.5),(50, 25)) 
#0 5
point0_5 = [885, 327.5]
rect1_5 = pygame.Rect((835, 352.5),(50, 25)) 
#1 5
point1_5 = [835, 352.5]
rect2_5 = pygame.Rect((785, 377.5),(50, 25)) 
#2 5
point2_5 = [785, 377.5]
rect3_5 = pygame.Rect((735, 402.5),(50, 25)) 
#3 5
point3_5 = [735, 402.5]
rect4_5 = pygame.Rect((685, 427.5),(50, 25)) 
#4 5
point4_5 = [685, 427.5]
rect5_5 = pygame.Rect((635, 452.5),(50, 25)) 
#5 5
point5_5 = [635, 452.5]
rect6_5 = pygame.Rect((585, 477.5),(50, 25)) 
#6 5
point6_5 = [585, 477.5]
rect7_5 = pygame.Rect((535, 502.5),(50, 25)) 
#7 5
point7_5 = [535, 502.5]
rect8_5 = pygame.Rect((485, 527.5),(50, 25))
#8 5
point8_5 = [485, 527.5]
rect9_5 = pygame.Rect((435, 552.5),(50, 25)) 
#9 5
point9_5 = [435, 552.5]
rect0_6 = pygame.Rect((935, 352.5),(50, 25)) 
#0 6
point0_6 = [935, 352.5]
rect1_6 = pygame.Rect((885, 377.5),(50, 25)) 
#1 6
point1_6 = [885, 377.5]
rect2_6 = pygame.Rect((835, 402.5),(50, 25)) 
#2 6
point2_6 = [835, 402.5]
rect3_6 = pygame.Rect((785, 427.5),(50, 25)) 
#3 6
point3_6 = [785, 427.5]
rect4_6 = pygame.Rect((735, 452.5),(50, 25)) 
#4 6
point4_6 = [735, 452.5]
rect5_6 = pygame.Rect((685, 477.5),(50, 25)) 
#5 6
point5_6 = [685, 477.5]
rect6_6 = pygame.Rect((635, 502.5),(50, 25)) 
#6 6
point6_6 = [635, 502.5]
rect7_6 = pygame.Rect((585, 527.5),(50, 25)) 
#7 6
point7_6 = [585, 527.5]
rect8_6 = pygame.Rect((535, 552.5),(50, 25)) 
#8 6
point8_6 = [535, 552.5]
rect9_6 = pygame.Rect((485, 577.5),(50, 25)) 
#9 6
point9_6 = [485, 577.5]
rect0_7 = pygame.Rect((985, 377.5),(50, 25)) 
#0 7
point0_7 = [985, 377.5]
rect1_7 = pygame.Rect((935, 402.5),(50, 25)) 
#1 7
point1_7 = [935, 402.5]
rect2_7 = pygame.Rect((885, 427.5),(50, 25)) 
#2 7
point2_7 = [885, 427.5]
rect3_7 = pygame.Rect((835, 452.5),(50, 25)) 
#3 7
point3_7 = [835, 452.5]
rect4_7 = pygame.Rect((785, 477.5),(50, 25)) 
#4 7
point4_7 = [785, 477.5]
rect5_7 = pygame.Rect((735, 502.5),(50, 25)) 
#5 7
point5_7 = [735, 502.5]
rect6_7 = pygame.Rect((685, 527.5),(50, 25)) 
#6 7
point6_7 = [685, 527.5]
rect7_7 = pygame.Rect((635, 552.5),(50, 25)) 
#7 7
point7_7 = [635, 552.5]
rect8_7 = pygame.Rect((585, 577.5),(50, 25)) 
#8 7
point8_7 = [585, 577.5]
rect9_7 = pygame.Rect((535, 602.5),(50, 25)) 
#9 7
point9_7 = [535, 602.5]
rect0_8 = pygame.Rect((1035, 402.5),(50, 25)) 
#0 8
point0_8 = [1035, 402.5]
rect1_8 = pygame.Rect((985, 427.5),(50, 25)) 
#1 8
point1_8 = [985, 427.5]
rect2_8 = pygame.Rect((935, 452.5),(50, 25)) 
#2 8
point2_8 = [935, 452.5]
rect3_8 = pygame.Rect((885, 477.5),(50, 25)) 
#3 8
point3_8 = [885, 477.5]
rect4_8 = pygame.Rect((835, 502.5),(50, 25)) 
#4 8
point4_8 = [835, 502.5]
rect5_8 = pygame.Rect((785, 527.5),(50, 25)) 
#5 8
point5_8 = [785, 527.5]
rect6_8 = pygame.Rect((735, 552.5),(50, 25)) 
#6 8
point6_8 = [735, 552.5]
rect7_8 = pygame.Rect((685, 577.5),(50, 25)) 
#7 8
point7_8 = [685, 577.5]
rect8_8 = pygame.Rect((635, 602.5),(50, 25)) 
#8 8
point8_8 = [635, 602.5]
rect9_8 = pygame.Rect((585, 627.5),(50, 25)) 
#9 8
point9_8 = [585, 627.5]
rect0_9 = pygame.Rect((1085, 427.5),(50, 25)) 
#0 9
point0_9 = [1085, 427.5]
rect1_9 = pygame.Rect((1035, 452.5),(50, 25)) 
#1 9
point1_9 = [1035, 452.5]
rect2_9 = pygame.Rect((985, 477.5),(50, 25)) 
#2 9
point2_9 = [985, 477.5]
rect3_9 = pygame.Rect((935, 502.5),(50, 25)) 
#3 9
point3_9 = [935, 502.5]
rect4_9 = pygame.Rect((885, 527.5),(50, 25)) 
#4 9
point4_9 = [885, 527.5]
rect5_9 = pygame.Rect((835, 552.5),(50, 25)) 
#5 9
point5_9 = [835, 552.5]
rect6_9 = pygame.Rect((785, 577.5),(50, 25)) 
#6 9
point6_9 = [785, 577.5]
rect7_9 = pygame.Rect((735, 602.5),(50, 25)) 
#7 9
point7_9 = [735, 602.5]
rect8_9 = pygame.Rect((685, 627.5),(50, 25)) 
#8 9
point8_9 = [685, 627.5]
rect9_9 = pygame.Rect((635, 652.5),(50, 25)) 
#9 9
point9_9 = [635, 652.5]



rect0_0B = None
rect0_1B = None
rect0_2B = None
rect0_3B = None
rect0_4B = None
rect0_5B = None
rect0_6B = None
rect0_7B = None
rect0_8B = None
rect0_9B = None
rect1_0B = None
rect1_1B = None
rect1_2B = None
rect1_3B = None
rect1_4B = None
rect1_5B = None
rect1_6B = None
rect1_7B = None
rect1_8B = None
rect1_9B = None
rect2_0B = None
rect2_1B = None
rect2_2B = None
rect2_3B = None
rect2_4B = None
rect2_5B = None
rect2_6B = None
rect2_7B = None
rect2_8B = None
rect2_9B = None
rect3_0B = None
rect3_1B = None
rect3_2B = None
rect3_3B = None
rect3_4B = None
rect3_5B = None
rect3_6B = None
rect3_7B = None
rect3_8B = None
rect3_9B = None
rect4_0B = None
rect4_1B = None
rect4_2B = None
rect4_3B = None
rect4_4B = None
rect4_5B = None
rect4_6B = None
rect4_7B = None
rect4_8B = None
rect4_9B = None
rect5_0B = None
rect5_1B = None
rect5_2B = None
rect5_3B = None
rect5_4B = None
rect5_5B = None
rect5_6B = None
rect5_7B = None
rect5_8B = None
rect5_9B = None
rect6_0B = None
rect6_1B = None
rect6_2B = None
rect6_3B = None
rect6_4B = None
rect6_5B = None
rect6_6B = None
rect6_7B = None
rect6_8B = None
rect6_9B = None
rect7_0B = None
rect7_1B = None
rect7_2B = None
rect7_3B = None
rect7_4B = None
rect7_5B = None
rect7_6B = None
rect7_7B = None
rect7_8B = None
rect7_9B = None
rect8_0B = None
rect8_1B = None
rect8_2B = None
rect8_3B = None
rect8_4B = None
rect8_5B = None
rect8_6B = None
rect8_7B = None
rect8_8B = None
rect8_8B = None
rect8_9B = None
rect9_0B = None
rect9_1B = None
rect9_2B = None
rect9_3B = None
rect9_4B = None
rect9_5B = None
rect9_6B = None
rect9_7B = None
rect9_8B = None
rect9_9B = None

#------------END-------------------------------







#---------Stuff for the Isometric Grid -------
popupX = 0
popupY = 0
grid1_1 = False
# OUR GRID MAP:
cellMAP = np.random.randint(2, size=(10, 10))
print(cellMAP)
#[[1, 1, 1, 1, 1, 1],
#  [0, 0, 1, 1, 0, 1],
 #[1, 0, 0, 0, 1, 1],
 # [0, 0, 0, 1, 1, 0],
 # [0, 1, 1, 0, 0, 0],
  #[1, 0, 0, 0, 0, 0]]
#np.random.randint(2, size=(10, 10))
#print(cellMAP)
# e.g. >>
# [[1 1 1 1 1 1]
#  [0 0 1 1 0 1]
#  [1 0 0 0 1 1]
#  [0 0 0 1 1 0]
#  [0 1 1 0 0 0]
#  [1 0 0 0 0 0]]


_VARS = {'surf': pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)),
         'gridSize': cellMAP.shape[0],
         'cellSize': 50,
         'cartGridOrigin': [80, 100],
         'isoGridOrigin': [520, -140]}


popupX, popupY  = pygame.mouse.get_pos() 
    
image = pygame.image.load("Assets/Hospital.png")
def popUp(rectangle): 
  loop = True
  check = False
  while loop:
    #_VARS['surf'].blit(BG, (0, 0))
    pygame.draw.rect(_VARS['surf'], BLACK, rectangle, 2)    
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:          
          if rect0_0.collidepoint(x, y):
            check = True
            rect0_0 = "Place"
          if rect0_1.collidepoint(x, y):
            check = True
            rect0_1 = "Place"
          if rect0_2.collidepoint(x, y):
            check = True
            rect0_2 = "Place"
          if rect0_3.collidepoint(x, y):
            check = True
            rect0_3 = "Place"
          if rect0_4.collidepoint(x, y):
            check = True
            rect0_4 = "Place"
          if rect0_5.collidepoint(x, y):
            check = True
            rect0_5 = "Place"
          if rect0_6.collidepoint(x, y):
            check = True
            rect0_6 = "Place"
          if rect0_7.collidepoint(x, y):
            check = True
            rect0_7 = "Place"
          if rect0_8.collidepoint(x, y):
            check = True
            rect0_9 = "Place"
          if rect1_0.collidepoint(x, y):
            check = True
            rect1_0 = "Place"
          if rect1_1.collidepoint(x, y):
            check = True
            rect1_1 = "Place"
          if rect1_2.collidepoint(x, y):
            check = True
            rect1_2 = "Place"
          if rect1_3.collidepoint(x, y):
            check = True
            rect1_3 = "Place"
          if rect1_4.collidepoint(x, y):
            check = True
            rect1_4 = "Place"
          if rect1_5.collidepoint(x, y):
            check = True
            rect1_5 = "Place"
          if rect1_6.collidepoint(x, y):
            check = True
            rect1_6 = "Place"
            check = True
            rect1_7 = "Place"
          if rect1_7.collidepoint(x, y):
            check = True
            rect1_8 = "Place"
          if rect1_9.collidepoint(x, y):
            check = True
            rect1_9 = "Place"
          if rect2_0.collidepoint(x, y):
            check = True
            rect2_0 = "Place"
          if rect2_1.collidepoint(x, y):
            check = True
            rect2_1 = "Place"
          if rect2_2.collidepoint(x, y):
            check = True
            rect2_2 = "Place"
          if rect2_3.collidepoint(x, y):
            check = True
            rect2_3 = "Place"
          if rect2_4.collidepoint(x, y):
            check = True
            rect2_4 = "Place"
          if rect2_5.collidepoint(x, y):
            check = True
            rect2_5 = "Place"
          if rect2_6.collidepoint(x, y):
            check = True
            rect2_6 = "Place"
          if rect2_7.collidepoint(x, y):
            check = True
            rect2_7 = "Place"
          if rect2_8.collidepoint(x, y):
            check = True
            rect2_8 = "Place"
          if rect2_9.collidepoint(x, y):
            check = True
            rect2_9 = "Place"
          if rect3_0.collidepoint(x, y):
            check = True
            rect3_0 = "Place"
          if rect3_1.collidepoint(x, y):
            check = True
            rect3_1 = "Place"
          if rect3_2.collidepoint(x, y):
            check = True
            rect3_2 = "Place"
          if rect3_3.collidepoint(x, y):
            check = True
            rect3_3 = "Place"
          if rect3_4.collidepoint(x, y):
            check = True
            rect3_4 = "Place"
          if rect3_5.collidepoint(x, y):
            check = True
            rect3_5 = "Place"
          if rect3_6.collidepoint(x, y):
            check = True
            rect3_6 = "Place"
          if rect3_7.collidepoint(x, y):
            check = True
            rect3_7 = "Place"
          if rect3_8.collidepoint(x, y):
            check = True
            rect3_8 = "Place"
          if rect3_9.collidepoint(x, y):
            check = True
            rect3_9 = "Place"
          if rect4_0.collidepoint(x, y):
            check = True
            rect4_0 = "Place"
          if rect4_1.collidepoint(x, y):
            check = True
            rect4_1 = "Place"
          if rect4_2.collidepoint(x, y):
            check = True
            rect4_2 = "Place"
          if rect4_3.collidepoint(x, y):
            check = True
            rect4_3 = "Place"
          if rect4_4.collidepoint(x, y):
            check = True
            rect4_4 = "Place"
          if rect4_5.collidepoint(x, y):
            check = True
            rect4_5 = "Place"
          if rect4_6.collidepoint(x, y):
            check = True
            rect4_6 = "Place"
          if rect4_7.collidepoint(x, y):
            check = True
            rect4_7 = "Place"
          if rect4_8.collidepoint(x, y):
            check = True
            rect4_8 = "Place"
          if rect4_9.collidepoint(x, y):
            check = True
            rect4_9 = "Place"
          if rect5_0.collidepoint(x, y):
            check = True
            rect5_0 = "Place"
          if rect5_1.collidepoint(x, y):
            check = True
            rect5_1 = "Place"
          if rect5_2.collidepoint(x, y):
            check = True
            rect5_2 = "Place"
          if rect5_3.collidepoint(x, y):
            check = True
            rect5_3 = "Place"
          if rect5_4.collidepoint(x, y):
            check = True
            rect5_4 = "Place"
          if rect5_5.collidepoint(x, y):
            check = True
            rect5_5 = "Place"
          if rect5_6.collidepoint(x, y):
            check = True
            rect5_6 = "Place"
          if rect5_7.collidepoint(x, y):
            check = True
            rect5_7 = "Place"
          if rect5_8.collidepoint(x, y):
            check = True
            rect5_8 = "Place"
          if rect5_9.collidepoint(x, y):
            check = True
            rect5_9 = "Place"
          if rect6_0.collidepoint(x, y):
            check = True
            rect6_0 = "Place"
          if rect6_1.collidepoint(x, y):
            check = True
            rect6_1 = "Place"
          if rect6_2.collidepoint(x, y):
            check = True
            rect6_2 = "Place"
          if rect6_3.collidepoint(x, y):
            check = True
            rect6_3 = "Place"
          if rect6_4.collidepoint(x, y):
            check = True
            rect6_4 = "Place"
          if rect6_5.collidepoint(x, y):
            check = True
            rect6_5 = "Place"
          if rect6_6.collidepoint(x, y):
            check = True
            rect6_6 = "Place"
          if rect6_7.collidepoint(x, y):
            check = True
            rect6_7 = "Place"
          if rect6_8.collidepoint(x, y):
            check = True
            rect6_8 = "Place"
          if rect6_9.collidepoint(x, y):
            check = True
            rect6_9 = "Place"
          if rect7_0.collidepoint(x, y):
            check = True
            rect7_0 = "Place"
          if rect7_1.collidepoint(x, y):
            check = True
            rect7_1 = "Place"
          if rect7_2.collidepoint(x, y):
            check = True
            rect7_2 = "Place"
          if rect7_3.collidepoint(x, y):
            check = True
            rect7_3 = "Place"
          if rect7_4.collidepoint(x, y):
            check = True
            rect7_4 = "Place"
          if rect7_5.collidepoint(x, y):
            check = True
            rect7_5 = "Place"
          if rect7_6.collidepoint(x, y):
            check = True
            rect7_6 = "Place"
          if rect7_7.collidepoint(x, y):
            check = True
            rect7_7 = "Place"
          if rect7_8.collidepoint(x, y):
            check = True
            rect7_8 = "Place"
          if rect7_9.collidepoint(x, y):
            check = True
            rect7_9 = "Place"
          if rect8_0.collidepoint(x, y):
            check = True
            rect8_0 = "Place"
          if rect8_1.collidepoint(x, y):
            check = True
            rect8_1 = "Place"
          if rect8_2.collidepoint(x, y):
            check = True
            rect8_2 = "Place"
          if rect8_3.collidepoint(x, y):
            check = True
            rect8_3 = "Place"
          if rect8_4.collidepoint(x, y):
            check = True
            rect8_4 = "Place"
          if rect8_5.collidepoint(x, y):
            check = True
            rect8_5 = "Place"
          if rect8_6.collidepoint(x, y):
            check = True
            rect8_6 = "Place"
          if rect8_7.collidepoint(x, y):
            check = True
            rect8_7 = "Place"
          if rect8_8.collidepoint(x, y):
            check = True
            rect8_8 = "Place"
          if rect8_9.collidepoint(x, y):
            check = True
            rect8_9 = "Place"
          if rect9_0.collidepoint(x, y):
            check = True
            rect9_0 = "Place"
          if rect9_1.collidepoint(x, y):
            check = True
            rect9_1 = "Place"
          if rect9_2.collidepoint(x, y):
            check = True
            rect9_2 = "Place"
          if rect9_3.collidepoint(x, y):
            check = True
            rect9_3 = "Place"
          if rect9_4.collidepoint(x, y):
            check = True
            rect9_4 = "Place"
          if rect9_5.collidepoint(x, y):
            check = True
            rect9_5 = "Place"
          if rect9_6.collidepoint(x, y):
            check = True
            rect9_6 = "Place"
          if rect9_7.collidepoint(x, y):
            check = True
            rect9_7 = "Place"
          if rect9_8.collidepoint(x, y):
            check = True
            rect9_8 = "Place"
          if rect9_9.collidepoint(x, y):
            check = True
            rect9_9 = "Place"
            
            
        if check:
          popup = pygame.Rect((x-5,y-5),(100,500))
          pygame.draw.rect(_VARS['surf'], BLACK, popup, 2 )
          button1 = writeText("Hospital", get_font2(30), LIME, _VARS['surf'], x+45, y +20 ) 
          button2 = writeText("Farm", get_font2(30), LIME, _VARS['surf'], x+45, y+60) 
          button3 = writeText("Restaurant", get_font2(25), LIME, _VARS['surf'], x+45, y + 100 ) 
          button4 = writeText("Hotel", get_font2(30), LIME, _VARS['surf'], x+45, y+140) 
          if event.type== pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(x,y):
                
                image = pygame.image.load("Assets/Hospital.png")
                if rect0_0 == "Place":
                  rect0_0B = image
                if rect0_1 == "Place":
                  rect0_1B = image
                if rect0_2 == "Place":
                  rect0_2B = image
                if rect0_3 == "Place":
                  rect0_3B = image
                if rect0_4 == "Place":
                  rect0_4B = image
                if rect0_5 == "Place":
                  rect0_5B = image
                if rect0_6 == "Place":
                  rect0_6B = image
                if rect0_7 == "Place":
                  rect0_7B = image
                if rect0_8 == "Place":
                  rect0_8B = image
                if rect0_9 == "Place":
                  rect0_9 == "Place"
                if rect1_0 == "Place":
                  rect1_0B = image
                if rect1_1 == "Place":
                  rect1_1B = image
                if rect1_2 == "Place":
                  rect1_2B = image
                if rect1_3 == "Place":
                  rect1_3B = image
                if rect1_4 == "Place":
                  rect1_4B = image
                if rect1_5 == "Place":
                  rect1_5B = image
                if rect1_6 == "Place":
                  rect1_6B = image
                if rect1_7 == "Place":
                  rect1_7B = image
                if rect1_8 == "Place":
                  rect1_8B = image
                if rect1_9 == "Place":
                  rect1_9 == "Place"
                if rect2_0 == "Place":
                  rect2_0B = image
                if rect2_1 == "Place":
                  rect2_1B = image
                if rect2_2 == "Place":
                  rect2_2B = image
                if rect2_3 == "Place":
                  rect2_3B = image
                if rect2_4 == "Place":
                  rect2_4B = image
                if rect2_5 == "Place":
                  rect2_5B = image
                if rect2_6 == "Place":
                  rect2_6B = image
                if rect2_7 == "Place":
                  rect2_7B = image
                if rect2_8 == "Place":
                  rect2_8B = image
                if rect2_9 == "Place":
                  rect2_9 == "Place"
                if rect3_0 == "Place":
                  rect3_0B = image
                if rect3_1 == "Place":
                  rect3_1B = image
                if rect3_2 == "Place":
                  rect3_2B = image
                if rect3_3 == "Place":
                  rect3_3B = image
                if rect4_4 == "Place":
                  rect4_4B = image
                if rect5_5 == "Place":
                  rect5_5B = image
                if rect5_6 == "Place":
                  rect5_6B = image
                if rect5_7 == "Place":
                  rect5_7B = image
                if rect5_8 == "Place":
                  rect5_8B = image
                if rect5_9 == "Place":
                  rect5_9 == "Place"
                if rect6_0 == "Place":
                  rect6_0B = image
                if rect6_1 == "Place":
                  rect6_1B = image
                if rect6_2 == "Place":
                  rect6_2B = image
                if rect6_3 == "Place":
                  rect6_3B = image
                if rect6_4 == "Place":
                  rect6_4B = image
                if rect6_5 == "Place":
                  rect6_5B = image
                if rect6_6 == "Place":
                  rect6_6B = image
                if rect6_7 == "Place":
                  rect6_7B = image
                if rect6_8 == "Place":
                  rect6_8B = image
                if rect6_9 == "Place":
                  rect6_9 == "Place"
                if rect7_0 == "Place":
                  rect7_0B = image
                if rect7_1 == "Place":
                  rect7_1B = image
                if rect7_2 == "Place":
                  rect7_2B = image
                if rect7_3 == "Place":
                  rect7_3B = image
                if rect7_4 == "Place":
                  rect7_4B = image
                if rect7_5 == "Place":
                  rect7_5B = image
                if rect7_6 == "Place":
                  rect7_6B = image
                if rect7_7 == "Place":
                  rect7_7B = image
                if rect7_8 == "Place":
                  rect7_8B = image
                if rect7_9 == "Place":
                  rect7_9 == "Place"
                if rect8_0 == "Place":
                  rect8_0B = image
                if rect8_1 == "Place":
                  rect8_1B = image
                if rect8_2 == "Place":
                  rect8_2B = image
                if rect8_3 == "Place":
                  rect8_3B = image
                if rect8_4 == "Place":
                  rect8_4B = image
                if rect8_5 == "Place":
                  rect8_5B = image
                if rect8_6 == "Place":
                  rect8_6B = image
                if rect8_7 == "Place":
                  rect8_7B = image
                if rect8_8 == "Place":
                  rect8_8B = image
                if rect8_9 == "Place":
                  rect9_9 == "Place"
                if rect9_0 == "Place":
                  rect9_0B = image
                if rect9_1 == "Place":
                  rect9_1B = image
                if rect9_2 == "Place":
                  rect9_2B = image
                if rect9_3 == "Place":
                  rect9_3B = image
                if rect9_4 == "Place":
                  rect9_4B = image
                if rect9_5 == "Place":
                  rect9_5B = image
                if rect9_6 == "Place":
                  rect9_6B = image
                if rect9_7 == "Place":
                  rect9_7B = image
                if rect9_8 == "Place":
                  rect9_8B = image
                if rect9_9 == "Place":
                    rect9_9B = image
            if button2.collidepoint(x, y):
                print("Farm")         
                image = pygame.image.load("Assets/Hydroponic_Farm.png")
            if button3.collidepoint(x,y):
                print("Restaurant")
                image = pygame.image.load("Assets/Restaurant.png")
            if button4.collidepoint(x, y):
                print("Hotel")         
                image = pygame.image.load("Assets/AirQuality.png")
          if popup.collidepoint(x, y) == False:
            print ("false")
            check = False
        
            loop = False
        
        pygame.display.update()

def placeBuilding(image, point):
    _VARS['surf'].blit(image, point)
    pygame.display.update()


def main_ocean():
    health = 100
    population = 0
    money = 1000000000
    red = 0
    blue = 0
    green = 0
    ascending = True    
    pygame.display.set_caption("Your Space Colony")
    BG = pygame.image.load("Assets/OceanBackGround.gif")
    BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
    while True:
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
        _VARS['surf'].fill((red, blue, green))
        _VARS['surf'].blit(BG, (0, 0))
        writeText("This is the Ocean Planet", get_font2(75), WHITE, _VARS['surf'], WINDOW_WIDTH / 2, 100)
        hud(health, population, money)
        # PLacing tiles first to avoid tile border issues
        placeISOTiles()
        
        drawIsometricGrid(_VARS['isoGridOrigin'],
                          _VARS['gridSize'],
                          _VARS['cellSize'])
        checkEvents()
        
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
        pygame.display.update()


def main_rocky():
    health = 100
    population = 0
    money = 1000000000
    red = 0
    blue = 0
    green = 0
    ascending = True    
    check = False
    pygame.display.set_caption("Your Space Colony")
    BG = pygame.image.load("Assets/RockyBackGround.png")
    BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
    while True:
        
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
        _VARS['surf'].fill((red, blue, green))
        _VARS['surf'].blit(BG, (0, 0))
        writeText("This is the Rocky Planet", get_font2(75), WHITE, _VARS['surf'], WINDOW_WIDTH / 2, 100)
        hud(health, population, money)
        # PLacing tiles first to avoid tile border issues
        placeISOTiles()
        
        drawIsometricGrid(_VARS['isoGridOrigin'],
                          _VARS['gridSize'],
                          _VARS['cellSize'])

        checkEvents()
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
        time.sleep(.0001)

def main_mystery():
    health = 100
    population = 0
    money = 1000000000
    red = 0
    blue = 0
    green = 0
    ascending = True  
    pygame.display.set_caption("Your Space Colony")  
    BG = pygame.image.load("Assets/pixil-frame-0.png")
    BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
    while True:
        
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
        _VARS['surf'].fill((red, blue, green))
        _VARS['surf'].blit(BG, (0, 0))
        writeText("This is the Mystery Planet", get_font2(75), WHITE, _VARS['surf'], WINDOW_WIDTH / 2, 100)
        hud(health, population, money)
        # PLacing tiles first to avoid tile border issues
        placeISOTiles()
        
        drawIsometricGrid(_VARS['isoGridOrigin'],
                          _VARS['gridSize'],
                          _VARS['cellSize'])
        checkEvents()
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
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
        if rect0_0.collidepoint(x, y):
            point = [point0_0[0]+ 2, point0_0[1] -9.5]
            print(image)
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect0_0)
            placeBuilding(image, point0_0)
            pygame.display.update()
        if rect1_0.collidepoint(x, y):
            point = [point1_0[0]+ 2, point1_0[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect1_0) 
            _VARS['surf'].blit(image, point1_0)
        if rect2_0.collidepoint(x, y):
            point = [point2_0[0]+ 2, point2_0[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect2_0) 
        if rect3_0.collidepoint(x, y):
            point = [point3_0[0]+ 2, point3_0[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect3_0) 
        if rect4_0.collidepoint(x, y):
            point = [point4_0[0]+ 2, point4_0[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect4_0) 
        if rect5_0.collidepoint(x, y):
            point = [point5_0[0]+ 2, point5_0[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect5_0) 
        if rect6_0.collidepoint(x, y):
            point = [point6_0[0]+ 2, point6_0[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect6_0) 
        if rect7_0.collidepoint(x, y):
            point = [point7_0[0]+ 2, point7_0[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect7_0) 
        if rect8_0.collidepoint(x, y):
            point = [point8_0[0]+ 2, point8_0[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect8_0) 
        if rect9_0.collidepoint(x, y):
            point = [point9_0[0]+ 2, point9_0[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect9_0) 
        if rect0_1.collidepoint(x, y):
            point = [point0_1[0]+ 2, point0_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect0_1) 
        if rect1_1.collidepoint(x, y):
            point = [point1_1[0]+ 2, point1_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect1_1) 
        if rect2_1.collidepoint(x, y):
            point = [point2_1[0]+ 2, point2_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect2_1) 
        if rect3_1.collidepoint(x, y):
            point = [point3_1[0]+ 2, point3_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect3_1) 
        if rect4_1.collidepoint(x, y):
            point = [point4_1[0]+ 2, point4_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)   
            popUp(rect4_1)  
        if rect5_1.collidepoint(x, y):
            point = [point5_1[0]+ 2, point5_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect5_1)     
        if rect6_1.collidepoint(x, y):
            point = [point6_1[0]+ 2, point6_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect6_1)            
        if rect7_1.collidepoint(x, y):
            point = [point7_1[0]+ 2, point7_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect7_1)   
        if rect8_1.collidepoint(x, y):
            point = [point8_1[0]+ 2, point8_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect8_1)    
        if rect9_1.collidepoint(x, y):
            point = [point9_1[0]+ 2, point9_1[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect9_1)    
        if rect0_2.collidepoint(x, y):
            point = [point0_2[0]+ 2, point0_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect0_2)   
        if rect1_2.collidepoint(x, y):
            point = [point1_2[0]+ 2, point1_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect1_2) 
        if rect2_2.collidepoint(x, y):
            point = [point2_2[0]+ 2, point2_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect2_2)  
        if rect3_2.collidepoint(x, y):
            point = [point3_2[0]+ 2, point3_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect3_2) 
        if rect4_2.collidepoint(x, y):
            point = [point4_2[0]+ 2, point4_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect4_2)  
        if rect5_2.collidepoint(x, y):
            point = [point5_2[0]+ 2, point5_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect5_2) 
        if rect6_2.collidepoint(x, y):
            point = [point6_2[0]+ 2, point6_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect6_2) 
        if rect7_2.collidepoint(x, y):
            point = [point7_2[0]+ 2, point7_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect7_2) 
        if rect8_2.collidepoint(x, y):
            point = [point8_2[0]+ 2, point8_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect8_2)  
        if rect9_2.collidepoint(x, y):
            point = [point9_2[0]+ 2, point9_2[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect9_2)  
        if rect0_3.collidepoint(x, y):
            point = [point0_3[0]+ 2, point0_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)   
            popUp(rect0_3) 
        if rect1_3.collidepoint(x, y):
            point = [point1_3[0]+ 2, point1_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect1_3)  
        if rect2_3.collidepoint(x, y):
            point = [point2_3[0]+ 2, point2_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect2_3)
        if rect3_3.collidepoint(x, y):
            point = [point3_3[0]+ 2, point3_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect3_3) 
        if rect4_3.collidepoint(x, y):
            point = [point4_3[0]+ 2, point4_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect4_3) 
        if rect5_3.collidepoint(x, y):
            point = [point5_3[0]+ 2, point5_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect5_3)  
        if rect6_3.collidepoint(x, y):
            point = [point6_3[0]+ 2, point6_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect6_3)  
        if rect7_3.collidepoint(x, y):
            point = [point7_3[0]+ 2, point7_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect7_3)  
        if rect8_3.collidepoint(x, y):
            point = [point8_3[0]+ 2, point8_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect8_3) 
        if rect9_3.collidepoint(x, y):
            point = [point9_3[0]+ 2, point9_3[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect9_3) 
        if rect0_4.collidepoint(x, y):
            point = [point0_4[0]+ 2, point0_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect0_4)  
        if rect1_4.collidepoint(x, y):
            point = [point1_4[0]+ 2, point1_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect1_4)  
        if rect2_4.collidepoint(x, y):
            point = [point2_4[0]+ 2, point2_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect2_4)  
        if rect3_4.collidepoint(x, y):
            point = [point3_4[0]+ 2, point3_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect3_4)  
        if rect4_4.collidepoint(x, y):
            point = [point4_4[0]+ 2, point4_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect4_4)  
        if rect5_4.collidepoint(x, y):
            point = [point5_4[0]+ 2, point5_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect5_4)  
        if rect6_4.collidepoint(x, y):
            point = [point6_4[0]+ 2, point6_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect6_4)  
        if rect7_4.collidepoint(x, y):
            point = [point7_4[0]+ 2, point7_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect7_4)  
        if rect8_4.collidepoint(x, y):
            point = [point8_4[0]+ 2, point8_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect8_4)  
        if rect9_4.collidepoint(x, y):
            point = [point9_4[0]+ 2, point9_4[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect9_4)  
        if rect0_5.collidepoint(x, y):
            point = [point0_5[0]+ 2, point0_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)   
            popUp(rect0_5)  
        if rect1_5.collidepoint(x, y):
            point = [point1_5[0]+ 2, point1_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect1_5)  
        if rect2_5.collidepoint(x, y):
            point = [point2_5[0]+ 2, point2_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect2_5)  
        if rect3_5.collidepoint(x, y):
            point = [point3_5[0]+ 2, point3_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect3_5)   
        if rect4_5.collidepoint(x, y):
            point = [point4_5[0]+ 2, point4_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect4_5)   
        if rect5_5.collidepoint(x, y):
            point = [point5_5[0]+ 2, point5_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect5_5)  
        if rect6_5.collidepoint(x, y):
            point = [point6_5[0]+ 2, point6_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect6_5)   
        if rect7_5.collidepoint(x, y):
            point = [point7_5[0]+ 2, point7_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect7_5)   
        if rect8_5.collidepoint(x, y):
            point = [point8_5[0]+ 2, point8_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect8_5)  
        if rect9_5.collidepoint(x, y):
            point = [point9_5[0]+ 2, point9_5[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect9_5)  
        if rect0_6.collidepoint(x, y):
            point = [point0_6[0]+ 2, point0_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect0_6)  
        if rect1_6.collidepoint(x, y):
            point = [point1_6[0]+ 2, point1_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect1_6)  
        if rect2_6.collidepoint(x, y):
            point = [point2_6[0]+ 2, point2_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect2_6) 
        if rect3_6.collidepoint(x, y):
            point = [point3_6[0]+ 2, point3_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect3_6) 
        if rect4_6.collidepoint(x, y):
            point = [point4_6[0]+ 2, point4_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect4_6) 
        if rect5_6.collidepoint(x, y):
            point = [point5_6[0]+ 2, point5_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect5_6) 
        if rect6_6.collidepoint(x, y):
            point = [point6_6[0]+ 2, point6_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect6_6)  
        if rect7_6.collidepoint(x, y):
            point = [point7_6[0]+ 2, point7_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect7_6)  
        if rect8_6.collidepoint(x, y):
            point = [point8_6[0]+ 2, point8_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect8_6) 
        if rect9_6.collidepoint(x, y):
            point = [point9_6[0]+ 2, point9_6[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect9_6)  
        if rect0_7.collidepoint(x, y):
            point = [point0_7[0]+ 2, point0_7[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect0_7)  
        if rect1_7.collidepoint(x, y):
            point = [point1_7[0]+ 2, point1_7[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect1_7)  
        if rect2_7.collidepoint(x, y):
            point = [point2_7[0]+ 2, point2_7[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect2_7)  
        if rect3_7.collidepoint(x, y):
            point = [point3_7[0]+ 2, point3_7[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect3_7)  
        if rect4_7.collidepoint(x, y):
            point = [point4_7[0]+ 2, point4_7[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect4_7)   
        if rect5_7.collidepoint(x, y):
            point = [point5_7[0]+ 2, point5_7[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect5_7)   
        if rect6_7.collidepoint(x, y):
            point = [point6_7[0]+ 2, point6_7[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect6_7)   
        if rect7_7.collidepoint(x, y):
            point = [point7_7[0]+ 2, point7_7[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect7_7)   
        if rect8_7.collidepoint(x, y):
            point = [point8_7[0]+ 2, point8_7[1] -9.5]
            #placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect8_7)  
        if rect9_7.collidepoint(x, y):
            point = [point9_7[0]+ 2, point9_7[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)
            popUp(rect9_7)    
        if rect0_8.collidepoint(x, y):
            point = [point0_8[0]+ 2, point0_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect0_8)   
        if rect1_8.collidepoint(x, y):
            point = [point1_8[0]+ 2, point1_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect1_8)   
        if rect2_8.collidepoint(x, y):
            point = [point2_8[0]+ 2, point2_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect2_8)   
        if rect3_8.collidepoint(x, y):
            point = [point3_8[0]+ 2, point3_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect3_8)   
        if rect4_8.collidepoint(x, y):
            point = [point4_8[0]+ 2, point4_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect4_8)   
        if rect5_8.collidepoint(x, y):
            point = [point5_8[0]+ 2, point5_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect5_8)  
        if rect6_8.collidepoint(x, y):
            point = [point6_8[0]+ 2, point6_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect6_8)  
        if rect7_8.collidepoint(x, y):
            point = [point7_8[0]+ 2, point7_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect7_8)   
        if rect8_8.collidepoint(x, y):
            point = [point8_8[0]+ 2, point8_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect8_8)   
        if rect9_8.collidepoint(x, y):
            point = [point9_8[0]+ 2, point9_8[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect9_8)  
        if rect0_9.collidepoint(x, y):
            point = [point0_9[0]+ 2, point0_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect0_9)   
        if rect1_9.collidepoint(x, y):
            point = [point1_9[0]+ 2, point1_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect1_9)   
        if rect2_9.collidepoint(x, y):
            point = [point2_9[0]+ 2, point2_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect2_9)  
        if rect3_9.collidepoint(x, y):
            point = [point3_9[0]+ 2, point3_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect3_9)   
        if rect4_9.collidepoint(x, y):
            point = [point4_9[0]+ 2, point4_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect4_9)   
        if rect5_9.collidepoint(x, y):
            point = [point5_9[0]+ 2, point5_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect5_9)  
        if rect6_9.collidepoint(x, y):
            point = [point6_9[0]+ 2, point6_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect6_9)   
        if rect7_9.collidepoint(x, y):
            point = [point7_9[0]+ 2, point7_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect7_9)   
        if rect8_9.collidepoint(x, y):
            point = [point8_9[0]+ 2, point8_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50) 
            popUp(rect8_9)   
        if rect9_9.collidepoint(x, y):
            point = [point9_9[0]+ 2, point9_9[1] -9.5]
            placeISOTile(isoToCart(point), YELLOW, 50)  
            popUp(rect9_9)  
        pygame.display.update()

#-------------------End---------------------


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        _VARS['surf'].fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True,
                                           "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        _VARS['surf'].blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None,
                              pos=(640, 460),
                              text_input="BACK",
                              font=get_font(75),
                              base_color="Black",
                              hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(_VARS['surf'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
username = ''
def inputName():
    clock = pygame.time.Clock()

    # it will display on screen

    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    # create rectangle
    input_rect = pygame.Rect(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT / 2 - 16,
                             100, 32)

    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')

    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    BG = pygame.image.load("Assets/MenuScreenBackGround.jpg")
    BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))

 
    active = False
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    screen.blit(BG, (0, 0))
    Blurb1 = get_font2(30).render("You are an eccentric billionaire, who has dared to venture into the enterprise of space travel.", True, "#42f5bf")
    Blurb2 = get_font2(30).render("You have taken money from your own pocket fund the start of an offworld colony.", True, "#42f5bf")
    Blurb3 = get_font2(30).render("The journey of established an offworld colony is dangerous, but rewarding.  ", True, "#42f5bf")
    Blurb4 = get_font2(30).render("The press wants to know: What do you call yourself, and what will you call your colony?", True, "#42f5bf")
    Blurb5 = get_font2(30).render("Now pick your planet. Choose carefully, because there may be unseeen ramifications later in the game.", True, "#42f5bf")
    Blurb_Loc1 = Blurb1.get_rect(center = (640, 60))
    screen.blit(Blurb1, Blurb_Loc1)
    Blurb_Loc2 = Blurb2.get_rect(center = (640, 85))
    screen.blit(Blurb2, Blurb_Loc2)
    Blurb_Loc3 = Blurb3.get_rect(center = (640, 110))
    screen.blit(Blurb3, Blurb_Loc3)
    Blurb_Loc4 = Blurb4.get_rect(center = (640, 135))
    screen.blit(Blurb4, Blurb_Loc4)
    Blurb_Loc5 = Blurb5.get_rect(center = (640, 160))
    screen.blit(Blurb5, Blurb_Loc5)
  
    NAME_TEXT = get_font(50).render("Please input your name", True, "#b68f40")
    NAME_RECT = NAME_TEXT.get_rect(center=(640, 300))

    screen.blit(NAME_TEXT, NAME_RECT)
    
    while True:
        for event in pygame.event.get():

            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    print(user_text)
                    username = user_text
                    loop = False
                    planetSelection()
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

        # it will set background color of screen
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.display.update()
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255))

        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+15, input_rect.y+10))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 5)

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()

        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


def planetSelection():
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            _VARS['surf'].fill((WHITE))
            BG = pygame.image.load("Assets/MenuScreenBackGround.jpg")
            BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
            _VARS['surf'].blit(BG, (0, 0))

            #Image of the Rocky Planet
            planet1 = pygame.image.load("Assets/Rocky Planet.png")
            planet1 = pygame.transform.scale(planet1, (200, 170))
            _VARS['surf'].blit(planet1, (100, 200))

            #Image of the Ocean Planet
            planet2 = pygame.image.load("Assets/Ocean Planet.png")
            planet2 = pygame.transform.scale(planet2, (200, 170))
            _VARS['surf'].blit(planet2, (WINDOW_WIDTH/2-100, WINDOW_HEIGHT-350))

            #Image of the Mystery Planet
            planet3 = pygame.image.load("Assets/Mystery Planet.png")
            planet3 = pygame.transform.scale(planet3, (200, 170))
            _VARS['surf'].blit(planet3, (WINDOW_WIDTH-400, 100))

            #Back Button in Planet Selection
            PLANET_MOUSE_POS = pygame.mouse.get_pos()
    
            PLANET_BACK = Button(image=None,
                          pos=(640, 260),
                          text_input="BACK",
                          font=get_font2(75),
                          base_color="Black",
                          hovering_color="Green")

            PLANET_BACK.changeColor(PLANET_MOUSE_POS)
            PLANET_BACK.update(_VARS['surf'])

            button1_color = Button(image=None, pos = (WINDOW_WIDTH / 2 - 440, 375), text_input = "Rocky Planet", font = get_font2(50),
                                    base_color=WHITE, hovering_color="Gold")
            button1_color.changeColor(pygame.mouse.get_pos())
            button1_color.update(_VARS['surf'])

            button2_color = Button(image=None, pos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT-150), text_input = "Ocean Planet", font = get_font2(50),
                                    base_color=WHITE, hovering_color="Gold")
            button2_color.changeColor(pygame.mouse.get_pos())
            button2_color.update(_VARS['surf'])

            button3_color = Button(image=None, pos = (WINDOW_WIDTH - 300, 80), text_input = "Mystery Planet", font = get_font2(50),
                                    base_color=WHITE, hovering_color="Gold")
            button3_color.changeColor(pygame.mouse.get_pos())
            button3_color.update(_VARS['surf'])


            button1 = writeText("                 ", get_font2(50), WHITE, _VARS['surf'],
                                WINDOW_WIDTH / 2 - 440, 375)
            button2 = writeText("                 ", get_font2(50), WHITE, _VARS['surf'],
                                WINDOW_WIDTH / 2, WINDOW_HEIGHT-150)
            button3 = writeText("                     ", get_font2(50), WHITE, _VARS['surf'],
                                WINDOW_WIDTH - 300, 80)
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:               #If you click the back button
                    if PLANET_BACK.checkForInput(PLANET_MOUSE_POS):
                        main_menu()
                x, y = pygame.mouse.get_pos()
                if button1.collidepoint(x, y) == True:

                    loop = False
                    main_rocky()
                if button2.collidepoint(x, y) == True:

                    loop = False
                    main_ocean()

                if button3.collidepoint(x, y) == True:
                    loop = False
                    main_mystery()

            pygame.display.update()




#Inital Screen
def main_menu():
    while True:
        _VARS['surf'].blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"),
                             pos=(640, 250),
                             text_input="PLAY",
                             font=get_font(75),
                             base_color="#d7fcd4",
                             hovering_color="White")
        OPTIONS_BUTTON = Button(
            image=pygame.image.load("Assets/Options Rect.png"),
            pos=(640, 400),
            text_input="OPTIONS",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/Quit Rect.png"),
                             pos=(640, 550),
                             text_input="QUIT",
                             font=get_font(75),
                             base_color="#d7fcd4",
                             hovering_color="White")

        _VARS['surf'].blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(_VARS['surf'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    inputName()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


#Synopsis of Game Play
# main_menu() --> inputName() --> planetSelection() --> mainGame(plant)
main_menu()
