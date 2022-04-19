from random import randint, uniform

class Player:
    def __init__(self, name) -> None:
        self.name = f"{name}"
        self.speed = randint(1, 10)
        self.max_distance = uniform(150, 500)

        self.can_run = True
        self.x = 0

    def update(self):
        if (self.can_run and self.x < self.max_distance):
            self.x += self.speed
        else:
            self.can_run = False

class Race:
    def __init__(self, distance) -> None:
        self.distance = distance

    def start_race(self, racers):
        pass

    def determine_winner(self):
        pass