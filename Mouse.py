import pygame
import Variables

class mouse:
    def __init__(self, mouse_x, mouse_y, selected_loc, current_loc, click_value, selectedx, selectedy):
        self.mouseX = mouse_x
        self.mouseY = mouse_y
        self.selectedLoc = selected_loc
        self.currentLoc = current_loc
        self.click_Value = click_value
        self.selectedx = selectedx
        self.selectedy = selectedy

    def get_mouse_pos(self):
        Variables.my_mouse.mouseX, Variables.my_mouse.mouseY = pygame.mouse.get_pos()

    def createMouse(self):
        Variables.my_mouse = mouse(0, 0, 0, 0, 0, 0, 0)