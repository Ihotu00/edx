import os
os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"  # Force software rendering

import pygame

# pygame setup
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 300  # movement speed

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Draw the player circle
    pygame.draw.circle(screen, "red", player_pos, 40)

    # Get keys pressed and update position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # calculate delta time (dt) to make the movement frame-rate independent
    dt = clock.tick(60) / 1000  # 60 FPS limit

pygame.quit()
