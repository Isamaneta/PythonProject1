#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_BLUE, MENU_OPTION, WIN_HEIGHT
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
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
        player1 = EntityFactory.get_entity('Player1', position=(0, WIN_HEIGHT - 0))
        if player1:
            self.entity_list.append(player1)
        else:
            print("⚠ Erro: Falha ao criar Player1")

        # Criando o Player2 se estiver em modo multiplayer
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player2 = EntityFactory.get_entity('Player2', position=(300, WIN_HEIGHT - 0))
            if player2:
                self.entity_list.append(player2)
            else:
                print("⚠ Erro: Falha ao criar Player2")

        self.timeout = 20000  # 20 segundos

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(90)
            for ent in self.entity_list:
                if ent is None:  # Evita erro caso alguma entidade seja None
                    print("⚠ Aviso: Pulando entidade NoneType")
                    continue

                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Atualiza a tela com as informações
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_BLUE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_BLUE, (10, 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_BLUE, (10, 20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
