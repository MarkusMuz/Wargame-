import os
import pygame
import json
from pygame.locals import *

class Unit:
    def __init__(self, screen, name = "", fraction = "", type = "", coordinates = [0, 0]) -> None:
        
        self.screen = screen
        
        img_path = "./images/" + fraction + "_" + type + ".jpg"
        json_path = "./units_compound/" + fraction + "_" + type + ".json"
        
        with open(json_path) as file:
            json_data = json.load(file)
            
        self.name = name
        self.fraction = fraction
        self.type = type
        self.coordinates = coordinates
        
        self.number_of_people = json_data["number_of_people"]    
        self.technic = json_data["technic"]                      
        self.morale = 1.0
        
        self.img = pygame.image.load(os.path.abspath(img_path))
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.coordinates[0]
        self.rect.bottom = self.coordinates[1]
        
    def blitme(self):   #draw unit on the screen
        self.screen.blit(self.img, self.rect)
