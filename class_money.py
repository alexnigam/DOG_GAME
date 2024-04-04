import pygame as pg
import pygame.freetype as pf


class Money():
    def __init__(self, game):
        self.image = pg.image.load(r'images\money.png')
        self.image = pg.transform.scale(self.image, [60, 60])
        self.rect = pg.Rect([50, 250], self.image.get_size())
        self.game = game

    def draw(self):
        self.game.okno.blit(self.image, self.rect)
        otrisovka_money = pf.Font(None, 20)
        otrisovka_money.render_to(self.game.okno, [self.rect.right + 10, self.rect.centery], str(self.game.dog.money), [255, 255, 255])
