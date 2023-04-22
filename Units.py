import random

import Rectangle
import Sprites
import pygame
import Variables
import Font
import Drawgame
import Sprites
import math
import Combat



def createUnits():
    temptype, tempunit, tempcooldown = get_image()

    Variables.people.append(Sprites.alive_units(Variables.unitimage[tempunit], 100, 50, 25, 25, 0, temptype,
                                                random.randrange(113, 1338, 25), random.randrange(63, 1163, 25),
                                                random.randrange(1, 5), tempcooldown, tempunit, tempcooldown,0,0,10,False))
    Variables.unitrectangles.append( Rectangle.my_rectangle(Font.red,  113, 63 , 3, 3, Font.arial15, 10, 0, '', '',True))

def createUnits2():
    for x in range(1,100):
        temptype, tempunit,tempcooldown = get_image()
        Variables.people.append(Sprites.alive_units(Variables.unitimage[tempunit], 100, 50, 25, 25, 0, temptype,random.randrange(113, 1338,25),
                                                    random.randrange(63, 1163, 25),random.randrange(1, 5),tempcooldown,tempunit,tempcooldown,0,0,0,False))
        Variables.unitrectangles.append(
            Rectangle.my_rectangle(Font.red, 110, 63, 5, 5, Font.arial15, 10, 0, '', '', True))
def drawUnits():
    for count in range(len(Variables.people)):

        Sprites.my_sprites.draw(Variables.people[count], Drawgame.screen)
        Variables.unitrectangles[count].draw(Drawgame.screen, 0)
        moveUnits(count)






def moveUnits(count):

    tempa = getlocation(Variables.unitrectangles[count].x, Variables.unitrectangles[count].y)
    Variables.people[count].loc= tempa
    Variables.unitrectangles[count].loc =getlocation(Variables.unitrectangles[count].x,Variables.unitrectangles[count].y)
    Variables.people[count].ct = Variables.locations[tempa].type
    destloc = getlocation(Variables.people[count].destx, Variables.people[count].desty)


    if Variables.locations[tempa].type =="cave2":

        if Variables.unitrectangles[count].x-13 < Variables.locations[tempa].centx:
            Variables.people[count].rect.x += Variables.people[count].speed
            Variables.unitrectangles[count].x += Variables.people[count].speed

        if Variables.unitrectangles[count].x+13 > Variables.locations[tempa].centx:
            Variables.people[count].rect.x -= Variables.people[count].speed
            Variables.unitrectangles[count].x -= Variables.people[count].speed

        if Variables.unitrectangles[count].y-13 < Variables.locations[tempa].centy:
            Variables.people[count].rect.y += Variables.people[count].speed
            Variables.unitrectangles[count].y += Variables.people[count].speed

        if Variables.unitrectangles[count].y+13 > Variables.locations[tempa].centy:
            Variables.people[count].rect.y -= Variables.people[count].speed
            Variables.unitrectangles[count].y -= Variables.people[count].speed
        else:
            Variables.people[count].move = False

        checkdest(count,tempa)


    if Variables.unitrectangles[count].x< Variables.people[count].destx and Variables.people[count].move==True:
        Variables.people[count].rect.x += Variables.people[count].speed
        Variables.unitrectangles[count].x +=  Variables.people[count].speed

    if Variables.unitrectangles[count].x > Variables.people[count].destx  and Variables.people[count].move==True:
        Variables.people[count].rect.x -= Variables.people[count].speed
        Variables.unitrectangles[count].x -= Variables.people[count].speed

    if Variables.unitrectangles[count].y< Variables.people[count].desty  and Variables.people[count].move==True:
        Variables.people[count].rect.y += Variables.people[count].speed
        Variables.unitrectangles[count].y += Variables.people[count].speed

    if Variables.unitrectangles[count].y > Variables.people[count].desty  and Variables.people[count].move==True:
        Variables.people[count].rect.y -= Variables.people[count].speed
        Variables.unitrectangles[count].y -= Variables.people[count].speed

    if destloc == tempa:

        checkdest(count,tempa)

