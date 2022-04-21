from random import randint, uniform
import pygame

import graphics

# Screen Information 16/9 aspect ratio
SCREEN_WIDTH = graphics.Texture.SCALED_RESOLUTION[0] * 16
SCREEN_HEIGHT = graphics.Texture.SCALED_RESOLUTION[1] * 9

class Player:
    def __init__(self, name, x, y) -> None:
        self.name = f"{name}"
        self.speed = randint(2, 10)
        self.max_distance = uniform(500, 800)

        self.can_run = True
        self.size = 20

        self.x = x
        self.y = y - self.size

        self.x_offset = 0
        self.y_offset = 0
        self.tx = self.x + self.x_offset
        self.ty = self.y + self.y_offset

    def update(self, surface):
        self.tx = self.x + self.x_offset
        self.ty = self.y + self.y_offset

        if (self.can_run and self.x < self.max_distance):
            self.x += self.speed
        else:
            self.can_run = False
            
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.size, self.size))

class Race:
    def __init__(self, distance) -> None:
        self.distance = distance

        self.racers = []
        self.finished_index = []
        self.winner_index = None

        self.fastest_racer_index = None
        self.x_view_offset = 0

        self.x_view_offset_threshold = SCREEN_WIDTH * 0.7

    def start_race(self, racers, x, y):
        # Reset
        self.racers = []
        self.finished_index = []
        self.winner_index = None

        self.fastest_racer_index = None
        self.x_view_offset = 0

        for i in range(racers):
            self.racers.append(Player(f"Player {i}", x, y))
        
        # Print out the details (name, speed, max distance) of each racer
        for i in range(len(self.racers)):
            racer = self.racers[i]
            print(f"{racer.name} Speed: {racer.speed} Max Distance: {racer.max_distance}")

    def determine_winner(self):
        # If the racers are still competing and a winner isn't chosen yet
        if ((len(self.finished_index) != len(self.racers)) and (self.winner_index == None)):
            for i in range(len(self.racers)):
                racer = self.racers[i]
                
                if ((not racer.can_run) and (racer.max_distance >= self.distance)):
                    if (i not in self.finished_index):
                        self.finished_index.append(i)
        else:
            # Find max speed of racers
            pass
            

    def update(self, surface):
        for i in range(len(self.racers)):
            racer = self.racers[i]
            racer.update(surface)
        
        self.fastest_racer_index = self.racers.index(max(self.racers, key=lambda x: x.x))
        self.x_view_offset = (self.racers[self.fastest_racer_index].x - self.x_view_offset_threshold) if (self.racers[self.fastest_racer_index].x >= self.x_view_offset_threshold) else 0
        self.determine_winner()