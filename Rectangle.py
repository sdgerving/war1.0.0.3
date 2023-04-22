import pygame
import Drawgame
import SpriteSheets
import Sprites
import Variables
import Units
import Font
import Mouse
import random


class my_rectangle:

    def __init__(self, color, x, y, width, height, myFont, thick, loc, text, name, show):
        self.show = show
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (x, y, width, height)
        self.text = text
        self.myFont = myFont
        self.thick = thick
        self.loc = loc



    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.thick)

        if self.text != '':
            font = self.myFont
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


def createButton():
    Variables.buttons.append(my_rectangle(Font.green, 1360, 10, 125, 65, Font.arial25, 0, 0, 'Add Unit!', 'add', True))
    Variables.buttons.append(my_rectangle(Font.green, 1485, 10, 125, 65, Font.arial25, 0, 0, 'Check Units', 'chkunit', False))
    Variables.buttons.append(my_rectangle(Font.green, 1360, 75, 125, 65, Font.arial25, 0, 0, 'Huge Unit!', 'addbig', True))
    Variables.buttons.append(my_rectangle(Font.green, 1360, 1130, 125, 35, Font.arial21, 0, 0, 'Next Unit', 'next', False))
    Variables.buttons.append(my_rectangle(Font.green, 1550, 1130, 125, 35, Font.arial21, 0, 0, 'Previous Unit', 'prev', False))
    Variables.buttons.append(my_rectangle(Font.green, 1385, 25, 125, 65, Font.arial21, 0, 0, 'Main', 'main', False))
    Variables.buttons.append(my_rectangle(Font.green, 1385, 830, 125, 65, Font.arial21, 0, 0, 'Send Hero', 'sendhero', False))


def drawButton():
    Sprites.my_sprites.draw(Sprites.my_sprites(Variables.background[0], 100, 50, 0, 0), Drawgame.screen)
    for count in range(len(Variables.buttons)):

        if Variables.buttons[count].show:
            Variables.buttons[count].draw(Drawgame.screen, (0, 0, 0))

        checkLoc(count)


def checkLoc(count):
    if Variables.buttons[count].isOver((Variables.my_mouse.mouseX, Variables.my_mouse.mouseY)):
        Variables.buttons[count].color = Font.blue
        if Variables.buttons[count].name == 'add' and Variables.my_mouse.click_Value == 1 and Variables.buttons[count].show == True:
            Variables.buttons[count].color = Font.yellow
            Units.createUnits()
            Variables.buttons[1].show = True
            Variables.my_mouse.click_Value = 0


        elif Variables.buttons[count].name == "chkunit" and Variables.my_mouse.click_Value == 1 and Variables.buttons[count].show == True:
            Variables.buttons[count].color = Font.yellow
            Variables.buttons[0].show = False
            Variables.buttons[1].show = False
            Variables.buttons[2].show = False
            Variables.buttons[3].show = True
            Variables.buttons[4].show = True
            Variables.buttons[5].show = True
            Variables.buttons[6].show = True

            Variables.my_mouse.click_Value = 0


        elif Variables.buttons[count].name == "addbig" and Variables.my_mouse.click_Value == 1 and Variables.buttons[count].show == True:
            Variables.buttons[count].color = Font.yellow
            Units.createUnits2()
            Variables.buttons[1].show = True
            Variables.my_mouse.click_Value = 0
        elif Variables.people and Variables.buttons[count].show == True:
            if Variables.buttons[count].name == "next" and Variables.my_mouse.click_Value == 1:
                Variables.my_mouse.click_Value = 0
                Variables.index = (Variables.index + 1) % len(Variables.people)
            if Variables.buttons[count].name == "prev" and Variables.my_mouse.click_Value == 1:
                Variables.my_mouse.click_Value = 0
                Variables.index = (Variables.index - 1) % len(Variables.people)
            if Variables.buttons[count].name == "main" and Variables.my_mouse.click_Value == 1:
                Variables.buttons[count].color = Font.yellow
                Variables.buttons[0].show = True
                Variables.buttons[1].show = True
                Variables.buttons[2].show = True
                Variables.buttons[3].show = False
                Variables.buttons[4].show = False
                Variables.buttons[5].show = False
                Variables.buttons[6].show = False
                Variables.my_mouse.click_Value = 0
            if Variables.buttons[count].name == "sendhero" and Variables.my_mouse.click_Value == 1 and Variables.buttons[count].show == True:
                Variables.people[Variables.index].destx= Variables.my_mouse.selectedx
                Variables.people[Variables.index].desty = Variables.my_mouse.selectedy
                Variables.my_mouse.click_Value = 0
    else:
        Variables.buttons[count].color = Font.green


