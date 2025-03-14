#C
import pygame

COLOR_BLACK = (5,0,10)
C_BLUE = (0,35,245)
COLOR_ORANGE =(240,134,80)

#E
EVENT_ENEMY =pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'player1'   : 5,
    'player2'   : 4,
    'EnemyCactus2':2,
    'EnemyRock2'  :3,
    }

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'player1': 300,
    'player2': 300,
    'EnemyRock2': 50,
    'EnemyCactus2': 60,
}

#M
#C
import pygame

COLOR_BLACK = (5,0,10)
C_BLUE = (0,35,245)
COLOR_ORANGE =(240,134,80)

#E
EVENT_ENEMY =pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'player1'   : 5,
    'player2'   : 4,
    'EnemyCactus2':2,
    'EnemyRock2'  :3,
    }

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'player1': 300,
    'player2': 300,
    'EnemyRock2': 50,
    'EnemyCactus2': 60,
}

#M
MENU_OPTION = (' NEW GAME 1P',
               ' NEW GAME 2P - COOPERATIVE',
               ' NEW GAME 2P - COMPETITIVE',
               ' SCORE',
               ' EXIT')

#P
PLAYER1 = pygame.K_SPACE
PLAYER2 = pygame.K_UP

#S
SPAWN_TIME = 4000


# W
WIN_WIDTH = 920
WIN_HEIGHT = 600


