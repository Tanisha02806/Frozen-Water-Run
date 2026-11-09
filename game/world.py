
import pygame
import math
import random

class World:

    def __init__(self):

        self.water_y = 500
        self.wave_offset = 0

        # Ocean colors
        self.sky_color = (180, 225, 245)
        self.water_color = (65, 170, 220)
        self.wave_color = (145, 220, 245)
        
        self.clouds = [
            {"x": 100, "y": 100, "speed": 0.5, "size": 1},
            {"x": 400, "y": 160, "speed": 0.7, "size": 1.2},
            {"x": 750, "y": 75, "speed": 0.4, "size": 0.9},
            {"x": 1100, "y": 130, "speed": 0.6, "size": 1.1},
        ]
        
        self.mountain_offset = 0
        self.mountain_speed = 0.3
        
        self.snowflakes = []
        
        for i in range(30):
            
            self.snowflakes.append({
                "x": random.randint(0, 1000),
                "y": random.randint(0, 480),
                "speed": random.uniform(0.5, 1.5),
                "size": random.uniform(2, 4)
            })
            
        self.sparkles = []
        
        for i in range(15):
            
            self.sparkles.append({
                "x": random.randint(0, 1000),
                "y": random.randint(50, 450),
                "speed": random.uniform(0.3, 0.8)
            })
            
        self.water_sparkles = []
        
        for i in range(20):
            
            self.water_sparkles.append({
                "x": random.randint(0, 1000),
                "y": random.randint(510, 590),
                "speed": random.uniform(0.3, 1.0)
            })

    def update(self):

        # Animate water waves
        self.wave_offset += 0.06

        # Animate mountains
        self.mountain_offset += self.mountain_speed
        
        if self.mountain_offset >= 1000:
            self.mountain_offset = 0

        for cloud in self.clouds:
            
            cloud["x"] -= cloud["speed"]
            
            cloud_width = 120 * cloud["size"]
            
            if cloud["x"] < -cloud_width:
                
                cloud["x"] = 1050
                cloud["y"] = 60 + (cloud["size"] * 60)
                
        self.update_particles()

    def update_particles(self):
        
        for snow in self.snowflakes:
            
            snow["y"] += snow["speed"]
            snow["x"] -= 0.2
            
            if snow["y"] > self.water_y:
                
                snow["y"] = random.randint(-50, 0)
                snow["x"] = random.randint(0, 1000)
                
        for sparkle in self.sparkles:
            
            sparkle["y"] -= sparkle["speed"]
            
            if sparkle["y"] < 40:
                
                sparkle["y"] = 460
                sparkle["x"] = random.randint(0, 1000)
                
        for sparkle in self.water_sparkles:
            
            sparkle["x"] -= sparkle["speed"]
            
            if sparkle["x"] < 0:
                
                sparkle["x"] = 1000
                sparkle["y"] = random.randint(510, 590)
                
    def draw_particles(self, screen):
        
        for snow in self.snowflakes:
            
            pygame.draw.circle(
                screen,
                (255, 255, 255),
                (int(snow["x"]), int(snow["y"])),
                snow["size"]
            )
            
        for sparkle in self.sparkles:
            
            x = int(sparkle["x"])
            y = int(sparkle["y"])
            
            pygame.draw.circle(
                screen,
                (220, 245, 255),
                (x, y),
                3
            )
            
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (x - 5, y),
                (x + 5, y),
                1
            )
            
        for sparkle in self.water_sparkles:
            
            pygame.draw.circle(
                screen,
                (200, 245, 255),
                (int(sparkle["x"]), int(sparkle["y"])),
                2
            )
            
    def draw_cloud(self, screen, cloud):
        
        x = int(cloud["x"])
        y = int(cloud["y"])
        size = cloud["size"]

        pixel = int(12 * size)
        
        cloud_blocks = [
            (2, 2, 3, 2),
            (1, 3, 5, 3),
            (0, 4, 7, 2),
            (1, 5, 5, 1)
        ]
        
        shadow = (205, 230, 245)
        
        white = (250, 253, 255)
        
        for bx, by, bw, bh in cloud_blocks:
            
            pygame.draw.rect(
                screen,
                shadow,
                (
                    x + bx * pixel,
                    y + by * pixel + 3,
                    bw * pixel,
                    bh * pixel
                )
            )
            
            pygame.draw.rect(
                screen,
                white,
                (
                    x + bx * pixel,
                    y + by * pixel,
                    bw * pixel,
                    bh * pixel
                )
            )
    def draw_mountains(self, screen):
        
        mountain_dark = (105, 155, 195)
        snow = (245, 250, 255)
        
        mountains = [
            (
                [(0, 350), (180, 130), (360, 350)],
                [(180, 130), (145, 173), (180, 160), (215, 173)]
            ),
            (
                [(220, 350), (470, 100), (720, 350)],
                [(470, 100), (425, 145), (470, 130), (515, 145)]
            ),
            (
                [(600, 350), (820, 160), (1040, 350)],
                [(820, 160), (780, 195), (820, 185), (860, 195)]
            )
        ]
        
        for base_x in (
            -self.mountain_offset,
            1000 - self.mountain_offset
        ):
            
            for mountain, snow_peak in mountains:
                
                shifted_mountain = [
                    (x + base_x, y) 
                    for x, y in mountain
                ]
                
                shifted_snow = [
                    (x + base_x, y) 
                    for x, y in snow_peak
                ]

                pygame.draw.polygon(
                    screen,
                    mountain_dark,
                    shifted_mountain
                )
        
                pygame.draw.polygon(
                    screen,
                    snow,
                    shifted_snow
                )
                
    def draw(self, screen):

        width = screen.get_width()
        height = screen.get_height()

        # Sky background
        screen.fill(self.sky_color)
        
        for cloud in self.clouds:
            self.draw_cloud(screen, cloud)
            
        self.draw_mountains(screen)

        # Ocean base
        pygame.draw.rect(
            screen,
            self.water_color,
            (0, self.water_y, width, height - self.water_y)
        )

        # Animated waves
        for x in range(0, width + 10, 10):

            wave_y = self.water_y + math.sin(
                x * 0.025 + self.wave_offset
            ) * 5

            pygame.draw.circle(
                screen,
                self.wave_color,
                (x, int(wave_y)),
                3
            )
            
        self.draw_particles(screen)