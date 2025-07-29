import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        original_image = pygame.image.load("Assets/alien.png")
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > self.screen.get_width():
            self.rect.right = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)