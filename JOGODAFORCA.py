#Jogo da forca: acerte ou morra
import sys

import pygame
from pygame.locals import *

pygame.init()
d = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    d.fill("pink")
    pygame.display.update()

