import random

import Sprites
import Variables





def initiative(people,locations):
    Variables.locationunit.append(Sprites.locationUnits(Variables.unitimage[2],  1350, 750, 25, 25, 0,0))


    heroroll=random.randrange(1,100)
    locationunitroll= random.randrange(1,100)
    Variables.people[people].herototalinit= heroroll + Variables.people[people].combatskill
    Variables.locationunit[0].totalinit = locationunitroll + Variables.locations[locations].difficulty
    if Variables.people[people].herototalinit >= Variables.locationunit[0].totalinit:
        Variables.people[people].attacker=True

        print('hero wins! ')
        print('total Hero Initiative: '+ str(Variables.people[people].herototalinit))
        print('total Location Initiative: ' + str(Variables.locationunit[0].totalinit))
        print(Variables.people[people].attacker)
    else:
        print('locatin wins!!')
        print('total Hero Initiative: ' + str(Variables.people[people].herototalinit))
        print('total Location Initiative: ' + str(Variables.locationunit[0].totalinit))
