import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_Y, FPS
from dinosaur import Dinosaur
from cactus import Cactus

BG = pygame.image.load("Assets/Other/Track.png")

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
clock = pygame.time.Clock()
pygame.display.set_caption("Dinosaur Game")

def main():
    player = Dinosaur()
    run = True
    obstacles = []
    score = 0
    font = pygame.font.SysFont(None, 30)

    while run:
        screen.fill((255, 255, 255))
        screen.blit(BG, (0, GROUND_Y))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False

        # Auto play logic
        jump = False
        if len(obstacles) > 0:
            first_obstacle = obstacles[0]
            if first_obstacle.rect.x - player.dino_rect.x < 150 and not player.is_jumping:
                jump = True

        player.update(jump=jump)
        player.draw(screen)

        # If there are no obstacles on screen, add one by creating a new Cactus() object.
        if len(obstacles)==0:
            obstacles.append(Cactus())

        for obstacle in list(obstacles):
            obstacle.update()
            obstacle.draw(screen)

            # If a cactus has moved past the left edge of the screen, it's no longer visible.
            # So we remove it from the list and increase the score by 1.
            if obstacle.rect.x < -obstacle.rect.width:
                obstacles.remove(obstacle)
                score += 1

            # Checks if the dino’s rectangle overlaps with the cactus’s rectangle.
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                run = False

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (600, 20))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
