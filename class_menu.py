from settings import*
import pygame as pg
import class_button as cb
import class_dog as cd
import class_toy as ct
import pygame.freetype as pgfr
import os
import class_clothes
import class_eda
class Menu():
    def __init__(self, image, x, y, game):
        self.image = image
        self.image = pg.transform.scale(self.image, [SCREEN_WIDTH, SCREEN_HEIGHT] )
        self.rect = pg.Rect([x, y], self.image.get_size())
        self.game = game
        self.knopki = []
        self.event_toy = pg.USEREVENT
        pg.time.set_timer(self.event_toy, 1000)

    def draw(self):
        self.game.okno.blit(self.image, self.rect)

    def update(self):
        pass

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for i in self.knopki:
                    if i.rect.collidepoint(event.pos):
                        i.function()
                        i.nazhali(i.rect.x, i.rect.y)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.game.menu = None
            self.local_event(event)

    def local_event(self, event):
        pass


class Clothes(Menu):
    def __init__(self, image, x, y, game):
        super().__init__(image, x, y, game)
        kartinki = os.listdir(r'images/items')
        knopka_image = pg.image.load(r'images\button.png')
        self.knopka1 = cb.Knopki(knopka_image, 'НАДЕТЬ', 150, 100, game, self.button_nadet )
        self.knopka2 = cb.Knopki(knopka_image, 'КУПИТЬ', 600, 100, game, self.button_kupit)
        self.knopka3 = cb.Knopki(knopka_image, 'НАЗАД', 150, 350, game, self.button_nazad )
        self.knopka4 = cb.Knopki(knopka_image, 'ВПЕРЕД', 600, 350, game, self.button_vpered )
        self.knopki = [self.knopka1, self.knopka2, self.knopka3, self.knopka4]
        self.odezhda = []
        self.number_odezhda = 0
        for i in self.game.test_sch['clothes']:
            a = class_clothes.Clothes(i['name'], self.game,i['kupleno'], i['nadeto'],i['cost'])
            self.odezhda.append(a)

    def objects_to_dict(self):
        spisok = []
        for i in self.odezhda:
            spisok.append(i.object_to_dict())
        return spisok

    def button_nadet(self):
        if self.odezhda[self.number_odezhda].kupleno is True:
            self.odezhda[self.number_odezhda].nadeto = True

    def button_kupit(self):
        if self.odezhda[self.number_odezhda].cost < self.game.dog.money:
            self.odezhda[self.number_odezhda].kupleno = True
            if self.game.udovl.znach <= 90:
                self.game.udovl.znach +=10
            else:
                self.game.udovl.znach = 100
            self.game.dog.money-= self.odezhda[self.number_odezhda].cost

    def button_nazad(self):
        if self.number_odezhda != 0:
            self.number_odezhda -=1

    def button_vpered(self):
        if self.number_odezhda != len(self.odezhda) - 1:
            self.number_odezhda +=1

    def draw(self):
        super().draw()
        for i in self.knopki:
            i.draw()
        self.odezhda[self.number_odezhda].draw()
        otrisovka_text = pgfr.Font(None, 15)
        if self.odezhda[self.number_odezhda].kupleno is True:
            otrisovka_text.render_to(self.game.okno,[410,130],'КУПЛЕНО' ,[0,0,0])
            
        else:
            otrisovka_text.render_to(self.game.okno,[405,130],'НЕ КУПЛЕНО' ,[100,100,100])

        if self.odezhda[self.number_odezhda].nadeto is True:
            otrisovka_text.render_to(self.game.okno,[410,410],'НАДЕТО' ,[0,0,0])
        else:
            otrisovka_text.render_to(self.game.okno,[405,410],'НЕ НАДЕТО' ,[100,100,100])

        otrisovka_text.render_to(self.game.okno, [self.odezhda[self.number_odezhda].rect.x + 80, self.odezhda[self.number_odezhda].rect.y+30], str(self.odezhda[self.number_odezhda].cost), [0, 0, 0])



    def update(self):
        for i in self.knopki:
            i.update()


class Eda(Menu):
    def __init__(self, image, x, y, game):
        super().__init__(image, x, y, game)
        kartinki = os.listdir(r'images/food')
        knopka_image = pg.image.load(r'images\button.png')
        self.knopka1 = cb.Knopki(knopka_image, 'НАЗАД', 150, 350, game, self.button_nazad )
        self.knopka2 = cb.Knopki(knopka_image, 'ВПЕРЕД', 600, 350, game, self.button_vpered )
        self.knopka3 = cb.Knopki(knopka_image, 'КУПИТЬ', 150, 150, game, self.button_kupit )
        self.knopki = [self.knopka1, self.knopka2, self.knopka3]
        self.eda =[]
        self.number_eda = 0
        for i in kartinki:
            a = class_eda.Eda(i, self.game)
            self.eda.append(a)


    def button_nazad(self):
        if self.number_eda != 0:
            self.number_eda -=1

    def button_vpered(self):
        if self.number_eda != len(self.eda) - 1:
            self.number_eda +=1

    def button_kupit(self):
        if self.eda[self.number_eda].cost < self.game.dog.money:
            if self.game.golod.znach<=90:
                self.game.golod.znach+=10
            else:
                self.game.golod.znach = 100
            self.game.dog.money-= self.eda[self.number_eda].cost
    def draw(self):
        super().draw()
        for i in self.knopki:
            i.draw()
        self.eda[self.number_eda].draw()

    def update(self):
        for i in self.knopki:
            i.update()


class Igra(Menu):
    def __init__(self, image, x, y, game):
        super().__init__(image, x, y, game)
        self.dog = cd.Dog_igra(game, [SHIRINA_DOG//4, VISOTA_DOG//4],self.game.dog.name, 0)
        self.game = game
        self.text = pgfr.Font(None, 20)
        self.spisok_toy = []
        self.kolvo_poi_toy = 0
        self.rect_dog_stolk = pg.Rect([self.dog.rect.x, self.dog.rect.y,],
                                      [self.dog.rect.width//2, self.dog.rect.height//2])

    def stolknovenie(self):
        self.rect_dog_stolk = pg.Rect([self.dog.rect.x + 45, self.dog.rect.y + self.dog.rect.width//2,],
                                      [self.dog.rect.width//2, self.dog.rect.height//2])
        for i in self.spisok_toy:
            if self.rect_dog_stolk.colliderect(i.rect) is True:
                self.spisok_toy.remove(i)
                self.kolvo_poi_toy += 1

    def spawn_toy(self):
        toy = ct.Toy(self.game)
        self.spisok_toy.append(toy)

    def local_event(self, event):
        super().local_event(event)
        if event.type == self.event_toy and isinstance(self, Igra):
            self.spawn_toy()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.game.dog.money += self.kolvo_poi_toy*5
                self.game.udovl.znach+=self.kolvo_poi_toy 

    def draw(self):
        super().draw()
        self.dog.draw()
        for i in self.spisok_toy:
            i.draw()
        self.text.render_to(self.game.okno, [100, 100], str(self.kolvo_poi_toy))

    def update(self):
        super().update()
        self.dog.update()
        for i in self.spisok_toy:
            i.update()
        self.stolknovenie()
