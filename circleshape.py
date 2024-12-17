import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, other):
        return (self.radius + other.radius) > pygame.math.Vector2.distance_to(self.position, other.position)
    
    def is_exiting(self):
        exiting_bottom, exiting_top = self.position.y <= KILL_BORDER_BOTTOM, self.position.y >= KILL_BORDER_TOP
        exiting_left, exiting_right = self.position.x <= KILL_BORDER_LEFT, self.position.x >= KILL_BORDER_RIGHT
        return exiting_bottom or exiting_left or exiting_right or exiting_top