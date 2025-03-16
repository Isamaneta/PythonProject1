import pygame
from code.Const import WIN_WIDTH
from code.background import Background
from code.enemy import Enemy
from code.player import Player

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                try:
                    return Player('player1',position, pygame.K_SPACE)
                except Exception as e:
                    print(f"Error creating Player1: {e}")
                    return None

            case 'Player2':
                try:
                    return Player('player2', position, pygame.K_UP)
                except Exception as e:
                    print(f"Error creating Player2: {e}")
                    return None

            case 'EnemyCactus2':
                return Enemy('EnemyCactus2', (0, 569))  # Ajuste na posição Y

            case 'EnemyRock2':
                return Enemy('EnemyRock2', (0, 545))  # Ajuste na posição Y

            case _:
                print(f"Warning: Entity '{entity_name}' not recognized")
                return None


















