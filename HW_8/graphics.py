from random import random
from abc import ABC, abstractmethod
import pygame

class Texture(ABC):
    TEXTURE_ATLAS = pygame.image.load("HW_8/1.17_Pre-release_3_blocks.png-atlas.png")
    RESOLUTION = (16, 16)
    SCALE = 4
    SCALED_RESOLUTION = (RESOLUTION[0] * SCALE, RESOLUTION[1] * SCALE)

    @abstractmethod
    def draw(self, surface):
        pass

class Grass(Texture):
    INDEX = (25, 0)
    tmp_surface = pygame.Surface((Texture.RESOLUTION[0], Texture.RESOLUTION[1]))

    def __init__(self, x, y) -> None:
        # res = self.RESOLUTION[0] # CHECK THIS OUT LATER
        self.x = x
        self.y = y

    def draw(self, surface):
        # res = self.RESOLUTION[0]
        crop_start_x = Grass.INDEX[0] * Texture.RESOLUTION[0]
        crop_start_y = Grass.INDEX[1] * Texture.RESOLUTION[1]

        # surface.blit(self.TEXTURE_ATLAS, (self.x, self.y), (crop_start_x, crop_start_y, res, res))

        # Draw texture onto a temporary surface
        Grass.tmp_surface.blit(Texture.TEXTURE_ATLAS, (self.x, self.y), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
        # Scale tmp_surface and blit onto surface
        surface.blit(pygame.transform.scale(Grass.tmp_surface, (Texture.SCALED_RESOLUTION[0], Texture.SCALED_RESOLUTION[1])), (self.x, self.y))


# class Dirt(Texture):
#     INDEX = (21, 10)
#     tmp_surface = pygame.Surface((Texture.RESOLUTION[0], Texture.RESOLUTION[1]))

#     def __init__(self, x, y) -> None:
#         # res = self.RESOLUTION[0] # CHECK THIS OUT LATER
#         self.x = x
#         self.y = y

#     def draw(self, surface):
#         # res = self.RESOLUTION[0]
#         crop_start_x = self.INDEX[0] * Texture.RESOLUTION[0]
#         crop_start_y = self.INDEX[1] * Texture.RESOLUTION[1]

#         # surface.blit(self.TEXTURE_ATLAS, (self.x, self.y), (crop_start_x, crop_start_y, res, res))

#         # Draw texture onto a temporary surface
#         self.tmp_surface.blit(self.TEXTURE_ATLAS, (self.x, self.y), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
#         # Scale tmp_surface and blit onto surface
#         surface.blit(pygame.transform.scale(self.tmp_surface, (Texture.SCALED_RESOLUTION[0], Texture.SCALED_RESOLUTION[1])), (self.x, self.y))

class Dirt(Texture):
    INDEX = (21, 10)

    def __init__(self, x, y) -> None:
        res = self.RESOLUTION[0] # CHECK THIS OUT LATER
        self.x = x
        self.y = y

    def draw(self, surface):
        res = self.RESOLUTION[0]
        crop_start_x = self.INDEX[0] * res
        crop_start_y = self.INDEX[1] * res

        surface.blit(self.TEXTURE_ATLAS, (self.x, self.y), (crop_start_x, crop_start_y, res, res))

class Floor():
    def __init__(self, length, depth, SCREEN_WIDTH, SCREEN_HEIGHT) -> None:
        self.length = length
        self.depth = depth

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        # Initialize 2D block_map array with Floor_Brick objects
        self.block_map = [[] for d in range(self.depth)]
        # self.block_map = [[Grass() for l in range(self.length)] for d in range(self.depth)]

        for l in range(self.length):
            for d in range(self.depth):
                pos_x = l * Texture.SCALED_RESOLUTION[0]
                pos_y = (d * Texture.SCALED_RESOLUTION[1]) + (self.SCREEN_HEIGHT - (self.depth * Texture.SCALED_RESOLUTION[1]))
                # Top layer = Grass
                # Everyother layer below = Dirt
                if (d == 0):
                    self.block_map[d].append(Grass(pos_x, pos_y))
                else:
                    self.block_map[d].append(Dirt(pos_x, pos_y))

    def draw(self, surface):
        for l in range(self.length):
            for d in range(self.depth):
                obj_instance = self.block_map[d][l]
                obj_instance.draw(surface)