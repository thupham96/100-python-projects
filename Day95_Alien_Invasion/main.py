import pygame
import sys
from ship import Ship
from bullet import Bullet
from alien import Alien
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")
clock = pygame.time.Clock()

ship = Ship(screen)
bullets = []
alien_bullets = []
aliens = [Alien(screen, x * 50, y * 50) for y in range(5) for x in range(17)]
alien_drop_interval = 3000
alien_bullet_interval = 500 # 10,000 milliseconds = 10 seconds
last_drop_time = pygame.time.get_ticks()
last_alien_bullet_time = pygame.time.get_ticks()
game_over = False
SPEED = -7

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bullets.append(Bullet(screen, ship.rect.centerx, ship.rect.centery, SPEED))

    keys = pygame.key.get_pressed()
    ship.move(keys)

    # Clear screen
    screen.fill((30, 30, 30))

    # Update bullets
    for bullet in bullets[:]:
        if not game_over:
            bullet.update()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)
            bullet.draw()

    # Update aliens
    for alien in aliens:
        if not game_over:
            alien.update()
            alien.draw()

    # New bullet from a random alien every 1 seconds
    current_alien_bullet_time = pygame.time.get_ticks()
    if current_alien_bullet_time - last_alien_bullet_time > alien_bullet_interval and len(aliens) > 0:
        random_alien = random.choice(aliens)
        alien_bullet = Bullet(screen, random_alien.rect.centerx, random_alien.rect.centery, -SPEED)
        alien_bullets.append(alien_bullet)
        last_alien_bullet_time = current_alien_bullet_time

    for alien_bullet in alien_bullets:
        if not game_over:
            alien_bullet.update()
            alien_bullet.draw()
        if alien_bullet.rect.x >= HEIGHT:
            alien_bullets.remove(alien_bullet)
        if alien_bullet.rect.colliderect(ship.rect):
            game_over = True

    # Bullet-alien collision
    for bullet in bullets:
        for alien in aliens:
            if bullet.rect.colliderect(alien.rect):
                bullets.remove(bullet)
                aliens.remove(alien)
                break

    # Aliens will move down every 5 seconds
    current_time = pygame.time.get_ticks()
    if current_time - last_drop_time > alien_drop_interval:
        for alien in aliens:
            alien.rect.y += 30  # Drop each alien down by 30 pixels
        last_drop_time = current_time

    # Alien-ship collision
    for alien in aliens:
        if alien.rect.bottom >= HEIGHT or alien.rect.colliderect(ship.rect):
            game_over = True

    if game_over:
        font = pygame.font.SysFont(None, 72)
        text = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    # No alien left - play has won
    if len(aliens) == 0:
        font = pygame.font.SysFont(None, 72)
        text = font.render("YOU HAVE WON!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    ship.draw()
    pygame.display.flip()
    clock.tick(60)