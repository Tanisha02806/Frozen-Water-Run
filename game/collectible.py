import pygame
import random
from game.resources import resource_path

class Collectible:

    def __init__(self, x, y):
        self.width = 30
        self.height = 40

        self.x = x
        self.y = y

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

        self.speed = 6

        # Collection sound
        self.collect_sound = pygame.mixer.Sound(resource_path("assets/sounds/collect.wav"))
        self.collect_sound.set_volume(0.6)

        # Sparkle effect
        self.sparkles = []
        self.sparkle_duration = 20

    def draw(self, screen):

        ice_blue = (100, 220, 255)
        light_blue = (200, 245, 255)
        dark_blue = (65, 160, 220)
        white = (255, 255, 255)

        # Draw crystal
        pygame.draw.polygon(
            screen,
            ice_blue,
            [
                (self.x + 15, self.y),
                (self.x + 28, self.y + 12),
                (self.x + 23, self.y + 32),
                (self.x + 15, self.y + 40),
                (self.x + 7, self.y + 32),
                (self.x + 2, self.y + 12)
            ]
        )

        pygame.draw.polygon(
            screen,
            light_blue,
            [
                (self.x + 15, self.y + 3),
                (self.x + 15, self.y + 35),
                (self.x + 7, self.y + 29),
                (self.x + 5, self.y + 13),
            ]
        )

        pygame.draw.line(
            screen,
            dark_blue,
            (self.x + 15, self.y),
            (self.x + 15, self.y + 40),
            2
        )

        pygame.draw.circle(
            screen,
            white,
            (self.x + 11, self.y + 10),
            3
        )

        # Draw sparkle particles
        for sparkle in self.sparkles:
            pygame.draw.circle(
                screen,
                sparkle["color"],
                (int(sparkle["x"]), int(sparkle["y"])),
                max(1, int(sparkle["life"] / 5))
            )

    def update(self):

        # Move crystal
        self.x -= self.speed

        if self.x < -self.width:
            self.x = 1050

        self.rect.x = int(self.x)

        # Update sparkle particles
        for sparkle in self.sparkles:
            sparkle["x"] += sparkle["vx"]
            sparkle["y"] += sparkle["vy"]

            sparkle["vy"] += 0.1
            sparkle["life"] -= 1

        # Remove expired particles
        self.sparkles = [
            sparkle for sparkle in self.sparkles
            if sparkle["life"] > 0
        ]

    def check_collection(self, player):

        return self.rect.colliderect(player.rect)

    def collect(self):

        # Play collection sound
        self.collect_sound.play()

        # Create sparkle burst at crystal position
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2

        sparkle_colors = [
            (255, 255, 255),
            (180, 240, 255),
            (100, 220, 255),
            (220, 250, 255)
        ]

        for _ in range(15):
            self.sparkles.append({
                "x": center_x,
                "y": center_y,
                "vx": random.uniform(-3, 3),
                "vy": random.uniform(-4, 1),
                "life": self.sparkle_duration,
                "color": random.choice(sparkle_colors)
            })

        # Move crystal away after collection
        self.x = 1050
        self.rect.x = int(self.x)