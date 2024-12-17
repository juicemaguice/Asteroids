import sys
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

def main():
    pygame.init()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    
    SCREEN_WIDTH = 1920
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock, dt = pygame.time.Clock(), 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")
        for obj in updatables:
            obj.update(dt)
        for ast in asteroids:
            if ast.is_colliding(player):
                print("Game over!")
                sys.exit()
            if ast.is_exiting():
                ast.kill()
            for shot in shots:
                if shot.is_colliding(ast):
                    ast.split()
                    shot.kill()
                    break
                if shot.is_exiting():
                    shot.kill()
        for obj in drawables:
            obj.draw(screen)

        if pygame.time.get_ticks() % 90 == 0:  # every second
            print(f"Number of asteroids: {len(asteroids)}")
            print(f"Number of shots    : {len(shots)}")

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    # ^ keep display.flip() as final call before loop


if __name__ == "__main__":
    main()