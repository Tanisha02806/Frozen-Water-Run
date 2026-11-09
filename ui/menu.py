import pygame

class MenuScreen:
    
    def __init__(self):
        
        self.title_font = pygame.font.Font(None, 90)
        self.subtitle_font = pygame.font.Font(None, 35)
        self.instruction_font = pygame.font.Font(None, 30)
        
    def draw(self, screen):
        
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 40, 110))
        screen.blit(overlay, (0, 0))
        
        white = (255, 255, 255)
        ice_blue = (120, 210, 255)
        light_blue = (190, 235, 255)
        
        title = self.title_font.render(
            "FROZEN WATER RUN",
            True,
            white
        )
        
        screen.blit(
            title,
            title.get_rect(center=(500, 180))
        )
        
        subtitle = self.subtitle_font.render(
            "A Magical Ice Adventure",
            True,
            ice_blue
        )
        
        screen.blit(
            subtitle,
            subtitle.get_rect(center=(500, 250))
        )
        
        start_text = self.instruction_font.render(
            "PRESS ENTER TO START",
            True,
            light_blue
        )
        
        screen.blit(
            start_text,
            start_text.get_rect(center=(500,370))
        )
        
        controls = self.instruction_font.render(
            "SPACE / UP ARROW - JUMP",
            True,
            white
        )
        
        screen.blit(
            controls,
            controls.get_rect(center=(500, 440))
        )
        
        quit_text = self.instruction_font.render(
            "ESC - QUIT",
            True,
            white
        )
        
        screen.blit(
            quit_text,
            quit_text.get_rect(center=(500,490))
        )