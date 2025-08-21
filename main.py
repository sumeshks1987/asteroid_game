import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    # Instantiate player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Update all objects
        for obj in updatables:
            obj.update(dt)
            
        # Player vs Asteroids (Game over!)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return  # exit main immediately
            
        # Shots vs Asteroids (Destruction)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.position.distance_to(shot.position) < asteroid.radius:
                    asteroid.split()   # ✅ instead of just kill()
                    shot.kill()

        # Fill the screen black
        screen.fill((0, 0, 0))  # RGB black
        
        # Draw all objects
        for obj in drawables:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()
        
        # Limit the frame rate to 60 FPS and get delta time
        dt = clock.tick(60) / 1000  # dt in seconds
        # updatables.update(dt)

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
