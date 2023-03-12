import pygame
import sys
from pygame.locals import *

pygame.init()

#TELA
display = pygame.display.set_mode((900,600))
pygame.display.set_caption("Bandeira do Brasil")
display.fill((0,255,0))

#CORES
amarelo = (255,255,0)
verde = (0,255,0)
branco = (255,255,255)
azul = (0,0,255)

#FORMAS
pygame.draw.polygon(display,(amarelo),((225,300),(450,150),(675,300),(450,450)))
pygame.draw.circle(display, (azul), (450,300), 50)
pygame.draw.line(display, (branco), (400,300), (500,300), 10)

pygame.display.flip()

#QUIT
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()










