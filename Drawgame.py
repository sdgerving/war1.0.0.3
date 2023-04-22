import pygame
import Font
import Variables
import Sprites

fps = 60
FPS_CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode([1700, 1200])
start_ticks=pygame.time.get_ticks()

def drawGameBoard():

    screen.fill((0, 0, 20))
    FPS_CLOCK.tick(fps)

    mouse_X = Font.arial21.render("X:" + str(Variables.my_mouse.mouseX), True, Font.red)
    mouse_Y = Font.arial21.render("Y:" + str(Variables.my_mouse.mouseY), True, Font.red)
    clock = Font.arial21.render(str(FPS_CLOCK), True, Font.red)

    screen.blit(clock, (102, 20))
    screen.blit(mouse_X, (5, 1150))
    screen.blit(mouse_Y, (5, 1170))

    screen.blit(Font.arial25.render('Hovered Location Number:' + str(Variables.my_mouse.currentLoc), True, Font.red),(1360, 145))
    screen.blit(Font.arial30.render('Selected Location:' + str(Variables.my_mouse.selectedLoc), True,Font.red), (1390, 180))
    #screen.blit(Font.arial21.render('Location number:' + str(Variables.my_mouse.selectedLoc), True, Font.red),(1400, 460))
    screen.blit(Font.arial25.render('Total Units:' + str(len(Variables.people)), True, Font.blue), (1400, 700))
    screen.blit(Font.arial25.render('Location type:' + str(Variables.locations[Variables.my_mouse.selectedLoc].type), True, Font.white), (1410, 200))
    screen.blit(Font.arial42.render('Seconds:' + str(Variables.seconds), True,Font.white), (1400, 530))
    screen.blit(Font.arial25.render(" cooldown: "+str(Variables.locations[Variables.my_mouse.selectedLoc].count), True, Font.white), (1410, 220))
    screen.blit( Font.arial25.render(" Encounter Rate: " + str(Variables.locations[Variables.my_mouse.selectedLoc].encounter),True, Font.white), (1410, 350))

    if Variables.locations[Variables.my_mouse.selectedLoc].type =='Scourge' or Variables.locations[Variables.my_mouse.selectedLoc].type =='tomb' or Variables.locations[Variables.my_mouse.selectedLoc].type =='cave2':
        screen.blit(Font.arial25.render(" Green: " + str(Variables.locations[Variables.my_mouse.selectedLoc].green), True,Font.white), (1410, 240))
        screen.blit(Font.arial25.render(" Regular: " + str(Variables.locations[Variables.my_mouse.selectedLoc].regular), True, Font.white), (1410, 260))
        screen.blit(Font.arial25.render(" Elite: " + str(Variables.locations[Variables.my_mouse.selectedLoc].elite), True,Font.white), (1410, 280))
        screen.blit(Font.arial25.render(" Difficulty: " + str(Variables.locations[Variables.my_mouse.selectedLoc].difficulty), True,Font.white), (1410, 300))
        screen.blit(Font.arial25.render(" Encounter Rate: " + str(Variables.locations[Variables.my_mouse.selectedLoc].encounter),True, Font.white), (1410, 320))
    if Variables.people:
        screen.blit(Font.arial25.render('unit 1 location: ' + str(Variables.people[0].loc), True, Font.blue),(1400, 500))

