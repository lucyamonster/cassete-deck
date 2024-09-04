import vlc
import time
import subprocess
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("Cassette Deck")
clock = pygame.time.Clock()
running = True
tick = 0

x = 0
y = 0

x_text = x
y_text = y

x_cas = x + 10
y_cas = y - 20

clockrate = 20
scale = 64
fontsize = scale

cas_rotaition_limit = 25

just_text_mode = False

if just_text_mode:
    screen = pygame.display.set_mode((scale * 16, scale * 5))
else:
    screen = pygame.display.set_mode(((scale * 16)*1, (scale * 5)*1.8))
    y_text += 128 * (scale//31)

GAME_FONT = pygame.freetype.Font("Base-Font/NerkoOne-Regular.ttf", fontsize)
cassette_img = pygame.image.load("Icons/Cassette 128x128.png")
fontsize += (fontsize//4)

updatedisplaysize = False

def slice_and_print():
    # Split by line
    splitdata = str(metadata).split("\\n")

    # Prep and assign lines
    album = str(str(splitdata[0])[2:])
    title = str(splitdata[1])
    artist = str(splitdata[2])
    genre = str(splitdata[5])

    # Print to window
    GAME_FONT.render_to(screen, (x_text, (fontsize*0)+y_text), str(album), (0, 0, 0))
    GAME_FONT.render_to(screen, (x_text, (fontsize*1)+y_text), str(title), (0, 0, 0))
    GAME_FONT.render_to(screen, (x_text, (fontsize*2)+y_text), str(artist), (0, 0, 0))
    GAME_FONT.render_to(screen, (x_text, (fontsize*3)+y_text), str(genre), (0, 0, 0))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tick += 1
    print(tick )

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((255,0,255,0))

    # RENDER YOUR GAME HERE
    a = subprocess.run(['vlc-ctrl',  'info'], stdout=subprocess.PIPE)
    metadata = a.stdout

    if str(metadata) == "b''":
        GAME_FONT.render_to(screen, (100, 100), "No vlc out found :(", (0, 0, 0))
    else:
        animated_cassette = pygame.transform.rotozoom(cassette_img, (tick % cas_rotaition_limit) - (cas_rotaition_limit // 2), scale//17)
        screen.blit(animated_cassette, (x_cas, y_cas))
        slice_and_print()

    # flip() the display to put your work on screen
    pygame.display.flip()

    if updatedisplaysize:
        screen = pygame.display.set_mode((scale * 16, scale * 5))
        updatedisplaysize = False

    clock.tick(clockrate)  # limits FPS to 60

pygame.quit()