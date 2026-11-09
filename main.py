
import pygame

from game.game import Game
from game.player import Player
from game.world import World
from game.obstacle import Obstacle
from ui.game_over import GameOverScreen
from game.collectible import Collectible
from ui.menu import MenuScreen
from ui.pause import PauseScreen

# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/background_music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Window settings
WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frozen Water Run")

clock = pygame.time.Clock()


# Create game objects
game = Game()

game_over_sound = pygame.mixer.Sound("assets/sounds/game_over.wav")
game_over_sound.set_volume(0.6)

player = Player()
world = World()
obstacle = Obstacle(650, 500)
game_over_screen = GameOverScreen()
collectible = Collectible(750, 420)
menu_screen = MenuScreen()
pause_screen = PauseScreen()

previous_state = game.game_state
next_speed_threshold = 5


# Main game loop
while game.running:

    # Handle events
    game.handle_event(player)

    # Detect restart
    if previous_state == "game_over" and game.game_state == "playing":

        player.reset()
        obstacle.reset()
        collectible.collect()
        game.reset_score()

        next_speed_threshold = 5

    previous_state = game.game_state

    # Update objects ONLY during gameplay
    if game.game_state == "playing":

        world.update()
        player.update()
        obstacle.update()
        collectible.update()

        # Check obstacle collision
        if obstacle.check_collision(player):
            
            game_over_sound.play()
            game.change_state("game_over")
            print("GAME OVER!")

        # Award score when obstacle passes the player
        elif obstacle.x + obstacle.width < player.x and not obstacle.passed:

            game.increase_score(1)
            obstacle.passed = True

            print("Score:", game.score)

        # Check crystal collection
        if collectible.check_collection(player):

            game.increase_score(5)
            collectible.collect()

            print("Crystal collected! Bonus: 5")
            print("Score:", game.score)

        # Increase difficulty at every 5-point milestone
        while game.score >= next_speed_threshold:

            if obstacle.speed < obstacle.max_speed:

                obstacle.increase_speed()

                print("Obstacle speed increased:", obstacle.speed)

            next_speed_threshold += 5

    # Draw background
    world.draw(screen)

    # Display menu
    if game.game_state == "menu":

        menu_screen.draw(screen)

    # Draw gameplay objects
    elif game.game_state == "playing":

        player.draw(screen)
        obstacle.draw(screen)
        collectible.draw(screen)

        game.draw_score(screen)

    # Display frozen gameplay and Game Over screen
    elif game.game_state == "game_over":

        player.draw(screen)
        obstacle.draw(screen)
        collectible.draw(screen)

        game.draw_score(screen)
        game_over_screen.draw(screen)
        
    elif game.game_state == "paused":
        
        player.draw(screen)
        obstacle.draw(screen)
        collectible.draw(screen)
        
        game.draw_score(screen)
        pause_screen.draw(screen)

    # Update display
    pygame.display.flip()

    # Maintain 60 FPS
    clock.tick(60)


# Quit Pygame
pygame.quit()
