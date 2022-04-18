from random import randint, uniform

class Player:
    def __init__(self) -> None:
        self.speed = randint(1, 10)
        self.max_distance = uniform(150, 500)

class Race:
    def __init__(self, distance) -> None:
        self.distance = distance