import sys
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")
    updatables, drawables, asteroids, shots = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    
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

        """
        if pygame.time.get_ticks() % 60 == 0:  # every second
            print(f"Number of asteroids: {len(asteroids)}")
            print(f"Number of shots    : {len(shots)}")
        """

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    # ^ keep display.flip() and dt as final call before loop

def display_text(self):
    font = pygame.font.Font("fonts/HyperspaceBoldItalic-jqm0.ttf", 32)
    text = font.renderer(f"test", False, "red")
    text_rect = text.get_rect()
    #text_rect.center = (0 + ( / 2), Y//2)


if __name__ == "__main__":
    main()