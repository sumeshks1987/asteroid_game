import pygame
from circleshape import CircleShape  # assuming you have this class in circle_shape.py
from constants import *
from shot import Shot  # assuming you have a Shot class defined in shot.py

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt, forward=True):
        direction = 1 if forward else -1
        vector = pygame.Vector2(0, 1).rotate(self.rotation) * direction
        self.position += vector * PLAYER_SPEED * dt
        
    # Update method for key input
    def update(self, dt):
        self.position += self.velocity * dt
        
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            if self.shoot_timer < 0:
                self.shoot_timer = 0
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)   # Rotate right
            
        if keys[pygame.K_w]:
            self.move(dt, forward=True)   # Move forward
        if keys[pygame.K_s]:
            self.move(dt, forward=False)  # Move backward
            
    def shoot(self):
        # Only shoot if timer is ready
        if self.shoot_timer > 0:
            return
        
        # Reset cooldown
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        
        # Starting velocity in "up" direction
        direction = pygame.Vector2(0, 1).rotate(self.rotation)  
        velocity = direction * PLAYER_SHOOT_SPEED
        
        Shot(self.position.x, self.position.y, velocity)