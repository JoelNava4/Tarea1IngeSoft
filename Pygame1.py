import pygame, sys
from pygame.locals import *

pygame.init()

Pantalla = pygame.display.set_mode((500,400))

pygame.display.set_caption("Mi primer juego")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
