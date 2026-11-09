import pygame

class GameOverScreen:
    
    def __init__(self):
        
        self.title_font = pygame.font.Font(None, 90)
        self.text_font = pygame.font.Font(None, 40)
        
        self.white = (255, 255, 255)
        self.ice_blue = (100, 200, 240)
        self.dark_blue = (0, 0, 40)
        
    def draw(self, screen):
        
        width = screen.get_width()
        height = screen.get_height()
        
        overlay = pygame.Surface((width, height))
        overlay.set_alpha(160)
        overlay.fill(self.dark_blue)
        
        screen.blit(overlay, (0, 0))
        
        title = self.title_font.render(
            "GAME OVER",
            True,
            self.white
        )
        
        screen.blit(
            title,
            title.get_rect(center=(width // 2, 220))
        )
        
        restart = self.text_font.render(
            "Press R to Restart",
            True,
            self.ice_blue
        )
        
        screen.blit(
            restart,
            restart.get_rect(center=(width // 2, 320))
        )
        
        quit_text = self.text_font.render(
            "Press Q to Quit",
            True,
            self.white
        )
        
        screen.blit(
            quit_text,
            quit_text.get_rect(center=(width // 2, 380))
        )