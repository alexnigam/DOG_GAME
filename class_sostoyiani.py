import pygame as pg
import pygame.freetype as pf


class Sostyanie():
    def __init__(self, game,image, koord ):
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, [60, 60])
        self.rect = pg.Rect(koord, self.image.get_size())
        self.game = game
        self.znach = 100

    def draw(self):
        self.game.okno.blit(self.image, self.rect)
        otrisovka_znach = pf.Font(None, 20)
        otrisovka_znach.render_to(self.game.okno, [self.rect.right + 10, self.rect.centery], str(self.znach ), [255, 255, 255])

        
