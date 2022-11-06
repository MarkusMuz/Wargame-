import pygame
from pygame.locals import *
from unit import Unit

class Infantry(Unit):
    
    def show_info(self):
        print(self.name, " ", self.fraction, " ", self.type, " ", self.coordinates, " ", self.morale, " ", self.number_of_people, " ", self.technic)
