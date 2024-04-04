import pygame as pg
import class_button as cb
import class_dog as cd
import class_money as cm
import class_menu as cme
from settings import*
import class_toy as ct
import base
import random
import class_sostoyiani as cs
# Инициализация pg
pg.init()



class Game:
    def __init__(self):
        self.fon = pg.image.load(r'images\background.png')
        self.fon = pg.transform.scale(self.fon, [SCREEN_WIDTH , SCREEN_HEIGHT ])
        # Создание окна
        self.okno = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        knopka_image = pg.image.load(r'images\button.png')
        self.knopka1 = cb.Knopki(knopka_image, 'ЕДА', 750, 10, self, self.button_eat)
        self.knopka2 = cb.Knopki(knopka_image, 'ОДЕЖДА', 750, 55, self, self.button_clothes)
        self.knopka3 = cb.Knopki(knopka_image, 'ИГРЫ', 750, 100, self, self.button_game)
        self.knopka4 = cb.Knopki(knopka_image, 'УЛУЧШЕНИЕ', 750, 145, self, self.button_uluchenie)
        self.koeff_monet = 1
        self.money = cm.Money(self)
        self.golod = cs.Sostyanie(self, 'images/satiety.png', [50,100])
        self.health = cs.Sostyanie(self, 'images/health.png', [50,150])
        self.udovl = cs.Sostyanie(self, 'images/happiness.png', [50, 200])
        self.knopki = [self.knopka1, self.knopka2, self.knopka3, self.knopka4]
        self.slovar_ulushenie = {}
        for i in range(10, 100, 20):
            self.slovar_ulushenie[i] = False
        pg.display.set_caption("Виртуальный питомец")
        self.base = base.Base('igra_dog', ['Name', 'money','health', 'clothes'])
        try:
            self.base.sozdanie({'Name':NAME, 'money':'0', 'health' : random.randint(1, 10), 'clothes':[]})
        except ValueError:
            pass
        self.test_sch = self.base.schitivanie(NAME)

        self.dog = cd.Dog(self, [SHIRINA_DOG//4, VISOTA_DOG//4], NAME, int(self.test_sch['money']))
        

        self.menu = None
        self.fon_menu = pg.image.load(r'images\menu\menu_page.png')
        self.fon_menu_game = pg.image.load(r'images\game_background.png')
        self.eda = cme.Eda(self.fon_menu, 0, 0, self)
        self.clothes = cme.Clothes(self.fon_menu, 0, 0, self)
        self.event_toy = pg.USEREVENT
        self.event_health =  pg.USEREVENT+1
        self.event_golod =  pg.USEREVENT+2
        self.event_udovl =  pg.USEREVENT+3
        pg.time.set_timer(self.event_toy, 1000)
        pg.time.set_timer(self.event_health, random.randint(300, 500))
        pg.time.set_timer(self.event_golod, random.randint(300, 500))
        pg.time.set_timer(self.event_udovl, random.randint(300, 500))

        self.run()

    def run(self):
        while True:
            if self.menu == None:
                self.event()
            else:
                self.menu.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.base.obnovlenie({'Name':self.dog.name, 'money':str(self.dog.money), 'health' : str(random.randint(1, 10)), 'clothes':self.clothes.objects_to_dict()})
                self.base.save()
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.dog.rect.collidepoint(event.pos):
                    self.dog.money += self.koeff_monet
                for i in self.knopki:
                    if i.rect.collidepoint(event.pos):
                        i.function()
            if event.type == self.event_health:
                self.health.znach-=random.randint(10,20)
                pg.time.set_timer(self.event_health, random.randint(20000, 50000))
            if event.type == self.event_golod:
                self.golod.znach-=random.randint(1,3)
                pg.time.set_timer(self.event_golod, random.randint(20000, 50000))
            if event.type == self.event_udovl:
                self.udovl.znach-=random.randint(10,20)
                pg.time.set_timer(self.event_udovl,  random.randint(20000, 50000))
                

    def update(self):
        for i in self.knopki:
            i.update()
        if self.menu != None:
            self.menu.update()

    def draw(self):
        self.okno.blit(self.fon, [0, 0])
        self.dog.draw()
        self.money.draw()
        self.golod.draw()
        self.udovl.draw()
        self.health.draw()
        for i in self.clothes.odezhda:
            if i.nadeto is True:
                i.draw() 
        for i in self.knopki:
            i.draw()
        if self.menu != None:
            self.menu.draw()
        pg.display.flip()

    def button_eat(self):
        self.menu = self.eda

    def button_clothes(self):
        self.menu = self.clothes

    def button_game(self):
        self.menu = cme.Igra(self.fon_menu_game, 0, 0, self) 

    def button_uluchenie(self):
        for i in self.slovar_ulushenie:
            if self.slovar_ulushenie[i] is False and self.dog.money >= i:
                self.dog.money -= i
                self.koeff_monet += 1
                self.slovar_ulushenie[i] = True





if __name__ == "__main__":
    Game()