import pygame
from constants import GROUND_Y

# Load assets into memory
START = pygame.image.load("Assets/Dino/DinoStart.png")

DUCKING = [
    pygame.image.load("Assets/Dino/DinoDuck1.png"),
    pygame.image.load("Assets/Dino/DinoDuck2.png"),
]

BIRD = [
    pygame.image.load("Assets/Birds/Bird1.png"),
    pygame.image.load("Assets/Birds/Bird2.png"),
]

CLOUD = pygame.image.load("Assets/Other/Cloud.png")

class Dinosaur:
    X_POS = 80
    Y_POS = GROUND_Y
    JUMP_VEL = 11.5

    def __init__(self):
        self.run_img = [
            pygame.image.load("Assets/Dino/DinoRun1_converted.png"),
            pygame.image.load("Assets/Dino/DinoRun2_converted.png")
        ]
        self.jump_img = pygame.image.load("Assets/Dino/DinoJump.png")

        # Sets the current image to the first running frame
        self.image = self.run_img[0]
        # Creates a rectangle(position and size) around the image.This is used for positioning and collision detection.
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS - self.dino_rect.height
        self.is_running = True
        self.is_jumping = False
        self.jump_vel = self.JUMP_VEL
        self.step_index = 0

    def update(self, jump=False):
        if self.is_jumping:
            self.jump()
        elif jump and not self.is_jumping:
            self.is_jumping = True
            self.is_running = False
        else:
            self.run()

    def run(self):
        # frames 0–4 → show run_img[0]
        # frames 5–9 → show run_img[1]
        index = self.step_index // 15
        if index >= len(self.run_img):
            index = 0
        self.image = self.run_img[index]
        # Ensures the dino is standing on the ground when it's running.
        # This resets the Y position in case it just landed from a jump.
        if not self.is_jumping:
            self.dino_rect.y = self.Y_POS - self.dino_rect.height

        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        # Dino starts jump: jump_vel = 8.5
        # y decreases (dino moves up), jump_vel goes down
        # At peak: jump_vel = 0, then becomes negative
        # Dino falls back down
        # When jump_vel < -8.5, it lands and resets
        self.image = self.jump_img
        self.dino_rect.y -= self.jump_vel * 4
        # Decreases the jump velocity over time — simulates gravity
        self.jump_vel -= 0.8
        # Once jump_vel reaches a negative value equal to the starting jump speed, that means the dino has landed.
        if self.jump_vel < -self.JUMP_VEL:
            self.is_jumping = False
            self.is_running = True
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen):
        # Display the dinosaur on the screen during each frame of the game
        screen.blit(self.image, self.dino_rect)

