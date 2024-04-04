import pygame as pg
import pygame.freetype as pf
import settings as st
import os
import random
class Clothes():
    def __init__(self, image, game ,kupleno ,nadeto, cost) -> None:
        self.image = pg.image.load('images/items/' + image)
        self.name = image
        self.game = game
        self.image = pg.transform.scale(self.image, self.game.dog.rect.size)
        self.rect = pg.Rect(self.game.dog.rect.topleft, self.image.get_size())
        self.kupleno = kupleno
        self.nadeto = nadeto
        self.cost = cost

    def object_to_dict(self):
        slovar = {'name':self.name, 'kupleno':self.kupleno, 'nadeto':self.nadeto, 'cost':self.cost}
        return slovar

    def draw(self):
        self.game.okno.blit(self.image, self.rect)


