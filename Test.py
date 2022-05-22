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
DISPLAYSURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.init()

pygame.display.set_caption("Menu")

BG = pygame.image.load("Assets/MenuScreenBackGround2.jpg")
BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
DISPLAYSURFACE.blit(BG, (0, 0))

#Setup Functions
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Assets/zerovelo.ttf", size)
def get_font2(size):
    return pygame.font.Font("Assets/SF Atarian System.ttf", size)



def make_popup():
    popupSurf = pygame.display.set_mode((100, 100))
    options = ['Attack',
               'Talk']
    for i in range(len(options)):
        textSurf = get_font2(30).render(options[i], 1, BLACK)
        textRect = textSurf.get_rect()
        top = textRect.top
        left = textRect.left
        top += pygame.font.Font.get_linesize(get_font2(30))
        popupSurf.blit(textSurf, textRect)
    popupRect = popupSurf.get_rect()
    popupRect.centerx = 100/2
    popupRect.centery = 100/2
    DISPLAYSURFACE.blit(popupSurf, popupRect)
    pygame.display.update()

make_popup()