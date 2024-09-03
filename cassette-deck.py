import vlc
import time
import subprocess
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

GAME_FONT = pygame.freetype.Font("NerkoOne-Regular.ttf", 24)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    a = subprocess.run(['vlc-ctrl',  'info'], stdout=subprocess.PIPE)
    metadata = a.stdout

    print(metadata)
    
    GAME_FONT.render_to(screen, (100, 100), str(metadata), (0, 0, 0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  # limits FPS to 60

pygame.quit()