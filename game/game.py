import pygame

from game import player
from pathlib import Path

MENU = "menu"
PLAYING = "playing"
PAUSED = "paused"
GAME_OVER = "game_over"

class Game:
    
    def __init__(self):
        
        self.game_state = MENU
        self.score = 0
        self.high_score = self.load_high_score()
        self.running = True
        
    def change_state(self, new_state):
        
        self.game_state = new_state
        
    def reset_score(self):
        self.score = 0
        
    def increase_score(self, points=1):
        
        self.score += points
        
        if self.score > self.high_score:
            
            self.high_score = self.score
            self.save_high_score()
            
    
    def handle_event(self, player):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.quit_game()

            if event.type == pygame.KEYDOWN:

                # MENU controls
                if self.game_state == MENU:

                    if event.key == pygame.K_RETURN:
                        self.change_state(PLAYING)

                    elif event.key == pygame.K_ESCAPE:
                        self.quit_game()

                # PLAYING controls
                elif self.game_state == PLAYING:

                    if event.key == pygame.K_p:
                        self.change_state(PAUSED)

                    elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        player.jump()

                # PAUSED controls
                elif self.game_state == PAUSED:

                    if event.key == pygame.K_p or event.key == pygame.K_RETURN:
                        self.change_state(PLAYING)
                        
                    elif event.key == pygame.K_ESCAPE:
                        self.change_state(MENU)

                # GAME OVER controls
                elif self.game_state == GAME_OVER:

                    if event.key == pygame.K_r:
                        self.change_state(PLAYING)

                    elif event.key == pygame.K_q:
                        self.quit_game()
        
    def quit_game(self):
        
        self.running = False
        
    def draw_score(self, screen):
        
        font = pygame.font.Font(None, 40)
        
        x = screen.get_width() - 200
        
        score_text = font.render(
            f"Score: {self.score}",
            True,
            (255, 255, 255)
        )
        
        screen.blit(score_text, (x, 30))
        
        high_score_text = font.render(
            f"Best Score: {self.high_score}",
            True,
            (255, 230, 150)
        )
        
        screen.blit(high_score_text, (x, 70))
        
    def load_high_score(self):
        
        file_path = Path(__file__).resolve().parent.parent / "data" / "highscore.txt"
        
        try:
            with open(file_path, "r") as file:
                return int(file.read().strip())
            
        except (FileNotFoundError, ValueError):
            return 0
        
    def save_high_score(self):
        
        file_path = Path(__file__).resolve().parent.parent / "data" / "highscore.txt"
        
        with open(file_path, "w") as file:
            file.write(str(self.high_score))