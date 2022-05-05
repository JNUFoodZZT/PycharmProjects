import pygame
import sys

screen = pygame.display.set_mode((1000,1000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.key == pygame.KEYDOWN:
            print(pygame.key)

    pygame.display.set_caption("鸿儒羊驼")