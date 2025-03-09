#C
import pygame

COLOR_BLACK = (5,0,10)
C_BLUE = (0,35,245)
COLOR_ORANGE =(240,134,80)

ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'player1'   : 3,
}

#M
MENU_OPTION = (' NEW GAME 1P',
               ' NEW GAME 2P - COOPERATIVE',
               ' NEW GAME 2P - COMPETITIVE',
               ' SCORE',
               ' EXIT')

#P
PLAYER1 = (pygame.K_SPACE)
PLAYER2 = (pygame.K_UP)


# W
WIN_WIDTH = 920
WIN_HEIGHT = 600


def PLAYER_KEY_SPACE():
    return None