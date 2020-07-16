import pygame

# initializing the game library
pygame.init()

# setting up display dimensions
display_height = 800
display_width = 800

# assigning colors to variables
white_color = (255, 255, 255)
black_color = (0, 0, 0)

# setting up display itself
game_display = pygame.display.set_mode( ( display_width, display_height ) )
game_display.fill(white_color)

# setting up game controlling clock, fps and whether it is over
clock = pygame.time.Clock()
game_fps = 60
game_over = False

# creating screen updating routine
while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
    clock.tick(game_fps)

pygame.quit()
quit()
