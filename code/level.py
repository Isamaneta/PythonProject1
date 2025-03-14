#!/usr/bin/python
# -*- coding: utf-8 -*-
# !/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_BLUE, MENU_OPTION, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME
from code.EntityMediator import EntityMediator
from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo
        self.entity_list: list[Entity] = []

        # Criando o background
        bg_entities = EntityFactory.get_entity('Level1Bg')
        if bg_entities:
            self.entity_list.extend(bg_entities)
        else:
            print("⚠ Erro: Falha ao criar Level1Bg")

        # Criando o Player1
        player1 = EntityFactory.get_entity('Player1', position=(0, WIN_HEIGHT - 0))  # Ajuste para o chão
        if player1:
            self.entity_list.append(player1)
        else:
            print("⚠ Erro: Falha ao criar Player1")

        # Criando o Player2 se estiver em modo multiplayer
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player2 = EntityFactory.get_entity('Player2', position=(300, WIN_HEIGHT - 0))  # Ajuste para o chão
            if player2:
                self.entity_list.append(player2)
            else:
                print("⚠ Erro: Falha ao criar Player2")

        # Configurando o timer para adicionar inimigos
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Adicionar inimigo a cada 2 segundos

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(90)  # Controla a taxa de quadros

            # Atualiza as entidades
            for ent in self.entity_list:
                if ent is None:  # Evita erro caso alguma entidade seja None
                    continue
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # Verifica os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:  # Se o evento de inimigo ocorrer
                    choice = random.choice(('EnemyCactus2','EnemyRock2'))
                    new_enemy = EntityFactory.get_entity(choice)
                    if new_enemy:
                        self.entity_list.append(new_enemy)  # Adiciona o inimigo à lista de entidades
                    else:
                        print("Erro ao criar inimigo")

            # Atualiza a tela com informações
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_BLUE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_BLUE, (10, 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_BLUE, (10, 20))
            pygame.display.flip()
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
