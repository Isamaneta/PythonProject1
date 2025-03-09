#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.key

from code.entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple, jump_key):
        super().__init__(name, position)

        self.initial_position = position  # Posição inicial
        self.rect.topleft = position  # Ajusta a posição inicial
        self.jump_key = jump_key  # Tecla para pular
        self.is_jumping = False  # Verifica se o jogador está pulando
        self.velocity_y = 5  # Velocidade vertical
        self.gravity = 1  # Gravidade aplicada constantemente
        self.jump_force = -30  # Força do pulo

    def update(self):
        self.move()

    def move(self):
        pressed_key = pygame.key.get_pressed()

        # Verifica se a tecla de pulo foi pressionada e se o jogador está no chão
        if pressed_key[self.jump_key] and self.rect.bottom >= self.initial_position[1] and not self.is_jumping:
            self.velocity_y = self.jump_force
            self.is_jumping = True  # Marca que o jogador começou a pular

        # Aplica a gravidade
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Garante que o player para exatamente no chão
        if self.rect.bottom > self.initial_position[1]:
            self.rect.bottom = self.initial_position[1]  # Ajusta a posição exata
            self.velocity_y = 0  # Reseta a velocidade
            self.is_jumping = False  # O jogador pode pular novamente
        pass