def createRectangle(length, width):
    recPosX = 0
    recPosY = 0
    tempcount = 1
    for i in (n + 1 for n in range(length)):
        for j in (n + 1 for n in range(width)):
            Variables.recboard.append(my_rectangle(Font.gameboardgreen, recPosX + 100, recPosY + 50, 25, 25, Font.arial15, 1, tempcount, '','', True))
            type, image,cooldown,green,regular,elite,difficulty,encounter = SpriteSheets.getMapLocationData(0)
            Variables.locations.append(Sprites.mapLocations(Variables.mapimage[image],  recPosX + 100, recPosY + 50, 25, 25, tempcount, type,cooldown, image,cooldown,green,regular,elite,difficulty,recPosX+100 , recPosY+50,encounter))

            recPosX += 25
            tempcount += 1
        recPosY += 25
        recPosX = 0
        tempcount += 1

def drawRecBoard():
    for count in range(len(Variables.recboard)):
        Variables.recboard[count].draw(Drawgame.screen, 0)




def drawlocations():
    for count in range(len(Variables.locations)):
        Sprites.mapLocations.draw(Variables.locations[count], Drawgame.screen)
        locationtimer(count)


def colorRect():
    for count in range(len(Variables.recboard)):

        if Variables.recboard[count].isOver((Variables.my_mouse.mouseX, Variables.my_mouse.mouseY)):
            Variables.recboard[count].color = Font.hoverrectgreen

            Variables.my_mouse.currentLoc = count
        else:
            Variables.recboard[count].color = Font.gameboardgreen
            Variables.recboard[Variables.my_mouse.selectedLoc].thick = 1
    Variables.recboard[Variables.my_mouse.selectedLoc].color = Font.green
    Variables.my_mouse.selectedx = Variables.recboard[Variables.my_mouse.selectedLoc].x+13
    Variables.my_mouse.selectedy = Variables.recboard[Variables.my_mouse.selectedLoc].y + 12


def locationtimer(count):
    tempx = Units.random_num(1, 100)
    if Variables.locations[count].count>0:
        Sprites.mapLocations.checkTime(Variables.locations[count])
    if Variables.locations[count].count == 0 and Variables.locations[count].type == 'Scourge':

        if tempx >= 98:
            Variables.locations[count].elite += 1
        elif tempx >=93 and tempx <= 97:
            Variables.locations[count].regular += 1
        else:
            Variables.locations[count].green += 1
        Variables.locations[count].count = random.randrange(10, 30)
        Variables.locations[count].cooldown = Variables.locations[count].count

    if Variables.locations[count].count == 0 and Variables.locations[count].type == 'tomb':
        if tempx >= 95:
            Variables.locations[count].elite += 1
        elif 85 <= tempx <= 95:
            Variables.locations[count].regular += 1
        else:
            Variables.locations[count].green += 1
        Variables.locations[count].count = random.randrange(10, 30)
        Variables.locations[count].cooldown = Variables.locations[count].count
    if Variables.locations[count].count == 0 and Variables.locations[count].type == 'cave2':
        if tempx >= 90:
            Variables.locations[count].elite += 1
        elif 75 <= tempx <= 89:
            Variables.locations[count].regular += 1
        else:
            Variables.locations[count].green += 1
        Variables.locations[count].count = random.randrange(6, 18)
        Variables.locations[count].cooldown = Variables.locations[count].count

