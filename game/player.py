import pygame
from game.resources import resource_path

class Player:

    def __init__(self):

        # Player dimensions
        self.width = 100
        self.height = 100

        # Ground position
        self.ground_y = 500

        # Player position
        self.x = 150
        self.y = self.ground_y - self.height

        # Collision rectangle
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

        # Jump settings
        self.velocity_y = 0
        self.jump_strength = -18
        self.is_jumping = False

        # Running animation settings
        self.animation_counter = 0
        self.animation_frame = 0

        # Load player sprite
        self.sprite = pygame.image.load(
            resource_path("assets/images/player.png")
        ).convert_alpha()

        # Resize sprite
        self.sprite = pygame.transform.scale(
            self.sprite,
            (self.width, self.height)
        )

        # Jump sound effect
        self.jump_sound = pygame.mixer.Sound(
            resource_path("assets/sounds/jump.wav")
        )
        self.jump_sound.set_volume(0.5)

    def draw(self, screen):

        # Draw pixel-art princess and horse
        screen.blit(
            self.sprite,
            (int(self.x), int(self.y))
        )

    def jump(self):

        if not self.is_jumping:

            self.velocity_y = self.jump_strength
            self.is_jumping = True

            # Play jump sound
            self.jump_sound.play()

    def update(self):

        # Running animation timer
        if not self.is_jumping:

            self.animation_counter += 1

            if self.animation_counter >= 8:

                self.animation_frame = (
                    self.animation_frame + 1
                ) % 2

                self.animation_counter = 0

        # Jump physics
        if self.is_jumping:

            # Apply gravity
            self.velocity_y += 0.8

            # Update vertical position
            self.y += self.velocity_y

            # Update collision rectangle
            self.rect.y = int(self.y)

            # Ground collision
            if self.y >= self.ground_y - self.height:

                self.y = self.ground_y - self.height

                self.velocity_y = 0
                self.is_jumping = False

                self.rect.y = int(self.y)

    def reset(self):

        self.y = self.ground_y - self.height
        self.velocity_y = 0
        self.is_jumping = False

        self.animation_counter = 0
        self.animation_frame = 0

        self.rect.topleft = (
            self.x,
            int(self.y)
        )
