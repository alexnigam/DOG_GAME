import pygame as pg
import pygame.freetype as pf
# import sprite as sp


class Knopki():
    def __init__(self, image, text, x, y, game, function):
        self.image = image
        self.image1 = image
        self.text = text
        self.image = pg.transform.scale(self.image, [150, 45])
        self.image1 = self.image
        self.rect = pg.Rect([x, y], self.image.get_size())
        self.game = game
        self.otrisovka_texta = pf.Font(None, 15)
        self.function = function
        x = self.otrisovka_texta.render(text)
        self.text_kartinka = x[0]
        self.text_rect = x[1]
        self.text_rect.center = self.rect.center
        self.time = 2

    def draw(self):
        self.game.okno.blit(self.image, self.rect)
        self.game.okno.blit(self.text_kartinka, self.text_rect)

    def nazhali(self, x, y):
        self.time = pg.time.get_ticks() 
        self.image = pg.image.load(r'images\button_clicked.png')
        self.image = pg.transform.scale(self.image, [150, 45])
        self.rect = pg.Rect([x, y], self.image.get_size())

    def update(self):
        if pg.time.get_ticks() - self.time >= 300:
            self.image = self.image1
