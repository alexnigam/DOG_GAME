import pygame as pg
import pygame.freetype as pf
import settings as st
# import sprite as sp


class Dog():
    def __init__(self, game, size, name, money):
        self.name = name
        self.image = pg.image.load(r'images/dog.png')
        self.image = pg.transform.scale(self.image, size)
        self.game = game
        self.money = money
        self.rect = pg.Rect([250, 150], self.image.get_size())
        self.rect.center = [st.SCREEN_WIDTH//2, st.SCREEN_HEIGHT//2+15]

        

    def draw(self):
        self.game.okno.blit(self.image, self.rect)


class Dog_igra(Dog):
    def update(self):
        klavishi_igre = pg.key.get_pressed()
        if klavishi_igre[pg.K_RIGHT] is True:
            self.rect.x += 10
        if klavishi_igre[pg.K_LEFT] is True:
            self.rect.x -= 10
