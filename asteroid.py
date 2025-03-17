import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def split(self):
        print(self.radius)
        if self.radius > ASTEROID_MIN_RADIUS:
            self.kill()
            velocity = self.velocity.rotate(random.uniform(0, 50))
            asteroid1 = self.spawn(
                self.radius - ASTEROID_MIN_RADIUS, self.position, velocity * 1.2
            )
            asteroid2 = self.spawn(
                self.radius - ASTEROID_MIN_RADIUS, self.position, -velocity
            )
            return [asteroid1, asteroid2]
        else:
            return None
