import pygame as pg
import pygame.freetype as pf
import settings as st
import os
import random


class Toy():
    kartinki = os.listdir(r'images\toys')

    def __init__(self, game):
        self.image = pg.image.load(r'images\toys\\' + Toy.kartinki[random.randint(0,2)])
        self.image = pg.transform.scale(self.image, [100, 100])
        self.rect = pg.Rect([random.randint(100, st.SCREEN_WIDTH-100), 0], self.image.get_size())
        self.game = game

    def draw(self):
        self.game.okno.blit(self.image, self.rect)

    def update(self):
        self.rect.y += 3
