from random import randint, uniform
import pygame

import graphics

# Screen Information 16/9 aspect ratio
SCREEN_WIDTH = graphics.Texture.SCALED_RESOLUTION[0] * 16
SCREEN_HEIGHT = graphics.Texture.SCALED_RESOLUTION[1] * 9

COLORS = {
    "red": (255, 0, 0),
    "orange": (255, 127, 0),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "indigo": (75, 0, 130),
    "violet": (148, 0, 211),
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "black": (0, 0, 0)
}

class Player:
    def __init__(self, name, x, y, color) -> None:
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

    def update(self, surface):
        if (self.can_run and self.x < self.max_distance):
            self.x += self.speed
        else:
            self.can_run = False
        
        self.tx = self.x + self.x_offset
        self.ty = self.y + self.y_offset
            
        pygame.draw.rect(surface, self.color, (self.tx, self.ty, self.size, self.size))

class Race:

    FINISHLINE_RESOLUTION = (int(graphics.Texture.SCALED_RESOLUTION[0] / 2), int(graphics.Texture.SCALED_RESOLUTION[1] / 2))

    def __init__(self, distance) -> None:
        self.distance = distance

        self.racers = []
        self.finished_index = []
        self.winner_index = None

        # self.fastest_racer_index = None
        self.x_view_offset = 0
        self.x_view_offset_threshold = SCREEN_WIDTH * 0.5

    def start_race(self, racers, x, y):
        # Reset
        self.racers = []
        self.finished_index = []
        self.winner_index = None

        # self.fastest_racer_index = None
        self.x_view_offset = 0

        color_keys = list(COLORS)
        for i in range(racers):
            self.racers.append(Player(f"Player {i}", x, y, COLORS[color_keys[i % len(COLORS)]]))
        
        # Print out the details (name, speed, max distance) of each racer
        for i in range(len(self.racers)):
            racer = self.racers[i]
            print(f"{racer.name} Speed: {racer.speed} Max Distance: {racer.max_distance}")

    def determine_winner(self):
        max_speed = None
        for i in range(len(self.racers)):
            racer = self.racers[i]
            if (racer.max_distance >= self.distance):
                # self.winner_index = self.racers.index(max(self.racers, key=lambda x: x.speed))
                if ((max_speed == None) or (racer.speed > max_speed)):
                    max_speed = racer.speed
                    self.winner_index = i

        # If the racers are still competing and a winner isn't chosen yet
        # if ((len(self.finished_index) != len(self.racers)) and (self.winner_index == None)):
        #     for i in range(len(self.racers)):
        #         racer = self.racers[i]
                
        #         if ((not racer.can_run) and (racer.max_distance >= self.distance)):
        #             if (i not in self.finished_index):
        #                 self.finished_index.append(i)
        # else:
        #     # Find winner based of the speed of those that finished the race
        #     max_speed = None
        #     for i in self.finished_index:
        #         if ((max_speed == None) or (self.racers[i].speed > max_speed)):
        #             max_speed = self.racers[i].speed
        #             self.winner_index = i

        #     print(self.winner_index)

    def update(self, surface, finishline_y, depth):
        # Track winning racer
        self.x_view_offset = (self.racers[self.winner_index].x - self.x_view_offset_threshold) if (self.racers[self.winner_index].x >= self.x_view_offset_threshold) else 0
        # self.fastest_racer_index = self.racers.index(max(self.racers, key=lambda x: x.x))
        # self.determine_winner()

        for i in range(len(self.racers)):
            racer = self.racers[i]
            racer.x_offset = -self.x_view_offset
            racer.update(surface)
        
        # pygame.draw.rect(surface, COLORS["black"], (self.distance - self.x_view_offset, finishline_y, res[0], height))
        for i in range(int(graphics.Texture.SCALED_RESOLUTION[0] / Race.FINISHLINE_RESOLUTION[0])):
            for j in range(int(graphics.Texture.SCALED_RESOLUTION[1] / Race.FINISHLINE_RESOLUTION[1]) * depth):
                ie = True if i%2 == 0 else False
                je = True if j%2 == 0 else False

                color_xor = ie ^ je
                color = (255, 255, 255) if color_xor else (0, 0, 0)

                x = (self.distance - self.x_view_offset) + (i * Race.FINISHLINE_RESOLUTION[0])
                y = finishline_y + (j * Race.FINISHLINE_RESOLUTION[1])
                pygame.draw.rect(surface, color, (x, y, Race.FINISHLINE_RESOLUTION[0], Race.FINISHLINE_RESOLUTION[1]))
