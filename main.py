import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock, dt = pygame.time.Clock(), 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        player.update(dt)

        dt = clock.tick(60) / 1000
        pygame.display.flip()
    # ^ keep display.flip() as final call before loop


if __name__ == "__main__":
    main()