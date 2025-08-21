import pygame
from circleshape import CircleShape  # Assuming your CircleShape class is in circle_shape.py
from constants import *
import random

class Asteroid(CircleShape):
    # Set static containers (groups)
    containers = None  # This will be set in main.py

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)   # ✅ pass x, y, radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (200, 200, 200), (radius, radius), radius, 2)
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
        
    def split(self):
        """Split asteroid into 2 smaller ones, or disappear if already smallest."""
        if self.radius <= 15:   # small asteroid → gone
            self.kill()
            return

        # decide new radius (half of current)
        new_radius = self.radius // 2

        # spawn 2 new asteroids with slightly different velocities
        for _ in range(2):
            vel = self.velocity.rotate(random.uniform(-30, 30)) * 1.2
            new_ast = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast.velocity = vel

        # kill the original asteroid
        self.kill()