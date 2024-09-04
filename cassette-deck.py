import vlc
import time
import subprocess
import pygame

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
scale = 64
screen = pygame.display.set_mode((scale * 16, scale * 5))


fontsize = scale

GAME_FONT = pygame.freetype.Font("Base-Font/NerkoOne-Regular.ttf", fontsize)
fontsize += (fontsize//4)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((255,0,255,0))

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
        GAME_FONT.render_to(screen, (x, (fontsize*0)+y), str(album), (0, 0, 0))
        GAME_FONT.render_to(screen, (x, (fontsize*1)+y), str(title), (0, 0, 0))
        GAME_FONT.render_to(screen, (x, (fontsize*2)+y), str(artist), (0, 0, 0))
        GAME_FONT.render_to(screen, (x, (fontsize*3)+y), str(genre), (0, 0, 0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  # limits FPS to 60

pygame.quit()