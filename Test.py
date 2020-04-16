# Comment out these two lines to go back to old Pygame version
import pygame

import pygame
from pygame import KEYDOWN, QUIT
import sys

def main():

    pygame.init()
    tilesize = 35
    size_x = 24
    size_y = 18
    screen_size = (tilesize * size_x, tilesize * size_y)
    screen = pygame.display.set_mode(screen_size, 0, 32)
    clock = pygame.time.Clock()

    stop_flag = False

    while not stop_flag:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


        screen.fill((75, 193, 114))


        for i in range (0, 10):

            box_surface_rect = pygame.Surface((90, 50), pygame.SRCALPHA)
            pygame.draw.rect(box_surface_rect, (255, 255, 255, 20), (0,0, 90,50))

            screen.blit(box_surface_rect, (150, 60))

        pygame.display.update()

        clock.tick(60)

if __name__ == '__main__':
    main()