def createforest(currenttile,totalforest):

    if totalforest != 0:
        if currenttile >= 2200:
            tempnum = random.randrange(1, 100)
            if tempnum >= 65:
                Variables.locations[currenttile - 50].image = Variables.mapimage[0]
                Variables.locations[currenttile - 50].type = 'Forest'
                totalforest -= 1
                if random.randrange(1,100)>=75:
                    Variables.locations[currenttile - 100].image = Variables.mapimage[0]
                    Variables.locations[currenttile - 100].type = 'Forest'
                    if random.randrange(1, 100) >= 85:
                        Variables.locations[currenttile - 150].image = Variables.mapimage[0]
                        Variables.locations[currenttile - 150].type = 'Forest'


        elif currenttile <= 49:
            tempnum = random.randrange(1, 100)
            if tempnum >= 65:
                Variables.locations[currenttile + 50].image = Variables.mapimage[0]
                Variables.locations[currenttile + 50].type = 'Forest'
                totalforest -= 1
                if random.randrange(1, 100) >= 75:
                    Variables.locations[currenttile + 100].image = Variables.mapimage[0]
                    Variables.locations[currenttile + 100].type = 'Forest'
                    if random.randrange(1, 100) >= 85:
                        Variables.locations[currenttile + 150].image = Variables.mapimage[0]
                        Variables.locations[currenttile + 150].type = 'Forest'

        else:
            tempnum = random.randrange(1, 100)
            if tempnum >= 65:
                Variables.locations[currenttile - 50].image = Variables.mapimage[0]
                Variables.locations[currenttile - 50].type = 'Forest'
                totalforest -= 1
                if random.randrange(1, 100) >= 75:
                    Variables.locations[currenttile - 100].image = Variables.mapimage[0]
                    Variables.locations[currenttile - 100].type = 'Forest'
                    if random.randrange(1, 100) >= 85:
                        Variables.locations[currenttile - 150].image = Variables.mapimage[0]
                        Variables.locations[currenttile - 150].type = 'Forest'
                    if random.randrange(1,100)>=95:
                        Variables.locations[currenttile - 50].image = pygame.transform.scale(Variables.mapimage[4], (25, 25))
                        Variables.locations[currenttile - 50].type = 'cave'
                        Variables.locations[currenttile - 100].image = pygame.transform.scale(Variables.mapimage[0],(25, 25))
                        Variables.locations[currenttile - 100].type = 'Forest'
                        Variables.locations[currenttile - 49].image = pygame.transform.scale(Variables.mapimage[0],(25, 25))
                        Variables.locations[currenttile - 49].type = 'Forest'
                        Variables.locations[currenttile - 51].image = pygame.transform.scale(Variables.mapimage[0],(25, 25))
                        Variables.locations[currenttile - 51].type = 'Forest'
                        totalforest -= 3
            tempnum = random.randrange(1, 100)
            if tempnum >= 65:
                Variables.locations[currenttile + 50].image = Variables.mapimage[0]
                Variables.locations[currenttile + 50].type = 'Forest'
                totalforest -= 1
                if random.randrange(1, 100) >= 75 and currenttile<=2100:
                    Variables.locations[currenttile + 100].image = Variables.mapimage[0]
                    Variables.locations[currenttile + 100].type = 'Forest'
                    if random.randrange(1, 100) >= 85and currenttile<=2050:
                        Variables.locations[currenttile + 150].image = Variables.mapimage[0]
                        Variables.locations[currenttile + 150].type = 'Forest'
                    if random.randrange(1,100)>=95:
                        Variables.locations[currenttile + 50].image = pygame.transform.scale(Variables.mapimage[4], (25, 25))
                        Variables.locations[currenttile + 50].type = 'cave'
                        Variables.locations[currenttile + 100].image = pygame.transform.scale(Variables.mapimage[0],(25, 25))
                        Variables.locations[currenttile + 100].type = 'Forest'
                        Variables.locations[currenttile + 49].image = pygame.transform.scale(Variables.mapimage[0],(25, 25))
                        Variables.locations[currenttile + 49].type = 'Forest'
                        Variables.locations[currenttile + 51].image = pygame.transform.scale(Variables.mapimage[0],(25, 25))
                        Variables.locations[currenttile + 51].type = 'Forest'
                        totalforest -= 3
        if random.randrange(1, 10) <= 5:
            currenttile += 1
            Variables.locations[currenttile ].image = Variables.mapimage[0]
            Variables.locations[currenttile ].type = 'Forest'
            if totalforest >= 0:
                totalforest -= 1
                createforest(currenttile, totalforest)
        else:
            currenttile -= 1
            Variables.locations[currenttile ].image = Variables.mapimage[0]
            Variables.locations[currenttile ].type = 'Forest'
            totalforest-=1
            if totalforest >= 0:
                totalforest -= 1
                createforest(currenttile, totalforest)


