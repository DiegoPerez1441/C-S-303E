import pygame

sys_font = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 16)

def render_text(text: str, color) -> None:
    img = font.render(text, True, color)
    rect = img.get_rect()