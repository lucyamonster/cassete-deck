import vlc
import time
import subprocess
import pygame

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True

x = 0
y = 0
clockrate = 5
scale = 64
fontsize = scale

screen = pygame.display.set_mode((scale * 16, scale * 5))

GAME_FONT = pygame.freetype.Font("Base-Font/NerkoOne-Regular.ttf", fontsize)
fontsize += (fontsize//4)

def slice_and_print():
    # Split by line
    splitdata = str(metadata).split("\\n")

    # Prep and assign lines
    album = str(str(splitdata[0])[2:])
    title = str(splitdata[1])
    artist = str(splitdata[2])
    genre = str(splitdata[5])

    # Print to window
    GAME_FONT.render_to(screen, (x, (fontsize*0)+y), str(album), (0, 0, 0))
    GAME_FONT.render_to(screen, (x, (fontsize*1)+y), str(title), (0, 0, 0))
    GAME_FONT.render_to(screen, (x, (fontsize*2)+y), str(artist), (0, 0, 0))
    GAME_FONT.render_to(screen, (x, (fontsize*3)+y), str(genre), (0, 0, 0))


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

    if str(metadata) == "b''":
        GAME_FONT.render_to(screen, (100, 100), "No vlc out found :(", (0, 0, 0))
    else:
        slice_and_print()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(clockrate)  # limits FPS to 60

pygame.quit()