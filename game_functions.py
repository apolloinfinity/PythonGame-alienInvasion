import sys
import pygame

def check_events(ship):
    """Respond to keypresses and moust events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                # Move the ship to the right
                ship.rect.centerx += 1



def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()