from random import randint, uniform
import pygame

class Player:
    def __init__(self, name, x, y) -> None:
        self.name = f"{name}"
        self.speed = randint(2, 10)
        self.max_distance = uniform(250, 500)

        self.can_run = True
        self.size = 20
        self.x = x
        self.y = y - self.size

    def update(self, surface):
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

    def start_race(self, racers, x, y):
        # Reset
        self.racers = []
        self.finished_index = []
        self.winner_index = None

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
        
        self.determine_winner()