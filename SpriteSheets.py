import pygame
import json
import Variables
import random

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()

        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite = pygame.transform.scale(sprite, (w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image


def create_sprite(image):
    my_spritesheet = Spritesheet(image)
    Variables.background = [my_spritesheet.parse_sprite('Basemap.png')]

    Variables.unitimage = [my_spritesheet.parse_sprite('mage.png'), my_spritesheet.parse_sprite('warrior.png'),
                           my_spritesheet.parse_sprite('ranger.png'), my_spritesheet.parse_sprite('priest.png')]
    Variables.unitpointer=[my_spritesheet.parse_sprite('redstar.png'),my_spritesheet.parse_sprite('star.png')]

    Variables.mapimage = [my_spritesheet.parse_sprite('forest.png'), my_spritesheet.parse_sprite('water.png'),
                        my_spritesheet.parse_sprite('farm.png'), my_spritesheet.parse_sprite('fire.png'),
                           my_spritesheet.parse_sprite('cave.png'), my_spritesheet.parse_sprite('tomb.png'),
                           my_spritesheet.parse_sprite('mountain.png'), my_spritesheet.parse_sprite('boulder.png'),
                           my_spritesheet.parse_sprite('cave2.png'), my_spritesheet.parse_sprite('stone.png'),
                           my_spritesheet.parse_sprite('rock.png'),my_spritesheet.parse_sprite('grassland.png'),
                           my_spritesheet.parse_sprite('scourge.png')]

def spriteList(currenttile,type,mod):
    if type == "Forest":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[0], (25, 25))
        Variables.locations[currenttile + mod].type = 'Forest'
        Variables.locations[currenttile + mod].cooldown = 0
        Variables.locations[currenttile + mod].green = 0
        Variables.locations[currenttile + mod].regular = 0
        Variables.locations[currenttile + mod].elite = 0
        Variables.locations[currenttile + mod].difficulty = 0
        Variables.locations[currenttile + mod].encounter = 15
    if type == "Water":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[1], (25, 25))
        Variables.locations[currenttile + mod].type = 'Water'
        Variables.locations[currenttile + mod].cooldown = 0
        Variables.locations[currenttile + mod].green = 0
        Variables.locations[currenttile + mod].regular = 0
        Variables.locations[currenttile + mod].elite = 0
        Variables.locations[currenttile + mod].difficulty = 0
        Variables.locations[currenttile + mod].encounter = 10
    if type == "Farm":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[2], (25, 25))
        Variables.locations[currenttile + mod].type = 'Farm'
        Variables.locations[currenttile + mod].cooldown = 0
        Variables.locations[currenttile + mod].green = 0
        Variables.locations[currenttile + mod].regular = 0
        Variables.locations[currenttile + mod].elite = 0
        Variables.locations[currenttile + mod].difficulty = 0
        Variables.locations[currenttile + mod].encounter = 10
    if type == "Fire":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[3], (25, 25))
        Variables.locations[currenttile + mod].type = 'Fire'
        Variables.locations[currenttile + mod].cooldown = 0
        Variables.locations[currenttile + mod].green = 0
        Variables.locations[currenttile + mod].regular = 0
        Variables.locations[currenttile + mod].elite = 0
        Variables.locations[currenttile + mod].difficulty = 0
        Variables.locations[currenttile + mod].encounter = 25
    if type == "Cave":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[4], (25, 25))
        Variables.locations[currenttile + mod].type = 'Cave'
        Variables.locations[currenttile + mod].cooldown = 0
        Variables.locations[currenttile + mod].green = 0
        Variables.locations[currenttile + mod].regular = 0
        Variables.locations[currenttile + mod].elite = 0
        Variables.locations[currenttile + mod].difficulty = 0
    if type == "Tomb":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[5], (25, 25))
        Variables.locations[currenttile + mod].type = 'Tomb'
        Variables.locations[currenttile + mod].cooldown = 15
        Variables.locations[currenttile + mod].green = random.randint(1000, 1500)
        Variables.locations[currenttile + mod].regular = random.randint(250, 750)
        Variables.locations[currenttile + mod].elite = random.randint(1, 50)
        Variables.locations[currenttile + mod].difficulty = 50
        Variables.locations[currenttile + mod].encounter = 100
    if type == "Mountain":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[6], (25, 25))
        Variables.locations[currenttile + mod].type = 'Mountain'
        Variables.locations[currenttile + mod].cooldown = 0
        Variables.locations[currenttile + mod].green = 0
        Variables.locations[currenttile + mod].regular = 0
        Variables.locations[currenttile + mod].elite = 0
        Variables.locations[currenttile + mod].difficulty = 0
        Variables.locations[currenttile + mod].encounter = 25
    if type == "Boulder":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[7], (25, 25))
        Variables.locations[currenttile + mod].type = 'Boulder'
        Variables.locations[currenttile + mod].cooldown = 0
        Variables.locations[currenttile + mod].green = 0
        Variables.locations[currenttile + mod].regular = 0
        Variables.locations[currenttile + mod].elite = 0
        Variables.locations[currenttile + mod].difficulty = 0
        Variables.locations[currenttile + mod].encounter = 15
    if type == "Cave2":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[8], (25, 25))
        Variables.locations[currenttile + mod].type = 'Cave2'
        Variables.locations[currenttile + mod].cooldown = 25
        Variables.locations[currenttile + mod].green = random.randint(100, 150)
        Variables.locations[currenttile + mod].regular = random.randint(25, 75)
        Variables.locations[currenttile + mod].elite = random.randint(1, 50)
        Variables.locations[currenttile + mod].difficulty = 25
        Variables.locations[currenttile + mod].encounter = 100
    if type == "Stone":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[9], (25, 25))
        Variables.locations[currenttile + mod].type = 'Stone'
        Variables.locations[currenttile + mod].cooldown = 0
        Variables.locations[currenttile + mod].green = 0
        Variables.locations[currenttile + mod].regular = 0
        Variables.locations[currenttile + mod].elite = 0
        Variables.locations[currenttile + mod].difficulty = 0
        Variables.locations[currenttile + mod].encounter = 15
    if type == "Rock":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[10], (25, 25))
        Variables.locations[currenttile + mod].type = 'Rock'
        Variables.locations[currenttile + mod].cooldown = 0
        Variables.locations[currenttile + mod].green = 0
        Variables.locations[currenttile + mod].regular = 0
        Variables.locations[currenttile + mod].elite = 0
        Variables.locations[currenttile + mod].difficulty = 0
        Variables.locations[currenttile + mod].encounter = 10
    if type == "Scourge":
        Variables.locations[currenttile + mod].image = pygame.transform.scale(Variables.mapimage[12], (25, 25))
        Variables.locations[currenttile + mod].type = 'Scourge'
        Variables.locations[currenttile + mod].cooldown = 10
        Variables.locations[currenttile + mod].green = random.randint(3000, 5000)
        Variables.locations[currenttile + mod].regular = random.randint(100, 1000)
        Variables.locations[currenttile + mod].elite = random.randint(25, 100)
        Variables.locations[currenttile + mod].difficulty = 100
        Variables.locations[currenttile + mod].encounter = 0000

