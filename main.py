import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    # Instantiate player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the loop if the window is closed

        # Update player
        player.update(dt)

        # Fill the screen black
        screen.fill((0, 0, 0))  # RGB black
        
        # Draw the player
        player.draw(screen)

        # Update the display
        pygame.display.flip()
        
        # Limit the frame rate to 60 FPS and get delta time
        dt = clock.tick(60) / 1000  # dt in seconds

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
