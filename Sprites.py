import pygame
import Drawgame
import Variables
import math

class my_sprites(pygame.sprite.Sprite):
    def __init__(self, Image,dx, dy,Loca,Type):
        pygame.sprite.Sprite.__init__(self)
        self.image=Image
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
        self.loc = Loca
        self.type=Type

    def draw(self, screen):
        Drawgame.screen.blit(self.image, self.rect)


class alive_units(my_sprites):
    def __init__(self, Image, dx, dy, w, h, Loca, Type, destX, destY, Speed,Cooldown,Imgvar,Count,Heroinit,Herototalinit,Combatskill,Attacker):
        super().__init__(Image, dx, dy, w, h)


        self.imgvar = Imgvar
        self.image = pygame.transform.scale(self.image, (w, h))
        self.destx = destX
        self.desty = destY
        self.speed = Speed
        self.loc=Loca
        self.type=Type
        self.cooldown = Cooldown
        self.last = Count
        self.move=True
        self.count = Count
        self.onesec=0
        self.heroinit=Heroinit
        self.herototalinitiat = Herototalinit
        self.combatskill= Combatskill
        self.attacker = False








    def checkTime(self):

        now = Variables.seconds
        if now - self.onesec >=1:
            self.count-=1
        self.onesec=now
        if now - self.last > self.cooldown:
            self.last = now
            self.move=True




class mapLocations(my_sprites):
    def __init__(self, Image, dx, dy, w, h, Loca, Type, Cooldown,Imgvar,Count,Green,Regular,Elite,Difficulty,Centx,Centy,Encounter):
        super().__init__(Image, dx, dy, w, h)
        self.imgvar = Imgvar
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.loc=Loca
        self.type=Type
        self.cooldown = Cooldown
        self.last = pygame.time.get_ticks()
        self.onesec = 0
        self.last = Count
        self.count = Count
        self.green = Green
        self.regular = Regular
        self.elite = Elite
        self.difficulty = Difficulty
        self.centx=Centx
        self.centy = Centy
        self.encounter= Encounter

    def checkTime(self):

        now = Variables.seconds
        if now - self.onesec >=1:
            self.count-=1
        self.onesec=now
        if now - self.last > self.cooldown:
            self.last = now
            self.move=True

class locationUnits(my_sprites):
    def __init__(self, Image, dx, dy, w, h,Init, Totalinit):
        super().__init__(Image, dx, dy, w, h)
        self.init= Init
        self.totalinit= Totalinit