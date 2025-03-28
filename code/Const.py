#C
import pygame

C_BLACK = (5, 0, 10)
C_BLUE = (0,35,245)
C_ORANGE =(240, 134, 80)
C_WHITE = (255, 255, 255)

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'player1' :1,
    'EnemyRock2':1,
    'player2' :1,
    'EnemyCactus2':1,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'player1': 10,
    'player2': 10,
    'EnemyRock2': 1,
    'EnemyCactus2': 1,
}

#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'player1'   : 5,
    'player2'   : 4,
    'EnemyCactus2':2,
    'EnemyRock2'  :3,
    }

#M
MENU_OPTION = (' NEW GAME 1P',
               ' NEW GAME 2P - COOPERATIVE',
               ' NEW GAME 2P - COMPETITIVE',
               ' EXIT')

#P
PLAYER1 = pygame.K_SPACE
PLAYER2 = pygame.K_UP

#S
SPAWN_TIME = 2000

#T
TIMEOUT_STEP = 100 #100MS
TIMEOUT_LEVEL = 10000 # 10S

# W
WIN_WIDTH = 920
WIN_HEIGHT = 600