import pygame
from circleshape import CircleShape  # Assuming your CircleShape class is in circle_shape.py
from constants import *

class Asteroid(CircleShape):
    # Set static containers (groups)
    containers = None  # This will be set in main.py

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt