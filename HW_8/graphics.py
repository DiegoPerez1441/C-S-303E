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
    tmp_surface.fill((255, 0, 0)) # [DEBUG]: Color tmp_surface red upon init

    def __init__(self, x, y) -> None:
        # res = self.RESOLUTION[0] # CHECK THIS OUT LATER
        self.x = x
        self.y = y

        self.x_offset = 0
        self.y_offset = 0
        self.tx = self.x + self.x_offset
        self.ty = self.y + self.y_offset

    def update(self):
        self.tx = self.x + self.x_offset
        self.ty = self.y + self.y_offset

    def draw(self, surface):
        crop_start_x = Grass.INDEX[0] * Texture.RESOLUTION[0]
        crop_start_y = Grass.INDEX[1] * Texture.RESOLUTION[1]

        # Original
        # surface.blit(self.TEXTURE_ATLAS, (self.x, self.y), (crop_start_x, crop_start_y, res, res))

        # Draw texture onto a temporary surface
        Grass.tmp_surface.blit(Texture.TEXTURE_ATLAS, (0, 0), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))

        # Scale tmp_surface and blit onto surface
        # surface.blit(pygame.transform.scale(Grass.tmp_surface, (Texture.SCALED_RESOLUTION[0], Texture.SCALED_RESOLUTION[1])), (self.x, self.y))
        surface.blit(pygame.transform.scale(Grass.tmp_surface, Texture.SCALED_RESOLUTION), (self.tx, self.ty))

class Dirt(Texture):
    INDEX = (21, 10)
    tmp_surface = pygame.Surface((Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
    tmp_surface.fill((255, 0, 0)) # [DEBUG]: Color tmp_surface red upon init

    def __init__(self, x, y) -> None:
        # res = self.RESOLUTION[0] # CHECK THIS OUT LATER
        self.x = x
        self.y = y
        
        self.x_offset = 0
        self.y_offset = 0
        self.tx = self.x + self.x_offset
        self.ty = self.y + self.y_offset

    def update(self):
        self.tx = self.x + self.x_offset
        self.ty = self.y + self.y_offset

    def draw(self, surface):
        crop_start_x = Dirt.INDEX[0] * Texture.RESOLUTION[0]
        crop_start_y = Dirt.INDEX[1] * Texture.RESOLUTION[1]

        # Original
        # surface.blit(self.TEXTURE_ATLAS, (self.x, self.y), (crop_start_x, crop_start_y, res, res))

        # Draw texture onto a temporary surface
        Dirt.tmp_surface.blit(Texture.TEXTURE_ATLAS, (0, 0), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
        
        # Scale tmp_surface and blit onto surface
        # surface.blit(pygame.transform.scale(Dirt.tmp_surface, (Texture.SCALED_RESOLUTION[0], Texture.SCALED_RESOLUTION[1])), (self.x, self.y))
        surface.blit(pygame.transform.scale(Dirt.tmp_surface, Texture.SCALED_RESOLUTION), (self.tx, self.ty))

class Floor():
    def __init__(self, length, depth, SCREEN_WIDTH, SCREEN_HEIGHT) -> None:
        self.length = length
        self.depth = depth

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.top_layer_height = self.SCREEN_HEIGHT - (self.depth * Texture.SCALED_RESOLUTION[1])

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

    def draw(self, surface, x_offset, y_offset):
        for l in range(self.length):
            for d in range(self.depth):
                obj_instance = self.block_map[d][l]

                l_x_offset = -(x_offset % Texture.SCALED_RESOLUTION[0])

                obj_instance.x_offset = l_x_offset
                obj_instance.update()
                obj_instance.draw(surface)