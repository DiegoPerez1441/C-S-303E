from typing import Tuple

from random import randint, uniform
import pygame

import graphics
from colors import COLORS
from text import render_text

_Color = Tuple[int, int, int]

# Screen Information 16/9 aspect ratio
SCREEN_WIDTH = graphics.Texture.SCALED_RESOLUTION[0] * 16
SCREEN_HEIGHT = graphics.Texture.SCALED_RESOLUTION[1] * 9

class Player:
    def __init__(self, name: str, x: int, y: int, color: _Color) -> None:
        self.name = f"{name}"
        self.speed = randint(2, 10)
        self.max_distance = uniform(500, 1000)

        self.can_run = True
        self.size = int(graphics.Texture.SCALED_RESOLUTION[0] / 4)
        self.color = color

        self.x = x
        self.y = y - self.size

        self.x_offset = 0
        self.y_offset = 0
        self.tx = self.x + self.x_offset
        self.ty = self.y + self.y_offset

    def update(self, surface: pygame.surface.Surface) -> None:
        if (self.can_run and self.x < self.max_distance):
            self.x += self.speed
        else:
            self.can_run = False
        
        self.tx = self.x + self.x_offset
        self.ty = self.y + self.y_offset
            
        pygame.draw.rect(surface, self.color, (self.tx, self.ty, self.size, self.size))

class Race:
    FINISH_LINE_RESOLUTION = (int(graphics.Texture.SCALED_RESOLUTION[0] / 2), int(graphics.Texture.SCALED_RESOLUTION[1] / 2))

    def __init__(self, distance: int) -> None:
        self.distance = distance

        self.racers = []
        self.winner = None

        self.stopped_racers = []
        self.finished_racers = []
        self.race_finished = False

        self.x_view_offset = 0
        self.x_view_offset_threshold = SCREEN_WIDTH * 0.5

    def start_race(self, num_racers: int, x: int, y: int) -> None:
        # Reset
        self.racers = []
        self.winner = None

        self.stopped_racers = []
        self.finished_racers = []
        self.race_finished = False

        self.x_view_offset = 0

        color_keys = list(COLORS)
        for i in range(num_racers):
            self.racers.append(Player(f"Player {i}", x, y, COLORS[color_keys[i % len(COLORS)]]))
        
        # Print out the details (name, speed, max distance) of each racer
        for i in range(len(self.racers)):
            racer = self.racers[i]
            print(f"{racer.name} Speed: {racer.speed} Max Distance: {racer.max_distance}")

    def determine_winner(self) -> None:
        max_speed = None
        for i in range(len(self.racers)):
            racer = self.racers[i]
            if (racer.max_distance >= self.distance):
                # self.winner_index = self.racers.index(max(self.racers, key=lambda x: x.speed))
                if ((max_speed == None) or (racer.speed > max_speed)):
                    max_speed = racer.speed
                    self.winner = racer

    def leaderboard_update(self, surface: pygame.surface.Surface) -> None:
        # If racers are still competing
        if ((len(self.stopped_racers) != len(self.racers)) and (not self.race_finished)):
            for i in range(len(self.racers)):
                racer = self.racers[i]
                
                if ((not racer.can_run) and (racer.max_distance >= self.distance)):
                    if (racer not in self.finished_racers):
                        self.finished_racers.append(racer)
                
                if (not racer.can_run):
                    if (racer not in self.stopped_racers):
                        self.stopped_racers.append(racer)
        else:
            self.race_finished = True


        if (self.race_finished):
            if (self.winner is not None):
                # Sort based on speed if race is done
                self.finished_racers.sort(reverse=True, key=lambda x: x.speed)

                render_text(surface, "Finished", 20, 20, (255, 0, 0))
                render_text(surface, f"Winner: {self.winner.name}", 120, 20, (255, 0, 0))

                for i in range(len(self.finished_racers)):
                    racer = self.finished_racers[i]
                    x = 20
                    y = 40 + (i*20)

                    render_text(surface, f"{i + 1}. ", x, y, (255, 0, 0))
                    pygame.draw.rect(surface, racer.color, (x + 20, y, 10, 10))
                    render_text(surface, f" {racer.name} Speed: {racer.speed} Max Distance: {racer.max_distance:0.2f}", x + 30, y, (255, 0, 0))

            else:
                # Show leaderboard in the case that there is no winner
                self.racers.sort(key=lambda x: x.x)
                render_text(surface, "Leaderboard (No Winners)", 20, 20, (255, 0, 0))

                for i in range(len(self.racers)):
                    racer = self.racers[i]
                    x = 20
                    y = 40 + (i*20)

                    render_text(surface, f"{i + 1}. ", x, y, (255, 0, 0))
                    pygame.draw.rect(surface, racer.color, (x + 20, y, 10, 10))
                    render_text(surface, f" {racer.name} Speed: {racer.speed} Max Distance: {racer.max_distance:0.2f}", x + 30, y, (255, 0, 0))

        else:
            # Sort based on position if race is not done
            self.racers.sort(reverse=True, key=lambda x: x.x)
            
            render_text(surface, "Leaderboard", 20, 20, (255, 0, 0))
            for i in range(len(self.racers)):
                racer = self.racers[i]
                x = 20
                y = 40 + (i*20)
                
                render_text(surface, f"{i + 1}. ", x, y, (255, 0, 0))
                pygame.draw.rect(surface, racer.color, (x + 20, y, 10, 10))
                render_text(surface, f" {racer.name} Speed: {racer.speed} Max Distance: {racer.max_distance:0.2f}", x + 30, y, (255, 0, 0))

    def update(self, surface: pygame.surface.Surface, finishline_y: int, depth: int) -> None:
        if (self.winner == None):
            # Track leading racer
            lead_racer = max(self.racers, key=lambda x: x.x)
            self.x_view_offset = (lead_racer.x - self.x_view_offset_threshold) if (lead_racer.x >= self.x_view_offset_threshold) else 0
        else:
            # Track winning racer
            self.x_view_offset = (self.winner.x - self.x_view_offset_threshold) if (self.winner.x >= self.x_view_offset_threshold) else 0    

        for i in range(len(self.racers)):
            racer = self.racers[i]
            racer.x_offset = -self.x_view_offset
            racer.update(surface)
        
        # pygame.draw.rect(surface, COLORS["black"], (self.distance - self.x_view_offset, finishline_y, res[0], height))
        for i in range(int(graphics.Texture.SCALED_RESOLUTION[0] / Race.FINISH_LINE_RESOLUTION[0])):
            for j in range(int(graphics.Texture.SCALED_RESOLUTION[1] / Race.FINISH_LINE_RESOLUTION[1]) * depth):
                ie = True if i%2 == 0 else False
                je = True if j%2 == 0 else False

                color_xor = ie ^ je
                color = (255, 255, 255) if color_xor else (0, 0, 0)

                # Winning after crossing the end of the finish line
                x = ((self.distance - self.x_view_offset) + (i * Race.FINISH_LINE_RESOLUTION[0]) - graphics.Texture.SCALED_RESOLUTION[0])
                y = finishline_y + (j * Race.FINISH_LINE_RESOLUTION[1])
                pygame.draw.rect(surface, color, (x, y, Race.FINISH_LINE_RESOLUTION[0], Race.FINISH_LINE_RESOLUTION[1]))
