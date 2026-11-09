
import pygame
import random
from game.resources import resource_path


class Obstacle:

    def __init__(self, x, ground_y, obstacle_type="small"):

        self.obstacle_type = obstacle_type
        self.ground_y = ground_y

        # Set dimensions according to obstacle type
        if obstacle_type == "small":
            self.width = 50
            self.height = 45

        elif obstacle_type == "spike":
            self.width = 45
            self.height = 90

        elif obstacle_type == "double":
            self.width = 105
            self.height = 55

        else:
            raise ValueError(f"Unknown obstacle type: {obstacle_type}")

        # Load obstacle sprite
        self.load_image()

        # Position
        self.x = x
        self.y = ground_y - self.height

        # Collision rectangle
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

        # Movement settings
        self.speed = 6
        self.max_speed = 12

        self.passed = False

    def load_image(self):

        # Select image according to obstacle type
        if self.obstacle_type == "small":
            image_path = "assets/images/small_obstacle.png"

        elif self.obstacle_type == "spike":
            image_path = "assets/images/spike_obstacle.png"

        elif self.obstacle_type == "double":
            image_path = "assets/images/double_obstacle.png"

        else:
            raise ValueError(
                f"Unknown obstacle type: {self.obstacle_type}"
            )

        # Load image using resource path
        self.image = pygame.image.load(
            resource_path(image_path)
        ).convert_alpha()

        # Resize image
        self.image = pygame.transform.scale(
            self.image,
            (self.width, self.height)
        )

    def draw(self, screen):

        # Draw pixel-art obstacle
        screen.blit(
            self.image,
            (int(self.x), int(self.y))
        )

        # Update collision rectangle
        self.rect.topleft = (
            int(self.x),
            int(self.y)
        )

    def change_type(self):

        # Randomly select a new obstacle type
        self.obstacle_type = random.choice(
            ["small", "spike", "double"]
        )

        # Update dimensions
        if self.obstacle_type == "small":
            self.width = 50
            self.height = 45

        elif self.obstacle_type == "spike":
            self.width = 45
            self.height = 90

        elif self.obstacle_type == "double":
            self.width = 105
            self.height = 55

        # Load the new obstacle image
        self.load_image()

        # Adjust vertical position
        self.y = self.ground_y - self.height

        # Update collision rectangle
        self.rect = pygame.Rect(
            int(self.x),
            int(self.y),
            self.width,
            self.height
        )

    def update(self):

        self.x -= self.speed

        # Recycle obstacle after it leaves the screen
        if self.x < -self.width:

            self.x = 1050
            self.passed = False

            # Select a new random obstacle
            self.change_type()

        # Update collision rectangle
        self.rect.x = int(self.x)

    def check_collision(self, player):

        return self.rect.colliderect(player.rect)

    def reset(self):

        # Restore starting position
        self.x = 650
        self.y = self.ground_y - self.height

        # Restore original speed
        self.speed = 6

        # Allow scoring again
        self.passed = False

        # Update collision rectangle
        self.rect.topleft = (
            int(self.x),
            int(self.y)
        )

    def increase_speed(self):

        if self.speed < self.max_speed:

            self.speed = min(
                self.speed + 0.5,
                self.max_speed
            )
