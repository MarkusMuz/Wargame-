import pygame
import sys
from pygame.locals import *
from settings import Settings
from infantry import Infantry


def run_game():
    pygame.init()
    game_settings = Settings()
    game_display = pygame.display.set_mode((game_settings.display_width, game_settings.display_height))
    pygame.display.set_caption("Wargame+")
    pygame.display.update()
    while (True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            print(event)
        game_display.fill(game_settings.bg_Colour)
        first_unit = Infantry(game_display, "1st Infantry", "red", "infantry", [100, 100])
        first_unit.blitme()
        first_unit.show_info()
        pygame.display.update()
        
run_game()