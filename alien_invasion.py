import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_invasion")

    #Make the Play button
    play_button = Button(ai_settings, screen, "Play")

    #Create an instance to store game statistics
    stats = GameStats(ai_settings)

    #Set the background color
    bg_color = (230, 230, 230)

    #Make a ship
    ship = Ship(ai_settings, screen)

    #Make a group to store bullets in
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start the main loop of the game
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        #Move to the ship based on the key press
        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

            #Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
