import pygame
import menuscreen.menuscreen as menu

# Initialize Pygame
pygame.init()

# Set up game window
screen = pygame.display.set_mode((800, 600))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Snake Game")

# Set up and display menu screen
menu.view_menu_screen(screen)
