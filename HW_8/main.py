import pygame, sys
from pygame.locals import *

import graphics

# Initialize pygame
pygame.init()

FPS = 30
FRAME_PER_SEC = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen Information 16/9 aspect ratio
SCREEN_WIDTH = graphics.Texture.SCALED_RESOLUTION[0] * 16
SCREEN_HEIGHT = graphics.Texture.SCALED_RESOLUTION[1] * 9

DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY_SURF.fill(WHITE)
pygame.display.set_caption("HW 8")

ground = graphics.Floor(10, 2, SCREEN_WIDTH, SCREEN_HEIGHT)
g = graphics.Grass(0, 0)
d = graphics.Dirt(64, 0)

def main():
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY_SURF.fill(WHITE)

        # Draw here
        ground.draw(DISPLAY_SURF)
        g.draw(DISPLAY_SURF)
        d.draw(DISPLAY_SURF)

        pygame.display.update()
        FRAME_PER_SEC.tick(FPS)

if __name__ == "__main__":
    main()