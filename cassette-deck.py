import vlc
import time
import subprocess
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

GAME_FONT = pygame.freetype.Font("Base-Font/NerkoOne-Regular.ttf", 24)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")

    # RENDER YOUR GAME HERE
    a = subprocess.run(['vlc-ctrl',  'info'], stdout=subprocess.PIPE)
    metadata = a.stdout

    print("-"*10)
    if str(metadata) == "b''":
        print("error, no vlc data")
        GAME_FONT.render_to(screen, (100, 100), "No vlc out found :(", (0, 0, 0))
    else:
        print(metadata)

        x = str(metadata).split("\\n")

        print(x)
        print("-"*5)
        print(str(x[0])[2:])
        print(x[1])
        print(x[2])
        print(x[5])

        album = str(str(x[0])[2:])
        title = str(x[1])
        artist = str(x[2])
        genre = str(x[5])
        x = 0
        y = 0
        GAME_FONT.render_to(screen, (x, 0+y), str(album), (0, 0, 0))
        GAME_FONT.render_to(screen, (x, 30+y), str(title), (0, 0, 0))
        GAME_FONT.render_to(screen, (x, 60+y), str(artist), (0, 0, 0))
        GAME_FONT.render_to(screen, (x, 90+y), str(genre), (0, 0, 0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  # limits FPS to 60

pygame.quit()