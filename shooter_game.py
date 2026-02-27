import pygame  # Game library

# ----------------------------
# SETUP
# ----------------------------

pygame.init()  # Initialize all pygame modules

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)  # Dinamic Window height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create window

pygame.display.set_caption("Shooter Game")  # Window title

# FPS
clock = pygame.time.Clock()  # Controls FPS
FPS = 60

# COLORS
BLUE_COLOR = (11, 43, 65)
GREEN_COLOR = (25, 60, 65)
RED_COLOR = (89, 28, 33)
YELLOW_COLOR = (242, 183, 5)

BG_COLOR = BLUE_COLOR

# VARIABLES

running = True  # Main loop control

# player
player_x_pos = 300
player_y_pos = 500
player_scale = 2
player_img = pygame.image.load("./assets/img/player/Idle/0.png").convert_alpha()
player_img = pygame.transform.scale(surface= player_img, size= (player_img.get_width()*player_scale, player_img.get_height()*player_scale))
player_rect = player_img.get_rect()
player_rect.center = (player_x_pos, player_y_pos)


# ----------------------------
# MAIN LOOP
# ----------------------------

while running:

    # ----------------------------
    # EVENTS
    # ----------------------------

    # EVENTS (keyboard, mouse, window)
    for event in pygame.event.get():

        # Close the window (X button)
        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN happens ONCE when a key is pressed
        if event.type == pygame.KEYDOWN:

            # Press ESC to quit
            if event.key == pygame.K_ESCAPE:
                running = False

        # KEYUP happens ONCE when a key is released
        if event.type == pygame.KEYUP:
            pass  # Placeholder for future logic

    # ----------------------------
    # RENDERING
    # ----------------------------

    # Render everything
    screen.fill(BG_COLOR)  # Clear screen every frame
    # player
    # Display player img at player rect position
    screen.blit(player_img, player_rect)



    pygame.display.update()  # Show frame

    # FPS LIMIT
    clock.tick(FPS)

# ----------------------------
# CLEANUP
# ----------------------------

pygame.quit()  # Close pygame safely
quit()         # Exit program