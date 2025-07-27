import pygame
import random
from constants import SCREEN_WIDTH, GROUND_Y

SMALL_CACTUS = [
    pygame.image.load("Assets\Cactus\SmallCactus1.png"),
    pygame.image.load("Assets\Cactus\SmallCactus2.png"),
    pygame.image.load("Assets\Cactus\SmallCactus3.png"),
]

LARGE_CACTUS = [
    pygame.image.load("Assets\Cactus\LargeCactus1.png"),
    pygame.image.load("Assets\Cactus\LargeCactus2.png"),
    pygame.image.load("Assets\Cactus\LargeCactus3.png"),
]

class Cactus:
    def __init__(self):
        if random.choice(["small", "large"])=="small":
            self.image = random.choice(SMALL_CACTUS)
        else:
            self.image = random.choice(LARGE_CACTUS)

        # Create rect and position at ground‐level off the right edge
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = GROUND_Y - self.rect.height

    def update(self):
        self.rect.x -= 10  # move left

    def draw(self, screen):
        screen.blit(self.image, self.rect)