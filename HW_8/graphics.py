from abc import ABC, abstractmethod
from typing import Tuple

from random import random
import pygame

_IndexCoordinate = Tuple[int, int]

class Texture(ABC):
    TEXTURE_ATLAS = pygame.image.load("HW_8/Texture_Atlas.png")
    RESOLUTION = (16, 16)
    SCALE = 4
    SCALED_RESOLUTION = (RESOLUTION[0] * SCALE, RESOLUTION[1] * SCALE)

    @abstractmethod
    def draw(self, surface):
        pass

class Block(Texture):
    INDEX: _IndexCoordinate = (0, 0) # Default value
    tmp_surface = pygame.Surface((Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
    tmp_surface.fill((255, 0, 0)) # [DEBUG]: Color tmp_surface red upon init

    def __init__(self, x: int, y: int) -> None:
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
        crop_start_x = Block.INDEX[0] * Texture.RESOLUTION[0]
        crop_start_y = Block.INDEX[1] * Texture.RESOLUTION[1]

        # Original
        # surface.blit(self.TEXTURE_ATLAS, (self.x, self.y), (crop_start_x, crop_start_y, res, res))

        # Draw texture onto a temporary surface
        Block.tmp_surface.blit(Texture.TEXTURE_ATLAS, (0, 0), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))

        # Scale tmp_surface and blit onto surface
        # surface.blit(pygame.transform.scale(Block.tmp_surface, (Texture.SCALED_RESOLUTION[0], Texture.SCALED_RESOLUTION[1])), (self.x, self.y))
        surface.blit(pygame.transform.scale(Block.tmp_surface, Texture.SCALED_RESOLUTION), (self.tx, self.ty))

class Grass(Block):
    INDEX = (0, 0)
    tmp_surface = pygame.Surface((Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
    tmp_surface.fill((255, 0, 0)) # [DEBUG]: Color tmp_surface red upon init

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def draw(self, surface):
        crop_start_x = Grass.INDEX[0] * Texture.RESOLUTION[0]
        crop_start_y = Grass.INDEX[1] * Texture.RESOLUTION[1]

        # Draw texture onto a temporary surface
        Grass.tmp_surface.blit(Texture.TEXTURE_ATLAS, (0, 0), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))

        # Scale tmp_surface and blit onto surface
        surface.blit(pygame.transform.scale(Grass.tmp_surface, Texture.SCALED_RESOLUTION), (self.tx, self.ty))

class Dirt(Block):
    INDEX = (1, 0)
    tmp_surface = pygame.Surface((Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
    tmp_surface.fill((255, 0, 0)) # [DEBUG]: Color tmp_surface red upon init

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def draw(self, surface):
        crop_start_x = Dirt.INDEX[0] * Texture.RESOLUTION[0]
        crop_start_y = Dirt.INDEX[1] * Texture.RESOLUTION[1]

        # Draw texture onto a temporary surface
        Dirt.tmp_surface.blit(Texture.TEXTURE_ATLAS, (0, 0), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))

        # Scale tmp_surface and blit onto surface
        surface.blit(pygame.transform.scale(Dirt.tmp_surface, Texture.SCALED_RESOLUTION), (self.tx, self.ty))

class Stone(Block):
    INDEX = (2, 0)
    tmp_surface = pygame.Surface((Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
    tmp_surface.fill((255, 0, 0)) # [DEBUG]: Color tmp_surface red upon init

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def draw(self, surface):
        crop_start_x = Stone.INDEX[0] * Texture.RESOLUTION[0]
        crop_start_y = Stone.INDEX[1] * Texture.RESOLUTION[1]

        # Draw texture onto a temporary surface
        Stone.tmp_surface.blit(Texture.TEXTURE_ATLAS, (0, 0), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))

        # Scale tmp_surface and blit onto surface
        surface.blit(pygame.transform.scale(Stone.tmp_surface, Texture.SCALED_RESOLUTION), (self.tx, self.ty))

class Log_Oak(Block):
    INDEX = (0, 1)
    tmp_surface = pygame.Surface((Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
    tmp_surface.fill((255, 0, 0)) # [DEBUG]: Color tmp_surface red upon init

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def draw(self, surface):
        crop_start_x = Log_Oak.INDEX[0] * Texture.RESOLUTION[0]
        crop_start_y = Log_Oak.INDEX[1] * Texture.RESOLUTION[1]

        # Draw texture onto a temporary surface
        Log_Oak.tmp_surface.blit(Texture.TEXTURE_ATLAS, (0, 0), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))

        # Scale tmp_surface and blit onto surface
        surface.blit(pygame.transform.scale(Log_Oak.tmp_surface, Texture.SCALED_RESOLUTION), (self.tx, self.ty))

class Leaves_Oak(Block):
    INDEX = (0, 1)
    tmp_surface = pygame.Surface((Texture.RESOLUTION[0], Texture.RESOLUTION[1]))
    tmp_surface.fill((255, 0, 0)) # [DEBUG]: Color tmp_surface red upon init

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def draw(self, surface):
        crop_start_x = Leaves_Oak.INDEX[0] * Texture.RESOLUTION[0]
        crop_start_y = Leaves_Oak.INDEX[1] * Texture.RESOLUTION[1]

        # Draw texture onto a temporary surface
        Leaves_Oak.tmp_surface.blit(Texture.TEXTURE_ATLAS, (0, 0), (crop_start_x, crop_start_y, Texture.RESOLUTION[0], Texture.RESOLUTION[1]))

        # Scale tmp_surface and blit onto surface
        surface.blit(pygame.transform.scale(Leaves_Oak.tmp_surface, Texture.SCALED_RESOLUTION), (self.tx, self.ty))

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