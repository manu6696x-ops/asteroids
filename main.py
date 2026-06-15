import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    while True:
        log_state()
        pygame.Surface.fill(screen, (0, 0, 0))  # Clear screen with black
        for event in pygame.event.get():
            pass  # Placeholder for event handling
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