def checkdest(count,x):

    if Variables.locations[x].type == "Cave2" and  Variables.people[count].count == 0:
        Variables.locations[x].image = pygame.transform.scale(Variables.mapimage[4], (25, 25))
        Variables.locations[x].type = "Cave"
        Variables.people[count].count = random.randrange(3, 10)
        Variables.people[count].cooldown = Variables.people[count].count
        Variables.people[count].move = True
    #if Variables.people[count].count == 0 :
        #Variables.people[count].count = random.randrange(3, 10)
        #Variables.people[count].cooldown = Variables.people[count].count
        #Variables.people[count].destx = random.randrange(113, 1338, 25)
        #Variables.people[count].desty = random.randrange(63, 1163, 25)
        #Variables.people[count].move = True
    if Variables.locations[x].type=="Scourge" and Variables.people[count].count == 0:
        Variables.people[count].move = False
        Combat.initiative(count,x )
    Sprites.alive_units.checkTime(Variables.people[count])








def myround(x, base):
    return base * round(x/base)



def getlocation(x,y):
    tempx = math.floor((x-100)/25)
    tempy = math.floor((y-50)/25)*50

    tempz =tempx +tempy

    return tempz
def get_image():
    global a, b,c
    tempx = random.randint(1, 4)
    if tempx == 1:
        a = "Warrior"
        b = 1
        c = 10
    elif tempx == 2:
        a = "Priest"
        b = 3
        c = 10

    elif tempx == 3:
        a = "Mage"
        b = 0
        c = 10
    elif tempx == 4:
        a = "Ranger"
        b = 2
        c = 10
    return a, b, c

def unitInfo():
    if Variables.people and Variables.buttons[1].show==False:
        Sprites.my_sprites.draw(Sprites.mapLocations(Variables.unitpointer[0],Variables.people[Variables.index].rect.x,Variables.people[Variables.index].rect.y-25, 30, 30,0,0,0,0,0,0,0,0,0,0,0,0), Drawgame.screen)
        #pygame.draw.rect(Drawgame.screen,Font.red,pygame.Rect(Variables.people[Variables.index].rect.x,Variables.people[Variables.index].rect.y,25,25),2)
        #pygame.draw.circle(Drawgame.screen, Font.red,[Variables.people[Variables.index].rect.x+7,Variables.people[Variables.index].rect.y-5], 7, 0)
        #pygame.draw.line(Drawgame.screen, Font.red,[Variables.people[Variables.index].rect.x, Variables.people[Variables.index].rect.y], [100,50], 1)
         #pygame.draw.polygon(Drawgame.screen, Font.red,[[Variables.people[Variables.index].rect.x, Variables.people[Variables.index].rect.y],[Variables.people[Variables.index].rect.x+13, Variables.people[Variables.index].rect.y],[Variables.people[Variables.index].rect.x+5, Variables.people[Variables.index].rect.y-17]], 0)
        if Variables.buttons[1].show==False:
            Drawgame.screen.blit(Font.arial42.render('Going To Loc #:' + str(getlocation((Variables.people[Variables.index].destx),(Variables.people[Variables.index].desty))), True, Font.blue), (1360, 901))
            Drawgame.screen.blit(Font.arial21.render('Going To Coord: X:' + str(Variables.unitrectangles[Variables.index].x)+ "Y: "+str(Variables.unitrectangles[Variables.index].y), True, Font.blue),(1360, 941))
            Drawgame.screen.blit(Font.arial21.render('Currently At: X:' + str(Variables.unitrectangles[Variables.index].x)+ "Y: "+str(Variables.unitrectangles[Variables.index].y), True, Font.blue),(1360, 961))
            Drawgame.screen.blit(Font.arial21.render('unit 1 location: ' + str(Variables.people[Variables.index].loc), True, Font.blue), (1360, 1000))
            Drawgame.screen.blit(Font.arial21.render('unit Number: ' + str(Variables.index), True, Font.blue),(1360, 1025))
            Drawgame.screen.blit(Font.arial21.render('Class: ' + str(Variables.people[Variables.index].type), True, Font.blue),(1360, 1050))
            Drawgame.screen.blit(Font.arial28.render('Cooldown: ' + str(Variables.people[Variables.index].count), True, Font.blue),(1360, 1075))
            Drawgame.screen.blit(Font.arial21.render('Is over:' + str(Variables.people[Variables.index].ct),True,Font.blue), (1360,1095))
            Sprites.my_sprites.draw(Sprites.alive_units(pygame.transform.scale(Variables.unitimage[Variables.people[Variables.index].imgvar],(50,50)), 1550, 1000, 90, 90,0,0,0,0,0,0,0,0,0,0,0,False), Drawgame.screen)
            Sprites.my_sprites.draw(Sprites.locationUnits(pygame.transform.scale(Variables.unitimage[3],(50,50)), 1550, 1100, 90, 90,0,0,), Drawgame.screen)

def random_num(min, max):
    x = random.randrange(min, max)

    return x