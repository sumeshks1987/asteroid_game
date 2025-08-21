import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers = None
    
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collides_with(self, other: "CircleShape") -> bool:
        """Return True if this circle overlaps another circle."""
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)