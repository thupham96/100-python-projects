import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, 4, 10)
        self.color = (255, 255, 0)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)