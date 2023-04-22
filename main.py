
import pygame
import Rectangle
import Mouse
import SpriteSheets
import Units
import Variables
import Drawgame
import math
import time
import random
pygame.init()
running = True
SpriteSheets.create_sprite('images/map.png')
Mouse.mouse.createMouse(Variables.my_mouse)
Rectangle.createButton()
Rectangle.createRectangle(45,50)

for x in range(1,25):
    Rectangle.createforest(random.randrange(1, 2249), random.randrange(1, 50))
Rectangle.createmountains()


index =0



while running:

    Variables.seconds = math.trunc((pygame.time.get_ticks() - Drawgame.start_ticks) / 1000 ) # calculate how many seconds

     # print how many second
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
           # for keys in Variables.listCount:

                #Variables.totalCount[keys]=Variables.totalCount.get(keys,0)+1
                #Variables.totalCount = sorted(Variables.totalCount.items(), key=lambda x: x[1], reverse=True)
           # print(Variables.totalCount)

            running = False
        if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                   time.sleep(15)
                    #index = (index+1)% len(Variables.map_pieces)
        if event.type == pygame.MOUSEBUTTONDOWN:
            Variables.my_mouse.click_Value = 1

        if event.type == pygame.MOUSEBUTTONUP:
            Variables.my_mouse.click_Value = 0
        if event.type == pygame.MOUSEBUTTONDOWN and Variables.my_mouse.mouseX <=1350 and Variables.my_mouse.mouseX>=100 and Variables.my_mouse.mouseY <=1175 and Variables.my_mouse.mouseY>=50:
            Variables.my_mouse.selectedLoc = Variables.my_mouse.currentLoc



    Drawgame.drawGameBoard()
    Mouse.mouse.get_mouse_pos(Variables.my_mouse)


    Rectangle.drawButton()
    Rectangle.drawlocations()
    Rectangle.drawRecBoard()
    Rectangle.colorRect()


    Units.drawUnits()
    Units.unitInfo()
    pygame.display.flip()



pygame.quit()
