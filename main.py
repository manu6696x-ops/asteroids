import pygame
from player import *
from circleshape import *
from constants import *
from asteroid import *
from logger import log_state , log_event
from asteroidfield import *
from shot import Shot
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x, y)
    asteroid_field = AsteroidField()
    
    

    while True:
        log_state()
        pygame.Surface.fill(screen, (0, 0, 0))  # Clear screen with black
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if object.collides_with(shot):
                    log_event("asteroid_shot")
                    object.kill()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # Calculate delta time or fps

if __name__ == "__main__":
    main()