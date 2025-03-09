#!/usr/bin/python
# -*- coding: utf-8 -*-
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
                    bg_name = f'Level1Bg{i}'
                    try:
                        list_bg.append(Background(bg_name, (0, 0)))
                        list_bg.append(Background(bg_name, (WIN_WIDTH, 0)))
                    except Exception as e:
                        print(f"Error creating background {bg_name}: {e}")
                return list_bg if list_bg else None

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


















