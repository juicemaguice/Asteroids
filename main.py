import sys
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

def main():
    pygame.init()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)

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
        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    # ^ keep display.flip() as final call before loop


if __name__ == "__main__":
    main()