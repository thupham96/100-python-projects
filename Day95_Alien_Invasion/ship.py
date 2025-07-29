import pygame

class Ship:
    def __init__(self, screen):
        self.screen = screen
        original_image = pygame.image.load("Assets/ship.png")
        self.image = pygame.transform.scale(original_image, (64, 64))
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()

        # Position the ship so that its mid-bottom is aligned with the midbottom of the screen rect.
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
