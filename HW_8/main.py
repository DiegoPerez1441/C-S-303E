import pygame, sys
from pygame.locals import *

import graphics
import utilities

# Initialize pygame
pygame.init()

FPS = 30
FRAME_PER_SEC = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SKY_BLUE = (135, 206, 235)

# Screen Information 16/9 aspect ratio
SCREEN_WIDTH = graphics.Texture.SCALED_RESOLUTION[0] * 16
SCREEN_HEIGHT = graphics.Texture.SCALED_RESOLUTION[1] * 9

DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY_SURF.fill(WHITE)
pygame.display.set_caption("HW 8")

def main():
    # Add one extra block to the right to compensate for transformations
    ground = graphics.Floor(int(SCREEN_WIDTH/graphics.Texture.SCALED_RESOLUTION[0] + 1), 2, SCREEN_WIDTH, SCREEN_HEIGHT)

    tree1 = graphics.Tree_Oak(0, 0)

    # Testing
    # g = graphics.Grass(0, 0)
    # d = graphics.Dirt(64, 0)

    race_1 = utilities.Race(800)
    print(f"race_1 Distance: {race_1.distance}")
    race_1.start_race(5, 0, ground.top_layer_height)

    race_1.determine_winner()
    print(f"Winner: {race_1.racers[race_1.winner_index].name}")

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        DISPLAY_SURF.fill(SKY_BLUE)
        
        # Testing
        # g.draw(DISPLAY_SURF)
        # d.draw(DISPLAY_SURF)

        # Draw here
        ground.draw(DISPLAY_SURF, race_1.x_view_offset, 0)
        tree1.draw(DISPLAY_SURF, race_1.x_view_offset, 0)
        
        race_1.update(DISPLAY_SURF, ground.top_layer_height, ground.depth)


        pygame.display.update()
        FRAME_PER_SEC.tick(FPS)

if __name__ == "__main__":
    main()