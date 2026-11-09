import pygame

class PauseScreen:
    
    def __init__(self):
        
        self.title_font = pygame.font.Font(None, 90)
        self.instruction_font = pygame.font.Font(None, 35)
        
    def draw(self, screen):
        
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 40, 160))
        screen.blit(overlay, (0, 0))
        
        white = (255, 255, 255)
        ice_blue = (150, 220, 255)
        
        title = self.title_font.render(
            "PAUSED",
            True,
            white
        )
        
        screen.blit(
            title,
            title.get_rect(center=(500, 220))
        )
        
        resume_text = self.instruction_font.render(
            "PRESS P OR ENTER TO RESUME",
            True,
            ice_blue
        )
        
        screen.blit(
            resume_text,
            resume_text.get_rect(center=(500, 330))
        )
        
        menu_text = self.instruction_font.render(
            "QUIT TO MENU - ESC",
            True,
            white
        )
        
        screen.blit(
            menu_text,
            menu_text.get_rect(center=(500, 400))
        )