def getMapLocationData(map_type):

    global type, image, cooldown, green, regular, elite, difficulty, encounter


    if map_type == 'Forest':
        type = "forest"
        image = 0
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 15
    elif map_type == 'Water':
        type = "water"
        image = 1
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 10
    elif map_type =="Farm":
        type = "farm"
        image = 2
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 10
    elif map_type == "Fire":
        type = "fire"
        image = 3
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 25
    elif map_type == "Cave":
        type = "cave"
        image = 4
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 30
    elif map_type == "Tomb":
        type = "tomb"
        image = 5
        cooldown = 15
        green = random.randint(1000, 1500)
        regular = random.randint(250, 750)
        elite = random.randint(1, 50)
        difficulty = 50
        encounter = 100
    elif map_type == "Mountain":
        type = "mountain"
        image = 6
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 25
    elif map_type == 8:
        type = "boulder"
        image = 7
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 15
    elif map_type == "Cave2":
        type = "cave2"
        image = 8
        cooldown = 25
        green = random.randint(100, 150)
        regular = random.randint(25, 75)
        elite = random.randint(1, 50)
        difficulty = 25
        encounter = 100
    elif map_type == "Stone":
        type = "stone"
        image = 9
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 15
    elif map_type == "Rock":
        type = "rock"
        image = 10
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 10
    elif map_type=="Scourge":
        type = "scourge"
        image = 12
        cooldown = 10
        green = random.randint(3000, 5000)
        regular = random.randint(100, 1000)
        elite = random.randint(25, 100)
        difficulty = 100
        encounter = 100
    else:
        type = "grassland"
        image = 11
        cooldown = 0
        green = 0
        regular = 0
        elite = 0
        difficulty = 0
        encounter = 10
    return type,image,cooldown, green, regular , elite, difficulty,encounter