import pygame, sys
from button import Button
from tkinter import CENTER
import time, random
from pygame.locals import *
#Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#fonts = pygame.font.Font(None, 80)
#Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
#font = pygame.font.SysFont(None, 80)
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#pygame.display.set_caption("Space Colonization Simulator")
pygame.init()

pygame.display.set_caption("Menu")

BG = pygame.image.load("Assets/MenuScreenBackGround2.jpg")
BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))

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
    pygame.draw.rect(WINDOW, BLACK, button, 2)
    return button

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        WINDOW.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True,
                                           "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        WINDOW.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None,
                              pos=(640, 460),
                              text_input="BACK",
                              font=get_font(75),
                              base_color="Black",
                              hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

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

    active = False
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    Blurb1 = get_font2(30).render("You are an eccentric billionaire, who has dared to venture into the enterprise of space travel.", True, "#ff0000")
    Blurb2 = get_font2(30).render("You have taken money from your own pocket fund the start of an offworld colony.", True, "#ff0000")
    Blurb3 = get_font2(30).render("The journey of established an offworld colony is dangerous, but rewarding.  ", True, "#ff0000")
    Blurb4 = get_font2(30).render("The press wants to know: What do you call yourself, and what will you call your colony?", True, "#ff0000")
    Blurb5 = get_font2(30).render("Now pick your planet. Choose carefully, because there may be unseeen ramifications later in the game.", True, "#ff0000")
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
            WINDOW.fill((WHITE))
            BG = pygame.image.load("Assets/MenuScreenBackGround.jpg")
            BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
            WINDOW.blit(BG, (0, 0))

            #Image of the Rocky Planet
            planet1 = pygame.image.load("Assets/Rocky Planet.png")
            planet1 = pygame.transform.scale(planet1, (200, 170))
            WINDOW.blit(planet1, (100, 200))

            #Image of the Ocean Planet
            planet2 = pygame.image.load("Assets/Ocean Planet.png")
            planet2 = pygame.transform.scale(planet2, (200, 170))
            WINDOW.blit(planet2, (WINDOW_WIDTH/2-100, WINDOW_HEIGHT-350))

            #Image of the Mystery Planet
            planet3 = pygame.image.load("Assets/Mystery Planet.png")
            planet3 = pygame.transform.scale(planet3, (200, 170))
            WINDOW.blit(planet3, (WINDOW_WIDTH-400, 100))

            #Back Button in Planet Selection
            PLANET_MOUSE_POS = pygame.mouse.get_pos()
    
            PLANET_BACK = Button(image=None,
                          pos=(640, 260),
                          text_input="BACK",
                          font=get_font2(75),
                          base_color="Black",
                          hovering_color="Green")

            PLANET_BACK.changeColor(PLANET_MOUSE_POS)
            PLANET_BACK.update(WINDOW)

          
            button1 = writeText("Rocky Planet", get_font2(50), WHITE, WINDOW,
                                WINDOW_WIDTH / 2 - 440, 375)
            button2 = writeText("Ocean Planet", get_font2(50), WHITE, WINDOW,
                                WINDOW_WIDTH / 2, WINDOW_HEIGHT-150)
            button3 = writeText("????", get_font2(50), WHITE, WINDOW,
                                WINDOW_WIDTH - 300, 80)
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:               #If you click the back button
                    if PLANET_BACK.checkForInput(PLANET_MOUSE_POS):
                        main_menu()
                        pygame.display.update()
                x, y = pygame.mouse.get_pos()
                if button1.collidepoint(x, y) == True:

                    loop = False
                    mainGame("The Rocky Planet")
                if button2.collidepoint(x, y) == True:

                    loop = False
                    mainGame("The Ocean Planet")

                if button3.collidepoint(x, y) == True:
                    loop = False
                    mainGame("The Mystery Planet")

            pygame.display.update()


def mainGame(plant):
    PLANET = plant

    #population = 0
    #money = 1,000,000,000
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            BG = pygame.image.load("Assets/Hack_bg1.jpg")
            BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
            WINDOW.fill((WHITE))
            WINDOW.blit(BG, (0, 0))

            writeText("This is " + PLANET, get_font2(75), BLACK, WINDOW,
                      WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            pygame.display.update()








def main_menu():
    while True:
        WINDOW.blit(BG, (0, 0))

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

        WINDOW.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WINDOW)

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


main_menu()