def createmountains():
    tempcount = 0


    scourgeloc = random.randrange(1, 2249)
    SpriteSheets.spriteList(scourgeloc, "Scourge",0,)
    print("scourgeloc:" + str(scourgeloc))
    for count in range(len(Variables.locations)):
        if Variables.locations[count].type == "Forest" and Variables.locations[count].type != "Scourge" and Variables.locations[count].type != "Cave2":

            if Variables.locations[count + 1].type == 'grassland' and Variables.locations[count + 2].type == 'grassland'  and Variables.locations[count + 3].type == 'Forest' and count<=2249 :
                SpriteSheets.spriteList(count, "Mountain", +1)
                SpriteSheets.spriteList(count, "Mountain", +2)
            if Variables.locations[count+1].type == 'grassland' and Variables.locations[count+2].type == 'grassland' and Variables.locations[count+3].type=='grassland'and Variables.locations[count+4].type=='Forest'and count<=2244:
                SpriteSheets.spriteList(count,"Mountain",+1)
                SpriteSheets.spriteList(count, "Mountain", +2)
                SpriteSheets.spriteList(count, "Mountain", +3)
def createmountains2():
    tempcount=0
    for count in range(len(Variables.locations)):

        if Variables.locations[count].type =="Forest":
            print(count)
            if count>1:
                temp=Units.random_num(1,100)

                if Variables.locations[count - 1].type =='grassland' and temp>=80:
                    print(temp)
                    tempcount += 1
                    Variables.locations[count - 1].image = pygame.transform.scale(Variables.mapimage[6], (25, 25))
                    Variables.locations[count - 1].type = 'Mountain'
            if count < 2248:
                temp = Units.random_num(1, 100)

                if Variables.locations[count + 1].type =='grassland' and temp>=75:
                    print(temp)
                    tempcount+=1
                    Variables.locations[count + 1].image = pygame.transform.scale(Variables.mapimage[6], (25, 25))
                    Variables.locations[count +1 ].type = 'Mountain'
            if count >51:
                temp = Units.random_num(1, 100)

                if Variables.locations[count - 50].type =='grassland' and temp>=85:
                    print(temp)
                    tempcount += 1
                    Variables.locations[count - 50].image = pygame.transform.scale(Variables.mapimage[6], (25, 25))
                    Variables.locations[count - 50].type = 'Mountain'
            if count <2200:
                temp = Units.random_num(1, 100)

                if Variables.locations[count + 50].type =='grassland' and temp>=75:
                    print(temp)
                    tempcount += 1
                    Variables.locations[count + 50].image = pygame.transform.scale(Variables.mapimage[6], (25, 25))
                    Variables.locations[count + 50].type = 'Mountain'

        if Variables.locations[count].type == "cave":
               None
    print("tempcount:" + str(tempcount))
    scourge = random.randrange(1, 2249)
    Variables.locations[scourge].image = pygame.transform.scale(Variables.mapimage[12], (25, 25))
    Variables.locations[scourge].type = 'Scourge'

