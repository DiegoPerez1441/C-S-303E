from typing import Union, Tuple

import pygame
from pygame.locals import *

_Color = Tuple[int, int, int]

pygame.init()

sys_font = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 24)

def render_text(surface: pygame.surface.Surface, text: str, x: Union[int, float], y: Union[int, float], color: _Color) -> None:
    img = font.render(text, True, color)
    rect = img.get_rect()
    surface.blit(img, (x, y))