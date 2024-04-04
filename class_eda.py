import pygame as pg
import pygame.freetype as pf
import settings as st
import os
import random
class Eda():
    def __init__(self, image, game) -> None:
        self.image = pg.image.load('images/food/' + image)
        self.game = game
        self.image = pg.transform.scale(self.image, [self.game.dog.rect.w//2,self.game.dog.rect.h//2])
        self.rect = pg.Rect(self.game.dog.rect.center, self.image.get_size())
        self.rect.center = [st.SCREEN_WIDTH//2, st.SCREEN_HEIGHT//2+15]
        self.kupleno = False
        self.cost = random.randint(10,100)

    def draw(self):
        self.game.okno.blit(self.image, self.rect)
        otrisovka_cost = pf.Font(None, 20)
        otrisovka_cost.render_to(self.game.okno, [self.rect.right + 10, self.rect.centery], str(self.cost ), [170, 100, 50])
